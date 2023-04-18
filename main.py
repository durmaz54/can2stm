import can
import struct
import threading
import time

def send():
    pass



def canLoop():
    while True:
        agv.read2STM()
        
def loop():
    bus = can.interface.Bus(bustype='socketcan', channel='can0')

    float1 = 3.14
    float2 = 2.71

    a = int(float1 * 100)
    b = int(float2*100)
    data = bytearray(struct.pack("ii", a,b))
    msg = can.Message(arbitration_id=0x17, data=data)
    while True:
        float1 += 0.1
        float2 += 0.2 
        a = int(float1 * 100)
        b = int(float2*100)
        data = bytearray(struct.pack("ii", a,b))
        msg = can.Message(arbitration_id=0x17, data=data)
        bus.send(msg)
        print(msg)
        time.sleep(1)

#t1 = threading.Thread(target=canLoop)
t2 = threading.Thread(target=loop)
#t1.start()
t2.start()

