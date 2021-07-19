import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mping
from itertools import count
import foot
import table
import time

foot = foot.Foot()
table = table.Table()
axis = mping.imread('/Desktop/amination/axis.png')
force = mping.imread('/Desktop/amination/force.png')

foot_angle_profile = [0,0,0,0,0,0,-6,5,5,5,5,5,5,5,5,5,-5,-3,0,-3,-3,-3,-3,-3,-3,-3,-5,-5,0,0]
foot_ypos_profile = [-3,-3,-3,-3,-3,-6,-6,0,0,0,0,0,0,0,0,0,3,5,8,0,1,1,1,1,1,1,1,1,1,2]
foot_xpos_profile = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,3,0,0]

table_angle_profile = [0,0,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,0,-5,-5,-5,-5,-5,-8,-8,-8,-6,-5,0]
table_xpos_profile = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0]

# fa=0
# fy=25
# ta=-20

# for i in range(0,len(foot_angle_profile)):
# 	fa+=foot_angle_profile[i]
# 	fy+=foot_ypos_profile[i]
# 	ta+=table_profile[i]

# print(fa)
# print(fy)
# print(ta)

# print(len(foot_angle_profile))
# print(len(foot_ypos_profile))
# print(len(table_profile))

j = -1

def animate(i):
	global j
	j += 1
	plt.cla()
	plt.axis('off')
	
	foot.update_state(foot_angle_profile,foot_ypos_profile,foot_xpos_profile,j)
	table.update_state(table_angle_profile,table_xpos_profile,j)

	if j == 29: 
		j =-1
		foot.reset_state()
		table.reset_state()

	plt.imshow(foot.state)
	plt.imshow(table.state)
	plt.imshow(axis)
	plt.imshow(force)
	tms=int(time.time())
	plt.savefig(f"output/{j}_{tms}.png")

ani = animation.FuncAnimation(plt.gcf(),animate,interval=10)
plt.show()



# import scipy.misc
# from scipy import ndimage
# import matplotlib.pyplot as plt

# img = scipy.misc.lena()  
# # img = scipy.misc.face()  # lena is not included in scipy 0.19.1
# plt.figure(figsize=(12, 2))

# for degree in range(5):
#     plt.subplot(151+degree)
#     rotated_img = ndimage.rotate(img, degree*60)
#     plt.imshow(rotated_img, cmap=plt.cm.gray)
#     plt.axis('off')

# plt.show()
