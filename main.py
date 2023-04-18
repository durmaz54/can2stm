import can
import struct
import threading
import time
import numpy as np

bus = can.interface.Bus(bustype='socketcan', channel='can0')

#son
def send(m1,m2):
    global bus
    x1 = np.int32(m1 * 100)
    x2 = np.int32(m2 * 100)
    data1 = x1.tobytes()
    data2 = x2.tobytes()
    data = data1+data2
    print(data)
    msg = can.Message(arbitration_id=0x17, data=data)
    print("f1 = {} f2={}".format(str(m1),str(m2)))
    bus.send(msg)
    print(msg)
    

def canLoop():
    while True:
        agv.read2STM()
        
def loop():

    float1 = 0
    float2 = 0

    while True:
        float1 += 0.01
        float2 -= 0.01 
        send(float1,float2)
        time.sleep(1)

#t1 = threading.Thread(target=canLoop)
t2 = threading.Thread(target=loop)
#t1.start()
t2.start()

