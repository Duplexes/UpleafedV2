import time

from flask import Flask, request, render_template
import serial
import os
app = Flask(__name__)
global comport
comport = input("Enter COM port: ")
#os.system("lt -p 5000 -h http://localtunnel.me -s upleafed")

@app.errorhandler(404)
def page_not_found(e):
    return "Something broke. Good job.", 404


# Main index.html page
@app.route('/')
def index():
    return render_template('index.html')


arduino = serial.Serial(port=comport, baudrate=115200, timeout=.1)  # open serial port
print("Connection to arduino completed.")

@app.route('/api/leaf', methods=['GET', 'POST'])
def leaf_input():
    # Crackhead method of getting a form fill. I'm not sure if this is the best way to do this. I'm sure there is a
    # better way.
    leaf_id = request.args.get('leaf')  # get leaf id from url
    debug = False
    if debug:
        print(f"""===================================")
        Leaf ID: {leaf_id}
        ===================================""")
        return "Leaf ID: " + leaf_id
    else:
        print(f"Opening serial connection to {comport}")
        print("Connected to Arduino")

        # Enables different pins on the arduino depending on the leaf id over the given comport
        if int(leaf_id) == 1:
            arduino.write(bytes("1", 'utf-8'))
            print(f"Sent 1 to arduino on {comport} at baud rate 115200")
        elif int(leaf_id) == 2:
            arduino.write(bytes("2", 'utf-8'))
            print(f"Sent 2 to arduino on {comport} at baud rate 115200")
        elif int(leaf_id) == 3:
            arduino.write(bytes("3", 'utf-8'))
            print(f"Sent 3 to arduino on {comport} at baud rate 115200")
        elif int(leaf_id) == 4:
            arduino.write(bytes("4", 'utf-8'))
            print(f"Sent 4 to arduino on {comport} at baud rate 115200")
        elif int(leaf_id) == 5:
            arduino.write(bytes("5", 'utf-8'))
            print(f"Sent 5 to arduino on {comport} at baud rate 115200")
        else:
            return "Leaf not found"
        return render_template('submission.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
