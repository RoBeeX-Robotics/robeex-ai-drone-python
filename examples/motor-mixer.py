from robeex_ai_drone_api import RobeexAIDrone, RGBMode, MotorNumber
import math
import numpy as np  # For array manipulation

drone_ip = "172.168.1.128"  # Drone IP address
# drone_ip = "192.168.1.60"  # Drone IP address
drone = RobeexAIDrone(drone_ip=drone_ip)  # Default port is 8585

def calc_mixer(t, r, p):
    z = [t + p - r, t + p + r,t - p + r, t - p - r]
    return tuple(map(lambda x: int(max(x, 0)), z))


def main():
    print('wait for telm ...')
    drone.wait_for_telemetry()
    print('connecting established !')

    while True:
        telm = drone.rc.get_next_telemetry_update()

        r, p = 250 * (telm.roll / math.pi), 250 * (telm.pitch / math.pi)
        motors = ul, ur, dl, dr = calc_mixer(20, r, p)

        print(f"UL: {ul:3.0f} UR: {ur:3.0f} DR: {dr:3.0f} DL: {dl:3.0f}")

        for i, m in enumerate(motors):
            drone.rc.rgb.set_color_by_motor_number(m, 100 - m, 0, MotorNumber(i + 1))

if __name__ == "__main__":
    main()

