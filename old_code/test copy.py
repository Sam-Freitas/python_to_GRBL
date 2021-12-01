import serial
import time
import argparse

BAUD_RATE = 115200


def remove_comment(string):
    if (string.find(';') == -1):
        return string
    else:
        return string[:string.index(';')]


def remove_eol_chars(string):
    # removed \n or traling spaces
    return string.strip()


def send_wake_up(ser):
    # Wake up
    # Hit enter a few times to wake the Printrbot
    ser.write(str.encode("\r\n\r\n"))
    time.sleep(2)   # Wait for Printrbot to initialize
    ser.flushInput()  # Flush startup text in serial input


def stream_gcode():
    # with contect opens file/connection and closes it if function(with) scope is left
    with open(args.file, "r") as file, serial.Serial(args.port, BAUD_RATE) as ser:
        send_wake_up(ser)
        for line in file:
            # cleaning up gcode from file
            gcode = remove_eol_chars(remove_comment(line))
            if gcode:  # checks if string is empty
                # print(f"Sending gcode: {gcode}")
                print("Sending gcode:" + str(gcode))
                # converts string to byte encoded string and append newline
                command = str.encode(line + '\n')
                ser.write(command)  # Send g-code
                grbl_out = ser.readline()  # Wait for response with carriage return
                print(f" : {grbl_out.strip().decode('utf-8')}")
                time.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This is a basic gcode sender. http://crcibernetica.com')
    parser.add_argument('-p', '--port', help='Input USB port', default= '/dev/tty.usbserial-A906L14X')
    parser.add_argument('-f', '--file', help='Gcode file name', default = 'grbl_test.gcode')
    args = parser.parse_args()
    ## show values ##
    print("USB Port: %s" % args.port)
    print("Gcode file: %s" % args.file)
    stream_gcode()