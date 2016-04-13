import naoqi
from naoqi import ALProxy
import time

lirc = ALProxy("ALInfrared", "192.168.0.4", 9559)  # change IP with NAO IP

# lirc.sendIpAddress("127.0.0.1") # Send IP address
time.sleep(0.5)  # Delay necessary for a reliable transfer
num = 42
keyName = 'KEY_2'
i = 1
while i > 0:
    # lirc.send8(num) # Send the number 42
    #lirc.sendRemoteKey('Samsung_00008E', "KEY_1")
    lirc.sendRemoteKey("Samsung_00008E", 'KEY_1')
    print('send finshied for {}'.format(num))
    time.sleep(1.5)
    i = i - 1
# time.sleep(0.5)
# lirc.send32(0x42, 0x2A, 0x13, 0x0D) # Send four 8 bits numbers
# time.sleep(0.5)
# lirc.send32("36757575") # Send one 32 bits number
