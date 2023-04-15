import can
import time
import os


a = 0

while True:
    time.sleep(1)
    txt = bytes(str(a))
    os.system("cansend can0 017#{}".format(txt))
    a+=0.3