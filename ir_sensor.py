import RPi.GPIO as g
import time
import servoctrl as s

g.cleanup()
g.setmode(g.BOARD)
g.setup(11,g.IN)

s.start_feeder()

# def ir_detected():
#     if !(g.input(11)):


try:
    while True:
        if g.input(11):
            
            # print("Not Detected")
            # s.opengate1()
            time.sleep(0.01)

        else:
            print(type(g.input(11)))
            if g.input(11) == 0:
                print("ok")
            # print("Ball passed through gate 1")
            s.closegate1()    
            s.opengate2()
            time.sleep(1.5)
            s.closegate2()

except KeyboardInterrupt:
    s.stop_feeder()
    g.cleanup()
    

