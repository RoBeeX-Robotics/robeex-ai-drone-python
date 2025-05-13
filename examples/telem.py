import asyncio
from robeex_ai_drone_api import RobeexAIDrone

async def main():
    drone_ip = "172.168.1.128"  # Drone IP address
    drone = RobeexAIDrone(drone_ip=drone_ip)  # Default port is 8585

    print('wait for telm ...')
    await drone.wait_for_telemetry()
    print('connecting established !')

    try:
        while True:
            telemetry = await drone.rc.get_next_telemetry_update()
            print(f"Telemetry: {telemetry}")
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        drone.stop()

if __name__ == "__main__":
    asyncio.run(main())

