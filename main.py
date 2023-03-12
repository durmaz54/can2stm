from agv2stm import *


agv = AGV2STM()


agv.setLiftUp()

agv.setLed(LedStatus.inMotion)
agv.setBuzzer(50)

agv.taskStatWrite(60, 20, 'A')


if(agv.read2STM() == LiftStatus.error):
    print("okuma başarısız")
    

if(agv.liftStatus == LiftStatus.liftDown):
    print("lift kalkmadi")

if(agv.motorWrite(10.0000, 12.0000) == LiftStatus.error):
    print("gönderim başarısız")