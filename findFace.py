import cv2
import numpy as np

# w, h = 0,0


def findFace(img):
    faceCascade = cv2.CascadeClassifier("C:/Users/ozreich/GM7/Resources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 20)
    print(faces)

    myFaceListC = []
    myFaceListArea = []
    for (x, y, w, h) in faces:
        print(w,h)
        cv2.rectangle(img, (x, y ), (x + w, y + h), (0, 0, 200), 2)
        # the center of the face
        cx = x + w // 2

        cy = y + h // 2
        # the area of the face
        print(w,h)
        area = w * h
        # point that indicate the center of the face
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

        myFaceListC.append([cx, cy])

        myFaceListArea.append(area)
# if there are many faces so we chose the closest one it mean the bigger face
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))

        return img, [myFaceListC[i], myFaceListArea[i]]
    else:

        return img, [[0, 0], 0]


cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    img, info = findFace(img)
    print("Center", info[0], "Area", info[1])
    # findFace(img)
    cv2.imshow("output", img)
    cv2.waitKey(1)
