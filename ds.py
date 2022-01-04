import cv2,time
import numpy as np

cap = cv2.VideoCapture('/home/hrishi/FMS/ds/test_videos/WIN_20211129_18_59_34_Pro.mp4')
# 252   186
# 563   372
# 638   212
# 850   427
# 945   446
# 1234   613
def draw_rectangle(img,start_point,end_point,thickness=2,color = (152, 243, 186)):
    return cv2.rectangle(img, start_point, end_point, color, thickness)

def resize(im):
    im = cv2.resize(im,(52,52),interpolation=cv2.INTER_NEAREST)
    return im
count = 0
while(cap.isOpened()):
    count=count+1
    start_time = time.time()
    ret, frame = cap.read()

    if ret == True:
        if count==3:
            cv2.imwrite('vid_frame.jpg',frame)
        input = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        ball_1,ball_2,ball_3 = frame[186:372,252:563,:],frame[212:427,638:850,:],frame[446:613,945:1234,:]
        ball_1,ball_2,ball_3 = resize(ball_1),resize(ball_2),resize(ball_3)
        cv2.imwrite(f'/home/hrishi/FMS/ds/train_ds/sort_machine/{count}_1_ball_1.png',ball_1)
        cv2.imwrite(f'/home/hrishi/FMS/ds/train_ds/sort_machine/{count}_1_ball_2.png',ball_2)
        cv2.imwrite(f'/home/hrishi/FMS/ds/train_ds/sort_machine/{count}_1_ball_3.png',ball_3)
        cv2.imshow('Frame',frame)
        cv2.waitKey(10)
    else:
        break

cap.release()
cv2.destroyAllWindows



        
# frame = np.concatenate((ball_1,ball_2,ball_3),axis=1)

# frame = draw_rectangle(frame,(251,181),(559,370))
# frame = draw_rectangle(frame,(642,206),(841,355))
# frame = draw_rectangle(frame,(945,448),(1216,621))
