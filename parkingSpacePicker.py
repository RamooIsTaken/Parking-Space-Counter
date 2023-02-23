import cv2
import pickle




widht = 40
height = 20

try :
    with open("CarParkPos","rb") as f :
        posList = pickle.load(f)
except :
    posList = []

def mouseClick(events,x,y,flags,params) :

    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))

    if events == cv2.EVENT_RBUTTONDOWN:
        for i ,pos in enumerate(posList) :
            x1,y1 = pos
            if x1<x<x1+widht and y1<y<y1+50 :
                posList.pop(i)
    
    with open("CarParkPos","wb") as f :
        pickle.dump(posList,f)


while True :

    img = cv2.imread("first_frame.png")
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0] + widht ,pos[1] + height),(255,0,0),2)




    cv2.imshow("İmg",img)
    cv2.setMouseCallback("İmg",mouseClick)
    if cv2.waitKey(1) & 0xFF == ord("q") :
        break 