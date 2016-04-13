'''
LocationPayload:
    int x; // SPL coord frame, mm
    int y; // SPL coord frame, mm

DataPayload:
    int fragmentOffset; // offset of current fragment relative to original message
                        // In the original message from communications tester
                        // fragmentOffset will be 0. In messages forwarded from R
                        // back to the communications tester, fragmentOffset may be non-zero.
    int numBytes; // number of bytes transmitted in this fragment
    byte data[]; // the array of bytes to be transmitted
                 // -- only the first numBytes values are used

'''
from subprocess import call
import os
import time

# configuration of global parameters
remote_name = 'Samsung_BN59-00599A_TV'
wait_time_between_send = 2


import logging

def send_start():
    final_cmd = 'irsend SEND_ONCE ' + remote_name + ' KEY_POWER'
    logging.debug('going to call {}'.format(final_cmd))
    os.system(final_cmd)
    time.sleep(wait_time_between_send)
def send_stop():
    final_cmd = 'irsend SEND_ONCE ' + remote_name + ' KEY_STOP'
    logging.debug('going to call {}'.format(final_cmd))
    os.system(final_cmd)
    time.sleep(wait_time_between_send)


def send_string(string_rep, send_as_one = False):
    """
    This functio sends the remote key using irsend
    irsend SEND_ONCE Samsung_BN59-00599A_TV KEY_1
    """
    command_prefix = 'irsend SEND_ONCE ' + remote_name + ' KEY_'
    #@TODO need to put a validation on string_rep
    if send_as_one:
        command_list = [string_rep] 
    else:
        command_list = [c for c in string_rep]
    for cmd in command_list:
        final_cmd = command_prefix + cmd
        logging.debug('going to call {}'.format(final_cmd))
        os.system(final_cmd)
        time.sleep(wait_time_between_send)
        #call([final_cmd])
    


    # start the communication via Ir
    # send 'KEY_POWER' then KEY_1 etc as per string representation
    # then send KEY_STOP to specify end of cummunication
    
