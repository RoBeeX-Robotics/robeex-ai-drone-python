import numpy as np
import cv2
from robeex_ai_drone_api import RobeexAIDrone
from cvzone.HandTrackingModule import HandDetector


REAL_TO_CV_SCALE = 100
OFFSET_X = 256
OFFSET_Y = 128

def to_real_pos(xc, yc):
    return (xc / REAL_TO_CV_SCALE, yc / REAL_TO_CV_SCALE)

def to_cv_pos(xm, ym):
    return (int(xm * REAL_TO_CV_SCALE), int(ym * REAL_TO_CV_SCALE))

IS_FLIGHT = True

def flight():
    # Create an image for visualization.
    img = np.ones((512, 512, 3), dtype=np.uint8) * 255
    w, h, _ = img.shape
    # Draw a vertical line to show the OFFSET_X
    img = cv2.line(img, (OFFSET_X, 0), (OFFSET_X, h), (0, 0, 255), 1)
    img = cv2.line(img, (0, h - OFFSET_Y), (w, h - OFFSET_Y), (0, 0, 255), 1)

    drone = RobeexAIDrone(drone_ip="172.168.1.128")

    if IS_FLIGHT:
        drone.rc.nav.disarm()
        print('connecting ... ')
        drone.wait_for_telemetry()
        print('done')
        drone.rc.nav.disarm()

        cv2.imshow(f"Y", img)
        drone.rc.rgb.set_full_color(100, 100, 100)

        if cv2.waitKey(0) != ord('a'):
            return
        drone.rc.rgb.set_full_color(200, 0, 0)
        drone.rc.nav.arm()
        if cv2.waitKey(0) != ord('t'):
            return
        drone.rc.rgb.set_full_color(0, 255, 0)
        drone.rc.nav.takeoff(0.5)

    drone.rc.rgb.set_full_color(0, 0, 200)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    hand_detector = HandDetector(detectionCon=0.8, maxHands=1)

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        hands, _  = hand_detector.findHands(frame, draw=False)
        if hands:
            hand = hands[0]
            wrist = hand['lmList'][0]  # The wrist is the first landmark in the list
            frame_height, frame_width, _ = frame.shape
            cv2.circle(frame, (wrist[0], wrist[1]), 5, (0, 0, 255), -1)
            wrist_percentage_y = 1 - (wrist[1] / frame_height)  # Calculate percentage of wrist position
            wrist_percentage_x = (wrist[0] / frame_width)  # Calculate percentage of wrist position
            # print("Wrist position:", wrist, "Wrist height percentage:", wrist_percentage_y)

            xm, ym = ((wrist_percentage_x - 0.5) * 2, wrist_percentage_y)

            xp, yp = to_cv_pos(xm,ym)

            img = np.ones((512, 512, 3), dtype=np.uint8) * 255
            cv2.circle(img, (OFFSET_X + xp,  h - yp - OFFSET_Y), 1, (100, 0, 100), -1)
            # print(xp,yp, '=>', xm, ym)
            
            drone_pos = (float(xm), 0, float(ym) + 0.5)
            print(drone_pos)
            if IS_FLIGHT:
                drone.rc.nav.set_position_3d(*drone_pos, wait_until_done=False)

        cv2.imshow(f"Y", img)

        cv2.imshow(f"frame", frame)
        k = cv2.waitKey(100) & 0xFF
        if k == ord('0'):
            drone.rc.nav.disarm()
            break
        if k == ord('q'):
            break

    if IS_FLIGHT:
        drone.rc.nav.land()
    while cv2.waitKey(0) != ord('q'):
        pass
    cv2.destroyAllWindows()

def main():
    flight()

if __name__ == "__main__":
    main()