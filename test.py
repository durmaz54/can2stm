import can
import time
import os
import binascii


a = 0
def send(data):
    x = str(data)
    if(len(x)<8):
        x = x + "0"*(8-len(x))
    elif (len(x)>8):
        x = x[0:8]
    x = bytes(str(x),'utf-8')
    x = binascii.hexlify(x)
    os.system("cansend can0 017#{}".format(str(x, 'utf-8')))


while True:
    time.sleep(1)
    send(a)
    a+=0.3

