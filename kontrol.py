import tty
import termios
import sys
from agv2stm import AGV2STM

agv = AGV2STM()


# Yön tuşlarına karşılık gelen karakterler
UP_ARROW = 'w'
DOWN_ARROW = 's'
RIGHT_ARROW = 'd'
LEFT_ARROW = 'a'

# Klavye girdilerini okuyan ve karakteri döndüren fonksiyon
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

x=0
y=0
# Sonsuz döngü içinde klavye girdilerini oku
while True:
    char = getch()
    if char == UP_ARROW:
        x+= 0.01
    elif char == DOWN_ARROW:
        x-= 0.01
    elif char == RIGHT_ARROW:
        y+=0.01
    elif char == LEFT_ARROW:
        y-=0.01
    elif char== 'q':
        agv.motorWrite(0.00,0.00)
        break
    else:
        print("hatali tuş")
    print("m1={} m2={}".format(str(x-y),str(x+y)))
    agv.motorWrite(x-y , x+y)
