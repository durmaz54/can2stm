from enum import Enum
import can


class LiftStatus(Enum):
    liftUp = 1
    liftDown = 0
    error = -1

class LedStatus(Enum):
    inMotion = 2
    inLift = 3
    taskFinish = 4
    onHold = 5
    error = -1


class AGV2STM():
    def __init__(self):
        self.liftStatus = LiftStatus.liftDown

        self.temp1 = None
        self.temp2 = None
        self.temp3 = None

        self.motorRightCurrent = None
        self.motorLeftCurrent = None
        self.motorLiftCurrent = None
        self.battery = 0 # %0 lion= 2.7V  --- %100 lion=4.2V

        self.bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=250000)  

    # stm32'lerden ısı, akım, batarya ve lift durum bilgilerini okur
    def read2STM(self):
        pass

    # yükü almak için lift sistemine CAN ile komut gönderir
    def setLiftUp(self):
        pass

    # yükü bırakmak için
    def setLiftDown(self):
        pass

    # motorlara double değerleri gönderen kod
    def motorWrite(self, motorLeft,motorRight):
        message = can.Message(arbitration_id=0x17, data=bytes(str(motorLeft), 'utf-8'), is_extended_id=False)
        self.bus.send(message, timeout= 0.0001)
    # buzzer sesi %volume
    def setBuzzer(self, volume: int):
        if(volume > 100):
            volume = 100
        elif (volume <0):
            volume = 0



    def setLed(self, stat: LedStatus):
        if(stat == LedStatus.inMotion):
            print("led hareket halinde durumuna ayarlandı")

    
    # Nextion ekrana gidecek olan görev bilgileri
    # taskStatWrite(600, 70, "A",) -> 600 saniye, %70 görev tamamlanması, 'A' bölgesine gidiyor,
    def taskStatWrite(self, startSecond: int, taskPerc : int, task: str):
        pass

