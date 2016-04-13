from naoqi import ALProxy
import time
# create proxy on ALMemory
NAO_IP = "192.168.0.6"
memProxy = ALProxy("ALMemory", NAO_IP, 9559)

keyName = "Device/SubDeviceList/IR/LIRC/Remote/Key/Sensor/Value/"
try:
    while True:
        # get data. Val can be int, float, list, string
        val = memProxy.getData(keyName)
        print('{} ::=> Value::{}'.format(keyName, val))
        time.sleep(1.5)
except Exception, e:
    print e
