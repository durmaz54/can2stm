import time
import threading
from agv2stm import AGV2STM
#18 nisan
agv = AGV2STM()

def canLoop():
    while True:
        agv.read2STM()
        
def loop():
    a=0.3
    b=0.3
    while True:
       # a+=0.01
        #b-= 0.02
        agv.motorWrite(a,b)
        print("data send")
        time.sleep(1)

#t1 = threading.Thread(target=canLoop)
t2 = threading.Thread(target=loop)
#t1.start()
t2.start()


