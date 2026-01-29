import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, serial, csv

log_file = "temp_data.csv"
ser = serial.Serial(port='COM5', baudrate=115200, timeout=1)
xsize = 200 

with open(log_file, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Seconds", "Temperature_C"])

def data_gen():
    t = data_gen.t
    while True:
        t += 1
        try:
            strin = ser.readline()
            decoded_line = strin.decode('utf-8').strip()
            if decoded_line:
                val = float(decoded_line)
                yield t, val
        except ValueError:
            continue

def run(data):
    t, y = data
    xdata.append(t)
    ydata.append(y)

    with open(log_file, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([t, y])
    
    
    if y > 27.0:
        line.set_color('red')
        ax.set_title("⚠️ OVERHEATING!⚠️", color='red')
    else:
        line.set_color('green')
        ax.set_title(f"Current Temperature: {y} C")

    if t > xsize:
        ax.set_xlim(t - xsize, t)
    
    line.set_data(xdata, ydata)
    return line,

data_gen.t = -1
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(0, 50)
ax.set_xlim(0, xsize)
ax.grid()

xdata, ydata = [], []

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=1000)
plt.show()
