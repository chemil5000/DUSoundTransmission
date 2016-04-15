import sys
import time
from naoqi import ALProxy

input = sys.argv[1]
#record wav sound
IP = 'localhost'
PORT = 9559

print "running"

try:
    aur = ALProxy('ALAudioDevice', IP, PORT)
    print "ok audio dev"
except Exception,e:
    print "Could not create proxy to ALAudioDevice"
    print "Error was: ",e
    sys.exit(1)

aur.startMicrophonesRecording('/home/nao/AudioTransm/' + input)
print "started recording..."    
time.sleep(5)
aur.stopMicrophonesRecording()
print "Stop recording..."
