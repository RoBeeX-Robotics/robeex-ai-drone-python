from robeex_ai_drone_api import RobeexAIDrone, UDPVideoStream, FrameSize
import cv2

# Initialize the UDP video stream
drone = RobeexAIDrone(drone_ip="192.168.1.60")
stream = drone.VideoCapture()

# Open the stream with a specific frame size and JPEG quality
stream.open(frame_size=FrameSize.SIZE_480x320, jpeg_quality=50)

try:
    while stream.isOpened():
        success, frame = stream.read()
        if not success:
            print("Failed to read frame")
            continue

        # Display the frame
        fps = stream.get_fps()
        if fps:
            cv2.putText(frame, f"FPS: {fps:.1f}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("UDP Stream", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass

print('stopping')

# Release the stream
stream.release()
cv2.destroyAllWindows()
