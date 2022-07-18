from flask import Flask, request
import serial
import time

# from pc_connector import get_usb
app = Flask(__name__)
global comport
comport = input("Enter COM port: ")

@app.errorhandler(404)
def page_not_found(e):
    # 404 Handler. Remove in production to abid by shad values!!
    return "You fucked up. Good job.", 404


# Main index.html page
@app.route('/')
def index():
    return 'Hello World!'


@app.route('/api/leaf', methods=['GET', 'POST'])
def leaf_input():
    # Crackhead method of getting a form fill. I'm not sure if this is the best way to do this. I'm sure there is a
    # better way.
    leaf_id = request.args.get('leaf')  # get leaf id from url
    debug = True
    if debug == True:
        print(f"""===================================")
        Leaf ID: {leaf_id}
        ===================================""")
        return "Leaf ID: " + leaf_id
    else:
        print(f"Opening serial connection to {comport}")
        arduino = serial.Serial(port=comport, baudrate=115200, timeout=.1)  # open serial port
        print("Connected to Arduino")

        # Enables different pins on the arduino depending on the leaf id over the given comport
        if int(leaf_id) == 1:
            arduino.write(bytes("1", 'utf-8'))
            print(f"Sent 1 to arduino on {comport} at baudrate 115200")
        elif int(leaf_id) == 2:
            arduino.write(bytes("2", 'utf-8'))
            print(f"Sent 2 to arduino on {comport} at baudrate 115200")
        elif int(leaf_id) == 3:
            arduino.write(bytes("3", 'utf-8'))
            print(f"Sent 3 to arduino on {comport} at baudrate 115200")
        elif int(leaf_id) == 4:
            arduino.write(bytes("4", 'utf-8'))
            print(f"Sent 4 to arduino on {comport} at baudrate 115200")
        elif int(leaf_id) == 5:
            arduino.write(bytes("5", 'utf-8'))
            print(f"Sent 5 to arduino on {comport} at baudrate 115200")
        else:
            return "Leaf not found"


if __name__ == '__main__':
    app.run()
