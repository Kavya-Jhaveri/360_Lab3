

from comm.Serial import SerialController
from joystick.JoystickManager import JoystickManager
import time

##### Insert your robot's MAC ADDRESS here ####
## (you can get it by running your arduino and looking at the serial monitor for your flying drone) ##
ROBOT_MAC = "34:85:18:91:49:C0" # "DC:54:75:D7:B3:E8" #use mac address of robots - esp32 once connected bioropter
#one on my mac is the one basetrancierver
#34:85:18:91:49:c0
#MAC: 48:27:e2:e6:e3:ac

### Insert your SERIAL PORT here ###
## may look like "COM5" in windows or "/dev/tty.usbmodem14301" in mac  #
## look in arduino for the port that your specific transeiver is connected to  ##
## Note: make sure that your serial monitor is OFF in arduino or else you will get "access is denied" error. ##
PORT = "/dev/cu.usbmodem11301"


# For debug purposes
PRINT_JOYSTICK = False


BaseStationAddress = "" # you do not need this, just make sure your DroneMacAddress is not your base station mac address



if __name__ == "__main__":
    # Communication
    serial = SerialController(PORT, timeout=.1)  # 5-second timeout
    serial.manage_peer("A", ROBOT_MAC)

    # Joystick
    joystick = JoystickManager()


    try:
        while True:
            # Axis input: [left_vert, left_horz, right_vert, right_horz, left_trigger, right_trigger]
            # Button inputs: [A, B, X, Y]
            axis, buttons = joystick.getJoystickInputs()


            if PRINT_JOYSTICK:
                print(" ".join(["{:.1f}".format(num) for num in axis]), buttons)

            #### CONTROL INPUTS to the robot here #########
            m1 = (axis[5] + 1) * 0.5  # Motor 1: a value between 0-1
            m2 = (axis[2] + 1) * 0.5  # Motor 2: a value between 0-1
            s1 = (axis[0] + 1) * 90.  # Servo 1: a value between 0-180
            s2 = (axis[0] + 1) * 90.  # Servo 2: a value between 0-180
            led = axis[0]
            ############# End CONTROL INPUTS ###############

            # Send through serial port
            serial.send_control_params(ROBOT_MAC, (m1, m2, s1, s2, led, 0, 0, 0, 0, 0, 0, 0, 0))
            time.sleep(.1)
            
    except KeyboardInterrupt:
        print("Stopping!")
        # Send zero input
        serial.send_control_params(ROBOT_MAC, (0, 0, 180, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0))
