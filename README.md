# Raspberry Pi LED Strip
*WS2812B LED Strip Raspberry Pi Setup and Example*

## Prerequisites
- Raspberry Pi (tested with models 3/B+ and 4/B+)
- WS2812B LED strip

## Hardware setup
- LED strip high to 5v pin on Pi (check pin layout using `pinout` command on the Pi)
- LED strip ground to GND pin on Pi
- LED strip data to GPIO18 pin on Pi


## Installation & setup
Disable output on GPIO18 pin: 
```shell
sudo nano /boot/config.txt
# Ensure the following value is off:
# dtparam=audio=off
```

```shell
# Create a project folder
mkdir led-strip
cd led-strip

# Install required python dependencies for addressing the LED strip using the raspberry's GPIO pins
sudo apt update

pip3 install flask
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel --break-system-packages
sudo python3 -m pip install --force-reinstall adafruit-blinka --break-system-packages

# Add the current user (pi) to the gpio group and reboot
sudo usermod -aG gpio $USER
sudo reboot
```

### Troubleshooting

In some cases `adafruit-blinka` installs the wrong GPIO module (Jetson error when starting server).
In such case, simply uninstall the Jetson GPIO package and re-run the server: 
```shell 
sudo pip3 uninstall Jetson.GPIO --break-system-packages
```

## Running manually

Start the server:
```shell
# Super user rights are required to access GPIO functionality
sudo python3 server.py
```


Switch on the LED strip:
> http://YOUR_RASPI_IP:8888/led-strip/on


Switch off the LED strip:
> http://YOUR_RASPI_IP:8888/led-strip/off


## Running automatically on system startup

Create a systemd service file
```shell
sudo nano /etc/systemd/system/led-strip.service
```

Paste the following content (adapt the path to your project files):
```
[Unit]
Description=LED Strip Control HTTP Server
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/led-strip/server.py
WorkingDirectory=/home/pi/led-strip
StandardOutput=inherit
StandardError=inherit
Restart=always

[Install]
WantedBy=multi-user.target
```

Reload systemd, enable and start the service: 
```shell
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable led-strip.service
sudo systemctl start led-strip.service
```

Confirm it's running:
```shell
sudo systemctl status led-strip.service
```

View logs:
```shell
journalctl -u led-strip.service -f
```
