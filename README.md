
# smc_arduino_pyserial_comm
This is a child project of the Samuko Motor Control (SMC) project. This library can be used in your python robotic project to communicate with the **smc_driver module** in order to send target angular velocities to the motors or receive the motor's angular velocity and angular position, after successful velocity PID setup with the [**smc_app**](https://github.com/samuko-things/EMC2_gui_application).

> you can use it in your microcomputer robotics project (e.g Raspberry Pi, Nvida, PC, etc.)

A simple way to get started is simply to try out and follow the example code


## Dependencies
- you'll need to pip install the pyserial library
  > pip3 install pyserial


## How to Use the Library
- Ensure you have the smc_driver module shield with a preffered arduino board of your choice (NANO or UNO) fully set up for velocity PID control.

- Download (by clicking on the green Code button above) or clone the repo into your PC

- A simple way to get started is simply to try out and follow the example code

- copy the **smc_arduino_pyserial_comm.py** file into your python robotics project, import the library as shown in the example code, add it to your code, and start using it.

- you can also just clone the repo and try out the example code, then use it in your project follwing the example code.


## Basic Library functions and usage

- connect to smc_driver shield module
  > SMCArduinoPyserialCommApi("port_name or port_path")

- send target angular velocity command
  > sendTargetVel(motorATargetVel, motorBTargetVel)

- read motors angular position
  > getMotorsPos() # returns angPosA, angPosB

- read motors angular velocity
  > getMotorsVel() # returns angVelA, angVelB