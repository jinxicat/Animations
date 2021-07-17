import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

df = pd.read_csv("important_values_2.csv")
df.dropna(inplace=True)

print(df.head())

# plt.plot(df['time [ms]'],df['instantaneous pulse frequency [kHz]'])
# plt.show()
t_real = df['time'].values
f_real = df['angle'].values

# print(len(t))
# print(len(f))

# print(type(t))
# print(type(f))

# print(t)
# print(f)

output = np.polyfit(t_real,f_real,1)
print(output)
 
# output_y=np.polyval(output,t)Exc
# print(output_y)
def freq(t):
	f = 3.40380556238001E-09*t**4 -18440762007152E-06*t**3 + 0.001485598211558*t**2 - 0.061710728884167*t +5.78663557424503
	return f

def foft_loading(t):
	f = t**4*3.40380556e-09+t**3*-4.18440762e-06+t**2*1.48559821e-03+t*-6.17107289e-02+5.78663557e+00
	return f

t_in = [i for i in range(1,601)]
t_in_2 = [i for i in range(601,1001)]

freqs_loading = []
for t in t_in:
	freqs_loading.append(foft_loading(t))

# freqs_swing = []
# for t in t_in:
# 	freqs_swing.append(foft_swing(t))

a_loading = [2.45074E-12*t**5.0-3.75984E-9*t**4.0+1.77519E-6*t**3.0-1.08409E-4*t**2.0+2.07217E-2*t-20.041 for t in t_in]
a_swing = [40 - 0.15*t for t in range(1,401)]


matplotlib.rcParams.update({'font.size':13})

plt.figure(1)

ax = plt.gca()
# ax2 = ax.twinx()

ax.plot(a_loading,freqs_loading)
ax.plot(a_swing,[41.771 for i in range(len(a_swing))],color='green')
ax.set_xlabel("Loop time [miliseconds]")
ax.set_ylabel("PWM frequency [kHz]")
ax.legend(['Loading Cycle','Swing Cycle'],loc='upper center',bbox_to_anchor=(0.9,1.15))

# ax2.plot(a_loading,[1 for i in range(len(a_loading))],color='red')
# ax2.plot(a_swing,[-1 for i in range(len(a_swing))],color='red')
# ax2.set_ylim(ymin=-2.5,ymax=2.5)
# ax2.set_ylabel('Sevo Direction Pin (1=HIGH/POS; -1=LOW/NEG)')
# ax2.legend(['Servo Direction'],loc='upper center',bbox_to_anchor=(0.9,1.05))


plt.title("Proposed Angle Dependent Functions")
plt.show()
# t=600
# print(freq(t))

# t_swing = np.arange(601,1001)

# #the table has to rotate 60 degrees in 400 ms
# # delta_angle = 60
# # delta time = 400 ms

# p1 = (601,40)
# p2 = (1000,-20)
# m = (p2[1]-p1[1]) / ((p2[0]-p1[0]))
# b = (m*p1[0])+p1[1]

# print(p1,p2,m)
# alpha_of_t = lambda x: m*x+b
# # alpha_of_t = lambda x: (m*x)-561
# # alpha_of_t = lambda x: m*(x-p1[0])+p1[1]
# angles = [alpha_of_t(t) for t in range(p1[0], p2[0])]
# # angles = [alpha_of_t(t) for t in range(0,400)]
# # 
# plt.plot(range(len(angles)), angles)
# plt.show()
