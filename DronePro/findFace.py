import cv2
import numpy as np

# w, h = 0,0
list_of_area = [10000]
list_a = []
list_a.append(1000)


def findFace2fornow(faces):
    myFaceListC = []
    myFaceListArea = []
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 200), 2)
        # the center of the face
        cx = x + w // 2
        cy = y + h // 2
        # the area of the face
        area = w * h
        list_of_area.append(area)
        # point that indicate the center of the face
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)
    # if there are many faces so we chose the closest one it mean the bigger face
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]], list_of_area
    else:
        return img, [[0, 0], 0], list_of_area


# min_area = 0
# max_area = 0

def findFace(img):
    # global min_area, max_area
    def findProfileFace():
        faceCascade = cv2.CascadeClassifier("C:/Users/ozreich/GM7/DronePro/haarcascade_profileface.xml")
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces2 = faceCascade.detectMultiScale(imgGray, 1.2, 20)
        # print(faces)

        return findFace2fornow(faces2)

    # def findFrontalFace():
    #     faceCascade1 = cv2.CascadeClassifier("C:/Users/ozreich/GM7/DronePro/haarcascade_frontalface_default.xml")
    #     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     faces1 = faceCascade1.detectMultiScale(imgGray, 1.2, 20)
    #     # faces = np.append(faces2, faces1)
    #     return findFace2fornow(faces1)
    # findFrontalFace()
    return findProfileFace()


cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    img, info, list_a = findFace(img)
    min_a = min(list_a)
    max_a = max(list_a)
    print("Center", info[0], "Area", info[1], min_a, max_a)
    cv2.imshow("output", img)
    cv2.waitKey(1)
