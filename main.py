import can
import struct
import threading
import time
import numpy as np

bus = can.interface.Bus(bustype='socketcan', channel='can0')


def send(m1,m2):
    global bus
    m1 = int(float1 * 100)
    m2 = int(float2 * 100)
    data1 = struct.pack("i",m1)
    data2 = struct.pack("i",m2)
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
        float1 += 0.1
        float2 -= 0.1 
        send(float1,float2)
        time.sleep(1)

#t1 = threading.Thread(target=canLoop)
t2 = threading.Thread(target=loop)
#t1.start()
t2.start()

