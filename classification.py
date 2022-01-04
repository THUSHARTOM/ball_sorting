import cv2
from inference import inference
import servoctrl as sc
import RPi.GPIO as g
import time
import numpy as np
# cap = cv2.VideoCapture('WIN_20211129_18_59_07_Pro.mp4')
cap = cv2.VideoCapture(0)
count = 0
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)
thickness = 1
class_names = ['empty', 'orange', 'white']
print("Initializing...")
g.cleanup()
g.setmode(g.BOARD)
g.setup(11,g.IN)

def resize(im):
    im = cv2.resize(im,(52,52),interpolation=cv2.INTER_NEAREST)
    im = im[None,...]
    return im
def put_text(img,pos,class_name):
    print(type(class_name))
    img = cv2.putText(img,class_name, pos, font,fontScale, color, thickness, cv2.LINE_AA)
    return img
def draw_rectangle(img,start_point,end_point,thickness=2,color = (152, 243, 186)):
    return cv2.rectangle(img, start_point, end_point, color, thickness)

while(cap.isOpened()):
    sc.start_feeder()
    start_time = time.time()
    ret, frame = cap.read()
    print("Cap open")
    if ret == True:
        print("inside loop")
        input = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = draw_rectangle(frame,(938,424),(1238,598))
        # loc_1,loc_2,loc_3,loc_4 = input[196:286,232:358,:],input[185:294,476:649,:],input[210:359,736:900,:],input[386:493,977:1202,:]
        # loc_1,loc_2,loc_3,loc_4 = resize(loc_1),resize(loc_2),resize(loc_3),resize(loc_4)
        loc_1 = input[424:598,938:1238,:]
        loc_1 = resize(loc_1)
        input = loc_1
        # input = np.concatenate([loc_1,loc_2,loc_3,loc_4],axis=0)
        io_time = time.time()-start_time
        # print(f'Time for IO operations = {io_time}')
        final_pred = inference(input)
        # comm.sendValue(class_names[final_pred['class_id'][0]])
        ball_color= class_names[final_pred['class_id'][0]]
        frame = put_text(frame,(938,424),class_names[final_pred['class_id'][0]]+'_'+str(int(final_pred['score'][0])))
        print(ball_color)
        if ball_color == "orange":
            time.sleep(0.1)
            sc.opengate1()
            sc.closegate2()
            print("Opening Orange gate")
            while True:
                if g.input(11) == 0:
                    time.sleep(1.5)
                    sc.closegate1()
                    break
            
        elif ball_color == "white":
            time.sleep(0.1)
            sc.opengate2()
            sc.closegate1()
            
            print("Opening white gate")
            while True:
                if g.input(11) == 0:
                    time.sleep(2.5)
                    sc.closegate2()
                    break

        sc.closegate1()
        sc.closegate2()
        # frame = put_text(frame,(476,185),class_names[final_pred[1]])
        # frame = put_text(frame,(736,210),class_names[final_pred[2]])
        # frame = put_text(frame,(977,386),class_names[final_pred[3]])
        # print(f'FPS for Inference operation = {1/(time.time()-start_time)-io_time}')
        #cv2.imshow('Frame',frame)
        cv2.waitKey(1)
        
    else:
        break

sc.stop_feeder()
cap.release()
cv2.destroyAllWindows
