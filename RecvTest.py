import socket
import time
import struct
from thread import start_new_thread 
import logging
import RXModTest as rxls
import startRecordWavNao as strtrwn
import stopRecordWavNao as stprwn
import recordWavNao as rcw

#while True:
rcw.recordWav(5) 
data = rxls.rxDecode("outRecX.wav")
    #@TODO send data to master
print "IN", data
