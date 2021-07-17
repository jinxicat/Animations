import matplotlib.image as mping
from scipy import ndimage

class Table():
	def __init__(self):
		self.state = mping.imread('/Desktop/amination/table.png')
		self.state = ndimage.rotate(self.state, -20, reshape=False)
	
	def update_state(self,table_angle_profile,table_xpos_profile,j):
		self.state = ndimage.rotate(self.state, table_angle_profile[j], reshape=False)
		self.state = ndimage.interpolation.affine_transform(self.state,[[1,0,0],[0,1,table_xpos_profile[j]],[0,0,1]])

	def reset_state(self):
		self.state = mping.imread('/home/chyper/Desktop/amination/table.png')
		self.state = ndimage.rotate(self.state, -20, reshape=False)
