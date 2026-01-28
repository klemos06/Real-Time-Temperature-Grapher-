import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, time, math
import serial


ser = serial.Serial(
    port='COM5',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

xsize = 200 

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
    if t > -1:
        xdata.append(t)
        ydata.append(y)
        
        if y > 27.0:
            line.set_color('red')
            ax.set_title("\N{Face Screaming In Fear} WARNING: OVERHEATING! \N{Face Screaming In Fear}", color='red', fontsize=16)
        else:
            line.set_color('green')
            ax.set_title("Temperature: Normal", color='black')

        if t > xsize:
            ax.set_xlim(t - xsize, t)bn
        
        line.set_data(xdata, ydata)
    return line,

def on_close_figure(event):
    ser.close() 
    sys.exit(0)

# graph
data_gen.t = -1
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close_figure)
ax = fig.add_subplot(111)

# plot line
line, = ax.plot([], [], lw=2, color='red')

# axis(es?)
ax.set_ylim(0, 50) # range
ax.set_xlim(0, xsize)
ax.set_ylabel("Temperature (C)")
ax.set_title("Temperature")
ax.grid()

xdata, ydata = [], []


ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=1000, repeat=False)

plt.show()