import cv2
import pickle
import numpy as np 


widht = 40
height = 20



def checkParkSpace(imgg) :
    spaceCounter = 0


    for pos in posList :
        x,y = pos

        imgCrop = imgg[y:y+height , x:x+widht] 
        count = cv2.countNonZero(imgCrop)

        

        if count < 165 :
            color = (0,255,0)
            thickness = 2 
            spaceCounter +=1
        
        else :
            color = (0,0,255)
            thickness = 2
        
        print(count)

        cv2.rectangle(img,pos,(pos[0] + widht ,pos[1] + height),color,thickness)
    cv2.putText(img,f"Free : {spaceCounter}/ {len(posList)}",(30,30),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,255),2)
cap = cv2.VideoCapture("video.mp4")


with open("CarParkPos","rb") as f :
    posList = pickle.load(f)

while True :

    success, img = cap.read()
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold,5)
    imgDilate = cv2.dilate(imgMedian,np.ones((3,3),dtype=np.uint8),iterations=1)







    checkParkSpace(imgDilate)
    """cv2.imshow("Median",imgMedian)
    cv2.waitKey(175)
    cv2.imshow("Dialte",imgDilate)"""

    cv2.imshow("Img",img)
    if cv2.waitKey(175) & 0xFF == ord("q") :
        break 