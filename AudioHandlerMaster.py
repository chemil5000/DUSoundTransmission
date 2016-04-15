### Python handler module for nonverbal communication ###
### designed to be impemented on a master server      ### 
### sending info                                      ###
### David Chan - April 3, 2016                        ###


##
# Imports
##

import numpy as np
import pickle
import socket

##
# Handle commands
##

def handle_command(send_con, recv_con, tokens):
	
	## Send information

	if tokens[0] == 'quit':
		return False

	elif tokens[0] == 'location':
		import random
		locx = random.randrange(0,10)
		locy = random.randrange(0,10)
		to_send = np.array([locx,locy])
		print 'Sending',to_send
		send_con.send('location')
		send_con.send(pickle.dumps(to_send))

	elif tokens[0] == 'data':
		print 'Functionality not yet implemented...'
		pass

	elif tokens[0] == 'file':
		print 'Functionality not yet implemented...'
		pass


	## Wait to receive information
	print 'Waiting on response from the receiving robot'
	data_back = recv_con.recv(4096)

	return True