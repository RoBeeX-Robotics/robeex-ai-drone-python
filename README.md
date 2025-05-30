<p align="center">
  <a href="https://robeex.com/" target="blank"><img src="https://robeex.com/favicon.svg" width="200" alt="Nest Logo" /></a>
</p>

<p  style="font-size:2em;font-weight: 900" align="center">RoBeeX AI Drone Python API</p>


The **RoBeeX AI Drone Python API** is a Python library designed to control and interact with RoBeeX AI Drones. It provides features for navigation, RGB LED control, video streaming, and telemetry data retrieval.  

## Project Structure  

```plaintext  
robeex-ai-drone-python/  
├── examples/  
│   ├── flight-path/  
│   │   ├── flight.py  
│   │   ├── generate-circle.py  
│   │   ├── generate-text-cords.py  
│   ├── camera_stream.py  
│   ├── hand-detection.py  
│   ├── rgb.py  
│   ├── rgb-to-hue.py  
│   ├── telem.py  
│   └── test-flight.py  
├── src/  
│   └── robeex_ai_drone_api
```  

## Features  

- **Navigation API**: Control drone movement, takeoff, landing, and position setting.  
- **RGB LED API**: Customize LED colors and brightness for individual motors or all LEDs.  
- **Video Streaming**: Stream live video from the drone's camera using UDP.  
- **Telemetry**: Retrieve real-time telemetry data such as position, altitude, battery status, and more.  

## Installation  

1. Clone the repository:  
    ```bash  
    git clone https://github.com/RoBeeX-Robotics/robeex-ai-drone-python.git  
    cd robeex-ai-drone-python  
    ```  

2. Install dependencies using Poetry:  
    ```bash  
    pip install .
    ```  

## Usage  

### Example: Basic Flight  

```python  
from robeex_ai_drone_api import RobeexAIDrone  
import asyncio  

async def main():  
     drone = RobeexAIDrone(drone_ip="172.168.1.128")  
     await drone.wait_for_telemetry()  
     await drone.rc.nav.arm()  
     await drone.rc.nav.takeoff(1.0)  
     await asyncio.sleep(5)  
     await drone.rc.nav.land()  
     await drone.rc.nav.disarm()  

if __name__ == "__main__":  
     asyncio.run(main())  
```  

### Example: RGB LED Control  

```python  
from robeex_ai_drone_api import RobeexAIDrone  

drone = RobeexAIDrone(drone_ip="172.168.1.128")  
drone.rc.rgb.set_full_color(255, 0, 0)  # Set all LEDs to red  
```  
### More Examples  

Explore additional examples in the [`examples/`](./examples/) directory to learn more about the capabilities of the API.  

## License  

This project is licensed under the MIT License.  

## Authors  

- **RoBeeX Robotics** - [robeex.robotics@gmail.com](mailto:robeex.robotics@gmail.com)  

## Contributing  

Contributions are welcome! Feel free to submit issues or pull requests.  
