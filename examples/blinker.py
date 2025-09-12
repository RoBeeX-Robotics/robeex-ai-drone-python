from time import sleep
from robeex_ai_drone_api import RobeexAIDrone

def main():
    drone_ip = "172.168.1.128"  # Drone IP address
    drone = RobeexAIDrone(drone_ip=drone_ip)  # Default port is 8585

    print('wait for telm ...')
    drone.wait_for_telemetry()
    print('connecting established !')

    try:
        while True:
            telemetry = drone.rc.get_next_telemetry_update()
            print(f"Telemetry: {telemetry}")
            drone.rc.rgb.set_full_color(255, 0,0)
            sleep(1)
            drone.rc.rgb.set_full_color(0, 255,0)
            sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        drone.rc.stop()
        # drone.stop()

if __name__ == "__main__":
    main()

