import can
import time

bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=250000)

while True:
    time.sleep(1)
    message = can.Message(arbitration_id=0x17, data=bytes(str(motorLeft), 'utf-8'), is_extended_id=False)
    bus.send(message, timeout= 0.1)
