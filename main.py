from agv2stm import *
import time

agv = AGV2STM()

for i in range(0,10):
    agv.motorWrite(0.5,0.5) # motorlara 0.5 değerini gönderir