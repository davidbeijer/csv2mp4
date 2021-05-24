import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import time

##inital time, to measure performance
start_time = time.time()

##read the data from a CSV file, and account for excel's bullshit ; separator
temps = pd.read_csv('dataCabine.csv', sep =";")


title = 'Temperatures'

##get the X and Y values from the pandas df
y = np.array(temps.loc[:, "Temp1":"Temp1"])
x = np.array(temps.loc[:, 'Sample':'Sample'])

##initialize the layout of the plots
fig, ax = plt.subplots()
plt.xlim(0, np.max(x))
plt.ylim(np.min(y), np.max(y))
plt.xlabel('time',fontsize=20)
plt.ylabel(title,fontsize=20)
plt.title('Measured temperature',fontsize=20)

##initialize the first data-line
line, = ax.plot(x, y, color='b', label='Temp1')

## what needs to update in the animation?
def animate(i):
    line.set_data(x[:i], y[:i])  

## make the animation    
ani = matplotlib.animation.FuncAnimation(fig, animate, interval=10, frames=len(x)-1)

##write the animation
ani.save('result.mp4', dpi=300)

#print how long it all took
print("--- %s seconds ---" % (time.time() - start_time))