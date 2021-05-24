import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

start_time = time.time()


temps = pd.read_csv('dataCabine.csv', sep =";")


title = 'Temperatures'
y = np.array(temps.loc[:, "Temp1":"Temp1"])
x = np.array(temps.loc[:, 'Sample':'Sample'])
#temps.columns = {title}

##initialize the writer
#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=1800)


fig, ax = plt.subplots()
plt.xlim(0, np.max(x))
plt.ylim(np.min(y), np.max(y))
plt.xlabel('time',fontsize=20)
plt.ylabel(title,fontsize=20)
plt.title('Measured temperature',fontsize=20)

line, = ax.plot(x, y, color='b', label='Temp1')


def animate(i):
    line.set_data(x[:i], y[:i])  
    
    
    
ani = matplotlib.animation.FuncAnimation(fig, animate, interval=10, frames=len(x)-1)

ani.save('result.mp4', dpi=300)

print("--- %s seconds ---" % (time.time() - start_time))