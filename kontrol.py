import msvcrt

while True:
    # Sonsuz döngüde yön tuşlarını okuyan ve işlem yapan kod
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'q':
            break
        elif key == b'H':
            print("Yukarı yön tuşuna basıldı.")
        elif key == b'P':
            print("Aşağı yön tuşuna basıldı.")
        elif key == b'M':
            print("Sağ yön tuşuna basıldı.")
        elif key == b'K':
            print("Sol yön tuşuna basıldı.")
        else:
            print("Geçersiz tuşa basıldı.")
