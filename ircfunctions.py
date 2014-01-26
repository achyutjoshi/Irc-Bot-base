#!/usr/bin/env python
#Filename: irc.py
"""
This is a file containing several of the functions that will be used 
by the irc bot. This includes send <expand as things are added> 
"""
def bot_send(irc, chan, message):
	"""
	This will be the function for sending messages.
	This takes two arguments, and sends a message, to the chan of the 
	first argument, and the text of the second.
	It then prints out something for the console, signifying this event.
	"""
	irc.send("PRIVMSG {0} :{1}\r\n".format(chan, message))
	print "BOT ==> {0} | {1}".format(chan, message)
	

