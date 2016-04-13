import naoqi import ALProxy

 IP = "192.168.0.100"
    PORT = 9559
    
    print "running sound detector"

try:
    sd = ALProxy("ALSoundDetection", IP, PORT)
except Exception,e:
    print "Could not create proxy to ALSoundDetection"
    print "Error was: ",e
    sys.exit(1)


    print "start recording..."    
    aur.startMicrophonesRecording("/home/nao/Code/outTXModTest.wav")
    time.sleep(10.0)
    aur.stopMicrophonesRecording()
    print "Stop recording..."


