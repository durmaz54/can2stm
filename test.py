import can
import time
import os
"""""
bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=250000)
motorLeft = 0
while True:
    time.sleep(1)
    motorLeft+=0.1
    message = can.Message(arbitration_id=0x17, data=bytes(str(motorLeft), 'utf-8'), is_extended_id=False)
    bus.send(message, timeout= 0.1)
    print("------------------------")
    print(motorLeft)""""

a = 0

while True:
    time.sleep(1)
    os.system("cansend can0 017#{}".format(str(1234)))