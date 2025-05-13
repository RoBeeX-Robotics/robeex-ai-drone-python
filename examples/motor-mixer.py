import asyncio
from robeex_ai_drone_api import RobeexAIDrone, RGBMode, MotorNumber
import math
import cv2  # OpenCV for HSV to RGB conversion
import numpy as np  # For array manipulation

drone_ip = "172.168.1.128"  # Drone IP address
# drone_ip = "192.168.1.60"  # Drone IP address
drone = RobeexAIDrone(drone_ip=drone_ip)  # Default port is 8585

def calc_mixer(t, r, p):
    z = [t + p + r, t + p - r,t - p - r, t - p + r]
    return tuple(map(lambda x: int(max(x, 0)), z))


async def main():
    print('wait for telm ...')
    await drone.wait_for_telemetry()
    print('connecting established !')

    while True:
        telm = await drone.rc.get_next_telemetry_update()
        # print(telm)
        r, p = 250 * (telm.roll / math.pi), 250 * (telm.pitch / math.pi)
        motors = ul, ur, dl, dr = calc_mixer(20, r, p)
        print(f"{ul} {ur}\n{dr} {dl}")

        for i, m in enumerate(motors):
            drone.rc.rgb.set_color_by_motor_number(m, 100 - m, 0, MotorNumber(i))
        # drone.rc.rgb.set_color_by_motor_number(ur, 100 - ur, 0, 1)
        # drone.rc.rgb.set_color_by_motor_number(ul, 100 - ul, 0, 2)
        # drone.rc.rgb.set_color_by_motor_number(dl, 100 - dl, 0, 3)
        # drone.rc.rgb.set_color_by_motor_number(dr, 100 - dr, 0, 4)
        # print(f"{r:7.2f} , {p:7.2f}")
        
    # await asyncio.sleep(0.1)  # Small delay to visualize the color change

if __name__ == "__main__":
    drone.safe_run_async_func(main())

