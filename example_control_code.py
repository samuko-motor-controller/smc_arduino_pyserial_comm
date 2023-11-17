from smc_arduino_pyserial_comm import SMCArduinoPyserialCommApi
import time


smc = SMCArduinoPyserialCommApi('/dev/ttyUSB0')


time.sleep(4)

angPosA=0.0
angPosB=0.0
angVelA=0.0
angVelB=0.0

lowTargetVel = 3.142 # in rad/sec
highTargetVel = -3.142 # in rad/sec

prevTime = None
sampleTime = 0.02

ctrlPrevTime = None
ctrlSampleTime = 10.0
sendHigh = True


smc.sendTargetVel(lowTargetVel, lowTargetVel) # targetA, targetB
sendHigh = True

prevTime = time.time()
ctrlPrevTime = time.time()
while True:
  if time.time() - ctrlPrevTime > ctrlSampleTime:
    if sendHigh:
      smc.sendTargetVel(highTargetVel, highTargetVel) # targetA, targetB
      sendHigh = False
    else:
      smc.sendTargetVel(lowTargetVel, lowTargetVel) # targetA, targetB
      sendHigh = True
    
    ctrlPrevTime = time.time()



  if time.time() - prevTime > sampleTime:
    try:
      angPosA, angPosB = smc.getMotorsPos() # returns angPosA, angPosB
      angVelA, angVelB = smc.getMotorsVel() # returns angVelA, angVelB
      print(f"motorA_readings: [{angPosA}, {angVelA}]")
      print(f"motorB_readings: [{angPosB}, {angVelB}]")
      print("")
    except:
      pass
    
    prevTime = time.time()
  # time.sleep(0.01)

