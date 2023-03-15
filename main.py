import time
import threading
from agv2stm import AGV2STM

agv = AGV2STM()

def canLoop():
    while True:
        agv.read2STM()
        
def loop():
    while True:
        print("ros")
        agv.motorWrite(5.345,7.567)
        time.sleep(1)

t1 = threading.Thread(target=canLoop)
t2 = threading.Thread(target=loop)
t1.start()
t2.start()


