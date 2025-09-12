from robeex_ai_drone_api import RobeexAIDrone, FrameSize
import cv2

drone = RobeexAIDrone()
stream = drone.VideoCapture()

# stream.open(frame_size=FrameSize.SIZE_640x480, jpeg_quality=45)
stream.open(frame_size=FrameSize.SIZE_320x240, jpeg_quality=5)

while stream.isOpened():
    success, frame = stream.read()
    if not success:
        print('bad image')
        continue

    cv2.imshow('RoBeeX Feed', frame)
    if cv2.waitKey(1) == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()

