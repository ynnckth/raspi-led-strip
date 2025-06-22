# LED Strip

## Installation & Setup

```shell
# Create a project folder
mkdir led-strip
cd led-strip

# Install required python dependencies for addressing the LED strip using the raspberry's GPIO pins
sudo apt update

sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel --break-system-packages
sudo python3 -m pip install --force-reinstall adafruit-blinka --break-system-packages
sudo pip3 uninstall Jetson.GPIO --break-system-packages

# Add the current user (pi) to the gpio group and reboot
sudo usermod -aG gpio $USER
sudo reboot
```

## Running the Server

Start the server:
```shell
python3 server.py
```

Switch on the LED strip:
> http://<ip>:8888/led-strip/on


Switch off the LED strip:
> http://<ip>:8888/led-strip/off

