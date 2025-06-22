import time
import board
import neopixel
import threading

# NeoPixels must be connected to D10, D12, D18 or D21 to work
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 9

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

_running = False
_thread = None

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
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

def start_rainbow():
    global _running, _thread
    if _running:
        return  # already running
    _running = True
    _thread = threading.Thread(target=rainbow_cycle, daemon=True)
    _thread.start()


def stop_rainbow():
    global _running
    _running = False
    pixels.fill((0, 0, 0))
    pixels.show()
