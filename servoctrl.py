from adafruit_servokit import ServoKit
import time
mykit = ServoKit(channels=16)

# while True:
#     mykit.servo[0].angle=90
#     time.sleep(1)
#     mykit.servo[0].angle=0
#     time.sleep(1)

def start_feeder():
    print("Started feeding")
    mykit.servo[6].angle=0 
    
def stop_feeder():
    print("Feeding stopped")
    mykit.servo[6].angle=95 

def opengate1():
    print("Gate 1 opened")
    mykit.servo[0].angle=170
    mykit.servo[1].angle=10
def closegate1():
    print("Gate 2 closed")
    mykit.servo[0].angle=0
    mykit.servo[1].angle=180    


def opengate2():
    print("Gate 2 opened")
    mykit.servo[4].angle=180
    mykit.servo[3].angle=0

def closegate2():
    print("Gate 2 closed")
    mykit.servo[4].angle=0
    mykit.servo[3].angle=180  

# while True:
#     opengate1()
#     time.sleep(1)
#     closegate1()
#     time.sleep(1)

# start_feeder()
# time.sleep(2)

# opengate1()

# time.sleep(3)

# closegate1()

# opengate2()

# time.sleep(3)

# closegate2()

# time.sleep(1)

stop_feeder()
