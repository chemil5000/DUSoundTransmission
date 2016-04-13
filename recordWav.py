import socket
import sys
import struct
import time
import startRecordWavNao as strtrwn
import stopRecordWavNao as stprwn



strtrwn.startRecordWav()
time.sleep(10.0)
#@TODO have an end signal to stop recording
stprwn.stopRecordWav()