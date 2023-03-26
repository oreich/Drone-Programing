"""
now this file got all the functionalities that he had to have (find faces and track them) .
the running of the find and track face occur in the main drone.
TODO add key board control to the main
TODO clean the code
TODO add the commends to takeoff etc to new python file
"""
import cv2
import numpy as np
from djitellopy import tello
# import findFace
# import KeyPressModule as kp
import time

# Parameters for pid controller
PROPORTIONAL = 0.8
INTEGRAL = 0.8
DERIVATIVE = 0

# Edges of the frame that indicate the distance
CLOSE = 4000
FAR = 20000

# the size of the frame
WIDTH = 360
HIGH = 240
list_of_area = [11000]

min_area = 0
max_area = 0
# kp.init()

# me = tello.Tello()
#
# me.connect()
#
# me.streamon()

# me.takeoff()

# me.send_rc_control(0, 0, 5, 0)

# time.sleep(1)
#

FRAME_RANGE = [FAR, CLOSE]  # the edges that indicates to us the distance

pid = [PROPORTIONAL, INTEGRAL, DERIVATIVE]  # i can fine-tune this parameters

# pError = 0  # previous error


#
# def getKeyboardInput():
#     lr, fb, ud, yv = 0, 0, 0, 0
#
#     speed = 100
#
#     if kp.getKey("LEFT"):
#         lr = -speed
#
#     elif kp.getKey("RIGHT"):
#         lr = speed
#
#     if kp.getKey("UP"):
#         fb = speed
#
#     elif kp.getKey("DOWN"):
#         fb = -speed
#
#     if kp.getKey("w"):
#         ud = speed
#
#     elif kp.getKey("s"):
#         ud = -speed
#
#     if kp.getKey("a"):
#         yv = -speed
#
#     elif kp.getKey("d"):
#         yv = speed
#
#     if kp.getKey("q"): me.land(); time.sleep(1)
#
#     if kp.getKey("e"):  me.takeoff()
#
#     if kp.getKey("z"):
#         cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
#
#         time.sleep(0.3)
#
#     return [lr, fb, ud, yv]
#

def findFace(img):
    faceCascade = cv2.CascadeClassifier("C:/Users/ozreich/GM7/DronePro/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convertung to grey scale
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
    myFaceListC = []  # list of faces if there are more then one face we will relate to the biggest face
    myFaceListArea = []
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # draw rectangle around the face
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

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]], list_of_area
    else:
        return img, [[0, 0], 0], list_of_area


def trackFace(info, w, pid, pError):
    area = info[1]
    x, y = info[0]
    fb = 0
    error = x - w // 2  # how far our object from the center
    speed = pid[0] * error + pid[1] * (error - pError)
    speed = int(np.clip(speed, -100, 100))
    if FRAME_RANGE[0] < area < FRAME_RANGE[1]:  # stay at its place
        fb = 0
    elif area > FRAME_RANGE[1]:  # if it to close go backword
        fb = 100
    elif area < FRAME_RANGE[0] and area != 0:  # if it to far go farword
        fb = -100
    # if we didnt ditact anything
    if x == 0:
        speed = 0
        error = 0
    print(speed, fb)
    # me.send_rc_control(0, fb, 0, speed)  # send the command to the drone
    return error

    # print(me.get_battery())
# cap = cv2.VideoCapture(1)

#
# while True:
#     _, img = cap.read()
#     # img = me.get_frame_read().frame
#     # img = cv2.resize(img, (WIDTH, HIGH))
#     img, info, list_a = findFace(img)
#     pError = trackFace(info, WIDTH, pid, pError)
#     # print("Center", info[0], "Area", info[1], min(list_a), max(list_a))
#     cv2.imshow("Output", img)
#     # vals = getKeyboardInput()
#     # me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
#     cv2.waitKey(1)
