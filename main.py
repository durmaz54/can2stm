import can
import struct
import threading
import time
import numpy as np
import binascii
bus = can.interface.Bus(bustype='socketcan', channel='can0')

#son
def send(m1,m2):
    global bus

    x = struct.pack('>f',m1)
    print(x)
    data = x+x
    print(data)
    with can.interface.Bus(bustype='socketcan', channel='can0', bitrate=250000) as bus2:
        msg = can.Message(arbitration_id=0x17, data=data, is_extended_id=False)
        bus2.send(msg)
        print(msg)

    

def canLoop():
    while True:
        agv.read2STM()
        
def loop():

    float1 = 0
    float2 = 0

    while True:
        float1 -= 0.01
        float2 -= 0.01 
        send(float1,float2)
        time.sleep(0.1)

#t1 = threading.Thread(target=canLoop)
t2 = threading.Thread(target=loop)
#t1.start()
t2.start()

