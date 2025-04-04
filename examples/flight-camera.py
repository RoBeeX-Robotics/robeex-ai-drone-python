from robeex_ai_drone_api import RobeexAIDrone, UDPVideoStream, FrameSize
import cv2
import asyncio

# Initialize the UDP video stream
drone = RobeexAIDrone(drone_ip="172.168.1.128")
stream = drone.VideoCapture()

# Open the stream with a specific frame size and JPEG quality
stream.open(frame_size=FrameSize.SIZE_480x320, jpeg_quality=20)


async def main():
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

            key = cv2.waitKey(1) & 0xFF
            await asyncio.sleep(0.01)
            if key == ord('q'):
                # Exit on 'q' key press
                break
            if key != 0xFF:
                print('Pressed: ', chr(key), '=>', key)
            if key == ord('1'):
                drone.rc.rgb.set_full_color(200, 0, 0)
                asyncio.create_task(drone.rc.nav.disarm())
            if key == ord('2'):
                drone.rc.rgb.set_full_color(0, 250, 100)
                asyncio.create_task(drone.rc.nav.arm())
            if key == ord('9'):
                drone.rc.rgb.set_full_color(0, 200, 100)
                asyncio.create_task(drone.rc.nav.takeoff(0.5))
            if key == ord('0'):
                drone.rc.rgb.set_full_color(50, 0, 255)
                asyncio.create_task(drone.rc.nav.land())
            if key == ord('w'):
                drone.rc.rgb.set_full_color(0, 0, 0)
                drone.rc.rgb.set_color_by_motor_number(200, 0, 0, index=1)
                drone.rc.rgb.set_color_by_motor_number(200, 0, 0, index=2)
                # asyncio.create_task(drone.rc.nav.go_forward(0.1))
            if key == ord('s'):
                drone.rc.rgb.set_full_color(0, 0, 0)
                drone.rc.rgb.set_color_by_motor_number(200, 0, 0, index=3)
                drone.rc.rgb.set_color_by_motor_number(200, 0, 0, index=4)
                # asyncio.create_task(drone.rc.nav.go_forward(-0.1))
            if key == ord('d'):
                drone.rc.rgb.set_full_color(0, 0, 0)
                drone.rc.rgb.set_color_by_motor_number(200, 0, 0, index=1)
                drone.rc.rgb.set_color_by_motor_number(200, 0, 0, index=4)
                # asyncio.create_task(drone.rc.nav.go_right(0.1))
            if key == ord('a'):
                drone.rc.rgb.set_full_color(0, 0, 0)
                drone.rc.rgb.set_color_by_motor_number(200, 0, 0, index=2)
                drone.rc.rgb.set_color_by_motor_number(200, 0, 0, index=3)
                # asyncio.create_task(drone.rc.nav.go_right(-0.1))
                # break

    except KeyboardInterrupt:
        pass

asyncio.run(main())

print('stopping')

# Release the stream
stream.release()
cv2.destroyAllWindows()
