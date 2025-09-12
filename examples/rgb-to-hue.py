from time import sleep
from robeex_ai_drone_api import RobeexAIDrone, RGBMode
import numpy as np  # For array manipulation
import cv2
from robeex_ai_drone_api.rgb_led_api import MotorNumber

drone_ip = "172.168.1.128"  # Drone IP address
# drone_ip = "192.168.1.60"  # Drone IP address
drone = RobeexAIDrone(drone_ip=drone_ip)  # Default port is 8585

def set_color_by_hue(hue: int, index: int):
    hsv_color = np.uint8([[[hue, 255, 255]]])  # Full saturation and value
    rgb_color = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2RGB)[0][0]
    drone.rc.rgb.set_color_by_motor_number(int(rgb_color[0]), int(rgb_color[1]), int(rgb_color[2]), MotorNumber(index))
    print(f"Index: {index} | Hue: {hue} => RGB: {rgb_color}")

def main():
    print('wait for telm ...')
    drone.wait_for_telemetry()
    print('connecting established !')

    for hue in range(10):  # OpenCV uses 0-179 for hue
        for hue in range(0, 180):  # OpenCV uses 0-179 for hue
            for i in range(0, 4):  # OpenCV uses 0-179 for hue
                set_color_by_hue((hue + (i * 45)) % 180, i + 1)
            # set_color_by_hue((hue + 45) % 180, 2)
            sleep(0.01)  # Small delay to visualize the color change

if __name__ == "__main__":
    main()

