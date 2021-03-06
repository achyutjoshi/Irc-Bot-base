#!/usr/bin/env python
#Filename: Main.py
import ircfunctions
import ssl
import socket
# The following lines, are for setting the constants that the irc bot
# will connect to.
OWNER = "~NDJ" #Set a bot owner, who can reset and control bot
HOST = "irc.rizon.net" #All the constants used here, can be edited, this is simply for testing
CHANS = ["#ndjr"] # A list, so we can connect to multiple chans
NICK = "NDJr"
USER = 'NDJr'
IDENT = 'NDJr'
PORT = 6667
"""
The bot runs with a user heirchy, of:
OWNER --> ADMIN --> ALLOWED --> USER --> IGNORED
All of these are managed via lists
OWNER can restart, make the bot quit, and anything that would alter it's state
ADMIN can pause, set allowed, ignored and have bot join & part chans
USER can interact with the bot,its purpose
IGNORED will simply have their commands disregarded.
"""
ADMIN = [OWNER]
ALLOWED = []
IGNORED = []
"""
The bot requires a nick key, in order to identify as a user.
This should be stored in a file, called: key.txt. It will read the text 
from there.
"""
with open("key.txt", "r") as key_file: #This file is NOT tracked in git :)
	NICK_KEY = key_file.readlines()[0].strip()
#Now, connect
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'BOT IS CONNECTING TO:' + HOST
socket.connect((HOST, PORT))
irc = ssl.wrap_socket(socket)
irc.send("USER " + NICK + " " + NICK + " " + NICK + " :NDJrbot\n")
irc.send("NICK " + NICK + "\n")
bot = ircfunctions.bot(irc) #The bot object
"""
Now, a loop to receive data
"""
while True:
     # This is the parsing of the message
	text = irc.recv(4096) # Text, will be the data that we get    
	"""
	The first things that need to be checked for, are the PINGS from the server
	the message of the day, and nickserv PRICMSGs
	"""
	
	if text.find("PING") != -1:
		bot.send('PONG ' + text.split()[1] + '\r\n')
		print "PINGED"
	if text.find("MOTD") != -1:
		bot.send("PRIVMSG Nickserv :identify {0}\r\n".format(NICK_KEY))
	if text.find("Password accepted - you are now recognized.") != -1:
		for chan in CHANS:
			bot.send('JOIN ' + chan + '\r\n')
	if text.find("Nickname in user") != -1:
		bot.send("PRIVMSG Nickserv :GHOST {0}\r\n".format(NICK_KEY))
	try:
		nick = text.split(":")[1].split("!")[0]
		chan = text.split(" ")[2]
		message = ":".join(text.split(":")[2:])
		message_prefix = message.split()[0]
		user = text.split("!")[1].split("@")[0]
	except IndexError:
		pass
	if message_prefix == "!quit" and user in ADMIN:
		bot.send("QUIT :Goodbye")
		exit() 
	if message_prefix == "!say":
		bot.send_message(chan,  nick + ", " + " ".join(message.split()[1::]))
	

	ircfunctions.out(text)

