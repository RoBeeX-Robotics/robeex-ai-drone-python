import asyncio
from robeex_ai_drone_api import RobeexAIDrone
import math
import cv2  # OpenCV for HSV to RGB conversion
import numpy as np  # For array manipulation

# drone_ip = "192.168.1.60"  # Drone IP address
drone_ip = "172.168.1.128"  # Drone IP address
drone = RobeexAIDrone(drone_ip=drone_ip)  # Default port is 8585

async def flight():
    await drone.rc.nav.set_mode()
    await drone.rc.nav.arm()
    await asyncio.sleep(0.5)
    print('takeoff -- start')
    await drone.rc.nav.takeoff(1)
    print('takeoff -- done')
    await asyncio.sleep(1)
    print('landing -- start')
    await drone.rc.nav.land()
    print('landing -- done')
    await asyncio.sleep(1)
    await drone.rc.nav.disarm()

async def main():

    print('wait for telm ...')
    await drone.wait_for_telemetry()
    print('connecting established !')

    await flight();

if __name__ == "__main__":
    drone.safe_run_async_func(main())
    # asyncio.run(main())

