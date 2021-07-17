import functions
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from itertools import count
import pandas as pd
import numpy as np
import pylab as pl
from numpy import fft
import random
from collections import deque
import seaborn as sns
import sys

sns.set(font='Franklin Gothic Book',rc={
'axes.axisbelow': False,
'axes.edgecolor': 'lightgrey',
'axes.facecolor': 'None',
'axes.grid': False,
'axes.labelcolor': 'dimgrey',
'axes.spines.right': False,
'axes.spines.top': False,
'figure.facecolor': 'white',
'lines.solid_capstyle': 'round',
'patch.edgecolor': 'w',
'patch.force_edgecolor': True,
'text.color': 'dimgrey',
'xtick.bottom': False,
'xtick.color': 'dimgrey',
'xtick.direction': 'out',
'xtick.top': False,
'ytick.color': 'dimgrey',
'ytick.direction': 'out',
'ytick.left': False,
'ytick.right': False})
sns.set_context("notebook", rc={"font.size":16,
"axes.titlesize":20,
"axes.labelsize":16})

sr = 15
f1c_max = 1273
t = [float(round(i,4)) for i in np.arange(0,615,sr)]
x_val = 0
f = []
a = []
for i in t:
	f.append(function_generator.ptforce(i,f1c_max))
	a.append(function_generator.tilt_angle(i))

time=[];force=[];angle=[];

def animate(i):
	global x_val,time,force,angle,sr
	if x_val < len(t):
		time.append(t[x_val])
		force.append(f[x_val])
		angle.append(a[x_val])

	elif x_val >= len(t) and x_val <= 1000/sr:
		time.append(time[x_val-1]+15)
		force.append(0)
		if angle[x_val-1] > -15:
			angle.append(angle[x_val-1]-5)
		else:
			angle.append(-20)
	else:
		time = [0]
		force = [20]
		angle = [-20]
		x_val = 0
		sys.exit()

	plt.figure(figsize=(8,15))
	# plt.title("0.5x Playback Speed")
	sub1 = plt.subplot(2,1,1)
	sub1.cla()
	if x_val > 200/sr:
		ax1 = plt.gca()
		sub1.text(0.18,0.3,f"Loading Phase", fontsize=14, color='#661D98', transform=ax1.transAxes)
	if x_val > 600/sr:
		sub1.text(0.70,0.3,f"Swing Phase", fontsize=14, color='#661D98', transform=ax1.transAxes)
	sub1.plot(time,force,color='#47DBCD',linewidth=3)
	plt.xlim([0, 1000])
	plt.ylim([0, 1300])
	plt.xlabel("Time [ms]")
	plt.ylabel("F(t) [Newtons]")
	plt.title("Applied Force Profile")

	sub2 = plt.subplot(2,1,2)
	sub2.cla()
	sub2.plot(time,angle,color='#0036ff',linewidth=3)
	plt.xlim([0, 1000])
	plt.ylim([-25, 45])
	plt.xlabel("Time [ms]")
	plt.ylabel("$\\theta$(t) [Degrees]")
	plt.title("Angle Profile")
	plt.savefig(f"/senior_design/amination_new/output/done4/{x_val}.png")

	x_val += 1

ani = animation.FuncAnimation(plt.gcf(),animate,interval=1000)
plt.show()


# plt.xlabel("Time [ms]")
# plt.ylabel("Force [N]")
# plt.title("Applied Test Force - F(t)")



# plt.xlabel("Time [ms]")
# plt.ylabel("[Degrees]")
# plt.title("Tiltiling Table Angular Position - r"${\\Theta}$[Degrees]"
