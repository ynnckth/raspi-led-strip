import time
import board
import neopixel
import threading
from enum import Enum, auto

pixel_pin = board.D18
num_pixels = 9
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

_running = False
_thread = None
_current_mode = None

class LedMode(Enum):
    RAINBOW = auto()
    RED = auto()


def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in {neopixel.RGB, neopixel.GRB} else (r, g, b, 0)

def rainbow_cycle(wait=0.001):
    global _running
    while _running:
        for j in range(255):
            if not _running:
                break
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(pixel_index & 255)
            pixels.show()
            time.sleep(wait)

def red_pulse(wait=0.01):
    global _running
    while _running:
        # Brighten up
        for intensity in range(20, 256, 5):
            if not _running:
                break
            pixels.fill((intensity, 0, 0))  # red channel only
            pixels.show()
            time.sleep(wait)
        # Dim down
        for intensity in range(255, 19, -5):
            if not _running:
                break
            pixels.fill((intensity, 0, 0))
            pixels.show()
            time.sleep(wait)

def _start_animation(mode: LedMode):
    global _running, _thread, _current_mode

    if _running:
        if _current_mode == mode:
            return  # same mode, already running — do nothing
        else:
            _stop_animation()  # stop current mode first

    _running = True
    _current_mode = mode

    if mode == LedMode.RAINBOW:
        target = rainbow_cycle
    elif mode == LedMode.RED:
        target = red_pulse
    else:
        return

    _thread = threading.Thread(target=target, daemon=True)
    _thread.start()


def _stop_animation():
    global _running, _current_mode
    _running = False
    _current_mode = None
    pixels.fill((0, 0, 0))
    pixels.show()


def start_rainbow():
    _start_animation(LedMode.RAINBOW)

def stop_rainbow():
    _stop_animation()

def start_red():
    _start_animation(LedMode.RED)

def stop_red():
    _stop_animation()
