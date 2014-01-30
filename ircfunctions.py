#!/usr/bin/env python
#Filename: ircfunctions.py
import sys
"""
This is a file containing several of the functions that will be used 
by the irc bot. This includes send <expand as things are added> 
"""
def out(data):
	sys.stderr.write(data + "\n")
class bot:
	def __init__(self, irc):
		self.irc = irc
	def send_message(self, chan, message):
		"""
		This will be the function for sending messages.
		This takes two arguments, and sends a message, to the chan of the 
		first argument, and the text of the second.
		It then prints out something for the console, signifying this event.
		"""
		self.irc.send("PRIVMSG {0} :{1}\r\n".format(chan, message))
		out("BOT ==> {0} | {1}".format(chan, message))
	def send(self, message):
		"""
		This is for sending things to the server as opposed to a chan/user
		"""
		self.irc.send(message + "\r\n")
		out("BOT ==> {0}".format(message))
