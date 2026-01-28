# Real-Time Temperature Monitoring System
A high-precision temperature sensing and visualization system. This project utilizes a Nuveton N76E003 microcontroller to sample environment temperature via assembly, which is then processed and graphed in real-time via a Python-based dashboard.

# Features
**Hardware Interaction**
 Displays current temperature readings directly on a breadboard-mounted LCD for immediate monitoring.

Utilizing LM4040 external voltage reference to calibrate/adjust data from the LM335 sensor.

Simultaneously sends data to a physical LCD and a serial interface if desired (PuTTY).

** Data Visualization & Monitoring**
Python backend scripts the incoming serial data to generate a Temperature vs. Time plot.

 Data printing to the PuTTY terminal for raw temperature monitoring and debugging.

 Built-in automated threshold alert that triggers an "OVERHEATING" warning once the temperature exceeds 27°C (can be modified for specific application).

# Tech Stack
**Language & Firmware**
8051 Assembly: Bare-metal firmware for sensor interfacing, timing loops, serial communication, and LCD control.

Python: Used for serial communication (PySerial) and real-time data plotting (Matplotlib/FuncAnimation).

**Hardware & I/O**
8051 Microcontroller: The central processing unit for hardware logic.

Temperature Sensor (LM335): Digital thermal sensor.

LCD: Physical display for real-time, local monitoring.

# Why I Built This
I built this project to strengthen my understanding of:

Assembly Language: Managing registers, memory pointers, and utilizing the stack for serial communication.

Serial Communication: Implementing UART to connect embedded hardware and firmware.

Scripting In Python: Utilizing scripts to run embedded processes and develop multiple layers to a system - my first time.

# Future Improvements
Logging Important Data: Logging peak or low temperatures in a chosen time frame.

Active Cooling: Interfacing a fan that cools the temperature sensor when it reaches a certain temperature.

Auditory Alert: Connecting a speaker/buzzer to alert when a temperature is reached. 

# How to Run Locally
**You will need a compiler for 8051 assembly that can flash to the N76E003 - CrossIDE is preferred**

Python with with pyserial, matplotlib, and numbpy libraries installed

A serial terminal - PuTTY works well with CrossIDE

# Setup  

**Printing to Terminal**

1. Configure your serial terminal software in the IDE - use CTRL + T in CrossIDE.

2. Open the .asm file in your IDE - **must download the math32 library**.

3. Build and flash the .asm file onto your N76E003.

**Creating graph and real-time logging with Python**

1. Open Command Prompt 

2. Type in the following : python TemperatureScript.py

# Contact
If you're a recruiter, developer, or are generally interested in this project, feel free to reach out via LinkedIn or email (listed on my GitHub profile).
