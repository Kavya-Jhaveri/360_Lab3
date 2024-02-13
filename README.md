# 360_Lab3
Lab 3: Assembling the robot and testing actuators

Due: Thursday, February 15, 2024, 11:59 PM
Objective: This practical session is designed to provide direct engagement with the robots. Students will assemble the robots, familiarize themselves with their key components, and learn how to control the actuators.

Part 0: Read the lab rules before accessing the lab.

Part 1: Assemble the robot

Follow the instructions to assemble the robot here. Do not install the propellers.
Take a picture of your robot and include it in the report.
Describe 5 ways to improve the design and include them in the report (how can the robot be assembled faster? How can the structure of the frame be improved? Alternative materials to use?).
Part 2: Install the robot firmware

Install Arduino IDE 2.3.0 on your computer.
Download BlimpSwarm into the Arduino/libraries folder.
In Arduino open the menu File->Examples->BlimpSwarm->RawBicopterFly.
Connect the ESP32 with PINs  to your computer, select the device XIAO_ESP32S3 and its port.
Click on Upload 
Click on serial, and copy the MAC address. Then, close the serial port.
Repeat the same process to install File->Examples->BlimpSwarm->BaseTranseiver in the ESP32 (without PINS). That is the ESP32 that will be connected to your computer.
Part 3: Control the actuators (servos and motors using the Joystick)



Connect the Joystick to the computer
Edit the Python file BlimpSwarm/swarmbase/RawBicopter.py
Update the ROBOT_MAC of your robot
Update the port of the ESP32 (same as the one in Arduino)
Run the file RawBicopter.py. Move the left vertical joystick. The LED in your ESP32 should turn on when you move the vertical joystick.
Modify the file RawBicopter.py to test two servos and two motors using the joystick. Describe your solution in the report.
The bicopter needs to fly, modify RawBicopter.py to control the bicopter. Describe how to control the two servos in the report. Put a balloon in your robot (ask TAs for a helium balloon) and install the propellers. Fly using your controller!! Take a picture of your robot flying and include it in your report.


Report: Write a report in the IEEE format that includes the required information in the steps above.

Upload a PDF with your report
Deadline: Thursday, February 15, 2024
Late submission policy: Max score is 0.7^d, where d is the number of days late.
