import tty
import termios
import sys

# Yön tuşlarına karşılık gelen karakterler
UP_ARROW = '\x1b[A'
DOWN_ARROW = '\x1b[B'
RIGHT_ARROW = '\x1b[C'
LEFT_ARROW = '\x1b[D'

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

# Sonsuz döngü içinde klavye girdilerini oku
while True:
    char = getch()
    if char == UP_ARROW:
        print("Yukarı yön tuşuna basıldı!")
    elif char == DOWN_ARROW:
        print("Aşağı yön tuşuna basıldı!")
    elif char == RIGHT_ARROW:
        print("Sağ yön tuşuna basıldı!")
    elif char == LEFT_ARROW:
        print("Sol yön tuşuna basıldı!")
    else:
        print(char)
