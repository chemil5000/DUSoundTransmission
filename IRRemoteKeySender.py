import naoqi
from naoqi import ALProxy
import time

NAO_IP = "192.168.0.102"
PORT = 9559
lirc = ALProxy("ALInfrared", NAO_IP, PORT)  # change IP with NAO IP

# lirc.sendIpAddress("127.0.0.1") # Send IP address
time.sleep(0.5)  # Delay necessary for a reliable transfer

motionProxy = ALProxy("ALMotion", NAO_IP, PORT)
postureProxy = ALProxy("ALRobotPosture", NAO_IP, PORT)

# Wake up robot
motionProxy.wakeUp()

# Send robot to Pose Init
postureProxy.goToPosture("Crouch", .5)

# Go to rest position
# motionProxy.rest()

# print motion state
print motionProxy.getSummary()

time.sleep(2)

num = 42
keyName2 = 'KEY_2'
keyName1 = 'KEY_1'

#keyName2 = 'KEY_POWER'
#keyName1 = 'KEY_HOME'


keyName = ''
toggle = 0
#remoteName = 'SAMSUNG_10340G-VCR'
#remoteName = 'Samsung_00008E'
#remoteName = '2wire'
remoteName = 'Samsung_BN59-00599A_TV'
while True:
    # lirc.send8(num) # Send the number 42
    # lirc.sendRemoteKey(, "KEY_1")
    if toggle == 0:
        lirc.sendRemoteKey(remoteName, keyName1)
        keyName = keyName1
        toggle = 1
    else:
        lirc.sendRemoteKey(remoteName, keyName2)
        toggle = 0
        keyName = keyName2
    print('send finshied for {}'.format(keyName))
    time.sleep(4)
# time.sleep(0.5)
# lirc.send32(0x42, 0x2A, 0x13, 0x0D) # Send four 8 bits numbers
# time.sleep(0.5)
# lirc.send32("36757575") # Send one 32 bits number
