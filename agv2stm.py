from enum import Enum
import can
import binascii
import os
#can.send veri gönderme hızı 15kHz = 0.066ms

MYSTDID_for_MotorLeft = 0x17
MYSTDID_for_MotorRight = 0x16
MYSTDID_for_Lift = 0x18
MotorLeft_STDID = 0x10
CAN_TIMEOUT = 0.1

id1= "017"
id2= "016"



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

        #self.bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=250000)



    def basamak(sayi):
        if sayi < 0:
            rslt = []
            sayi = str(sayi)
            rslt.append(sayi[1])
            rslt.append(sayi[3])
            rslt.append(sayi[4])
        else:
            rslt = []
            sayi = str(sayi)
            rslt.append(sayi[0])
            rslt.append(sayi[2])
            rslt.append(sayi[3])
        return rslt

    #dogruuuuu
    def send(self,data1, data2):
        digits1 = basamak(data1)
        digits2 = basamaklar(data2)

        print("{} {} {}".format(digits1[0],digits1[1],digits1[2])
        print("{} {} {}".format(digits2[0],digits2[1],digits2[2])

        if data1 < 0:
            s1 = "{}{}{}{}".format(1,digits1[0],digits1[1],digits1[2]) # 1 ise eksi
        else:
            s1 = "{}{}{}{}".format(0,digits1[0],digits1[1],digits1[2]) # 0 ise artı
        if data2 < 0:
            s2 = "{}{}{}{}".format(1,digits2[0],digits2[1],digits2[2]) # 1 ise eksi
        else:
            s2 = "{}{}{}{}".format(0,digits2[0],digits2[1],digits2[2]) # 0 ise artı
        
        os.system("cansend can0 {}#{}{}".format(id1,s1,s2))

        print("cansend can0 {}#{}{}".format(id1,s1,s2))

    # stm32'lerden ısı, akım, batarya ve lift durum bilgilerini okur
    def read2STM(self):
        msg = self.bus.recv(0.001)
        if msg is not None:
            print(msg)


    # yükü almak için lift sistemine CAN ile komut gönderir
    def setLiftUp(self):
        pass

    # yükü bırakmak için
    def setLiftDown(self):
        pass

    # motorlara double değerleri gönderen kod
    def motorWrite(self, motorLeft,motorRight):
        #message = can.Message(arbitration_id=MYSTDID_for_MotorLeft, data=bytes(str(motorLeft), 'utf-8'), is_extended_id=False)
        #self.bus.send(message, timeout= CAN_TIMEOUT)
        self.send(motorLeft, motorLeft)
        #self.send(id2, motorRight)


        #message = can.Message(arbitration_id=MYSTDID_for_MotorRight, data=bytes(str(motorRight), 'utf-8'), is_extended_id=False)
        #self.bus.send(message, timeout= CAN_TIMEOUT)

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



