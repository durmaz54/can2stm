import can
import time
import os


a = 0

while True:
    time.sleep(1)
    os.system("cansend can0 017#{}".format(byts(str(a))))
    a+=0.3