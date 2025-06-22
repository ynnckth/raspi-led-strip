from flask import Flask
import led

app = Flask(__name__)

@app.route('/led-strip/rainbow/on', methods=['GET'])
def rainbow_on():
    led.start_rainbow()
    print("Rainbow switched ON")
    return "LED strip rainbow ON", 200

@app.route('/led-strip/red/on', methods=['GET'])
def red_on():
    led.start_red()
    print("Red pulse switched ON")
    return "LED strip red pulse ON", 200

@app.route('/led-strip/blue/on', methods=['GET'])
def red_on():
    led.start_blue()
    print("Blue pulse switched ON")
    return "LED strip blue pulse ON", 200

@app.route('/led-strip/off', methods=['GET'])
def red_off():
    led.stop()
    print("LED strip switched OFF")
    return "LED strip OFF", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
