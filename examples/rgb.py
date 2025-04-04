import asyncio
from robeex_ai_drone_api import RobeexAIDrone
import math

async def main():
    drone_ip = "192.168.1.60"  # Drone IP address
    drone = RobeexAIDrone(drone_ip=drone_ip)  # Default port is 8585

    print('wait for telm ...')
    await drone.wait_for_telemetry()
    print('connecting established !')

    try:
        while True:
            telemetry = await drone.rc.get_next_telemetry_update()
            pg = (telemetry.pitch/(math.pi/2))
            if pg > 0:
                drone.rc.rgb.set_full_color(255 * pg , (1 - pg) * 255, 0)
            print(f"Telemetry: {telemetry.pitch} => {pg}")
    except Exception as e:
        print(e)
        print("Stopping...")

if __name__ == "__main__":
    asyncio.run(main())

