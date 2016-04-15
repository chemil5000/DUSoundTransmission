### Python receiver module for nonverbal communication ###
### designed to be impemented on a Nao Robot           ###
### David Chan - April 3, 2016                         ###

##
# Imports
##
import socket
import numpy as np
import pickle
import AudioHandlerReceiver

##
# Global Vars
##
SERVER_PORT = 14000


##
# Socket connection - wait on the socket, and then handle the connection.
##
s = socket.socket()
s.bind(('', SERVER_PORT))
s.listen(1)
try:
	while True:
		print 'Waiting for connection...'
		c, addr = s.accept()
		print 'Recieved connection from',addr
		print 'Handling connection from',addr
		AudioHandlerReceiver.handle_connection(c, addr, SERVER_PORT)
		print 'Connection from',addr,'handled. Disconnecting.'
		c.close()
		print 'Connection from',addr,'closed.'
except KeyboardInterrupt:
	print 'Interrupted... shutting down.'
	s.close()
	exit()
