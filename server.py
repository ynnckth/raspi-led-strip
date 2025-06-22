from flask import Flask
import led

app = Flask(__name__)

@app.route('/led-strip/rainbow/on', methods=['GET'])
def rainbow_on():
    led.start_rainbow()
    print("Rainbow switched ON")
    return "LED strip rainbow ON", 200

@app.route('/led-strip/rainbow/off', methods=['GET'])
def led_off():
    led.stop_rainbow()
    print("Rainbow switched OFF")
    return "LED strip rainbow OFF", 200

@app.route('/led-strip/red/on', methods=['GET'])
def red_on():
    led.start_red()
    print("Red pulse switched ON")
    return "LED strip red pulse ON", 200

@app.route('/led-strip/red/off', methods=['GET'])
def red_off():
    led.stop_red()
    print("Red pulse switched OFF")
    return "LED strip red pulse OFF", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
