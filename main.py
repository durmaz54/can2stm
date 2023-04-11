import time
import threading
from agv2stm import AGV2STM


agv = AGV2STM()

def canLoop():
    while False:
        agv.read2STM()
        
def loop():
    a=0
    while True:
        a+=0.1
        try:
            agv.motorWrite(a,a)
            print("data send")
        except:
            print("Hata")
        time.sleep(1)

#t1 = threading.Thread(target=canLoop)
t2 = threading.Thread(target=loop)
#t1.start()
t2.start()


