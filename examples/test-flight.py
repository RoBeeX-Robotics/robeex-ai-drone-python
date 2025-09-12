from time import sleep
from robeex_ai_drone_api import RobeexAIDrone

drone_ip = "172.168.1.128"  # Drone IP address
drone = RobeexAIDrone(drone_ip=drone_ip, debug=True)  # Default port is 8585

def flight():
    drone.rc.nav.set_mode()
    drone.rc.nav.arm()
    sleep(0.5)
    print('takeoff -- start')
    drone.rc.nav.takeoff(1)
    print('takeoff -- done')
    sleep(1)
    print('landing -- start')
    drone.rc.nav.land()
    print('landing -- done')
    sleep(1)
    drone.rc.nav.disarm()

def main():
    print('wait for telm ...')
    drone.wait_for_telemetry()
    print('connecting established !')

    flight();

if __name__ == "__main__":
    main()

