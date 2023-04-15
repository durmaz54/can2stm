import can
import time
import os


a = 0

while True:
    time.sleep(1)
    txt = bytes(str(a), 'utf-8')
    print(txt)
    os.system("cansend can0 017#{}".format(txt))
    a+=0.3