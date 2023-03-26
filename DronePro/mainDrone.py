import FaceTracking
import cv2

cap = cv2.VideoCapture(0)
# pError = 0


def main():
    pError = 0
    while True:
        _, img = cap.read()
        # img = me.get_frame_read().frame
        # img = cv2.resize(img, (WIDTH, HIGH))
        img, info, list_a = FaceTracking.findFace(img)
        pError = FaceTracking.trackFace(info, FaceTracking.WIDTH, FaceTracking.pid, pError)
        # print("Center", info[0], "Area", info[1], min(list_a), max(list_a))
        cv2.imshow("Output", img)
        # vals = getKeyboardInput()
        # me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
        cv2.waitKey(1)
        # _, img = cap.read()
        # img, info, list_a = findFace(img)
        # min_a = min(list_a)
        # max_a = max(list_a)
        # print("Center", info[0], "Area", info[1], min_a, max_a)
        # cv2.imshow("output", img)
        # cv2.waitKey(1)


if __name__ == '__main__':
    main()
