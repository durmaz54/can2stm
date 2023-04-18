import can
import struct
import threading
import time
import numpy as np

def send():

    pass



def canLoop():
    while True:
        agv.read2STM()
        
def loop():
    bus = can.interface.Bus(bustype='socketcan', channel='can0')

    float1 = -1.09
    float2 = -1.15

    while True:
        float1 += 0.1
        float2 += 0.2 
        a = int(float1 * 100)
        b = int(float2 * 100)
        data1 = struct.pack(">i",a)
        data2 = struct.pack(">i",b)
        data = a+b
        print(data)
        msg = can.Message(arbitration_id=0x17, data=data)
        print("f1 = {} f2={}".format(str(a),str(b)))
        bus.send(msg)
        print(msg)
        time.sleep(1)

#t1 = threading.Thread(target=canLoop)
t2 = threading.Thread(target=loop)
#t1.start()
t2.start()

