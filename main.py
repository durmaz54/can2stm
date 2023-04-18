import can
import struct
import threading
bus = can.interface.Bus(bustype='socketcan', channel='can0')

float1 = 3.14
float2 = 2.71

data = bytearray(struct.pack("ff", float1, float2))
msg = can.Message(arbitration_id=0x17, data=data)



def canLoop():
    while True:
        agv.read2STM()
        
def loop():
    while True:
        float1 += 0.01
        float2 += 0.02

        bus.send(msg)
        print(msg)
        time.sleep(1)

#t1 = threading.Thread(target=canLoop)
t2 = threading.Thread(target=loop)
#t1.start()
t2.start()


