import numpy as np
import cv2
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
rec=cv2.createLBPHFaceRecognizer()
rec.load("trainer/trainer.yml")
def getProfile(id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "Select * from People where id=" + str(id)
    cursor=conn.execute(cmd)
    profile = None
    for row in cursor:
        profile=row
    conn.close()
    return profile

id=0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
while(True):
    ret, img = cam.read()
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray, 1.3, 5)
    for(x, y, h, w) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0),2)
        id, conf=rec.predict(gray[y:y+h,x:x+w])
        profile = getProfile(id)
        if profile!=None:
            cv2.cv.PutText(cv2.cv.fromarray(img),"Name:"+profile[1],(x,y+h),font,255)
            cv2.cv.PutText(cv2.cv.fromarray(img), "Age:"+str(profile[2]),(x,y+h+20),font,255)
            cv2.cv.PutText(cv2.cv.fromarray(img), "Gender:"+profile[3],(x,y+h+40),font,255)
            cv2.cv.PutText(cv2.cv.fromarray(img), "Criminal Records:"+profile[4],(x,y+h+60),font,255)
    cv2.imshow("Face", img)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
