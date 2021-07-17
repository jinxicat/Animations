
def ptforce(t,f1c_max):
	#function for approximating pulsating test force Fc(t)
	#ISO 22675 pg 33
	f = 0.001*(f1c_max*10**-3*(5123.06842296552E-12*t**6-9203.7374110419E-9*t**5+5988.82225167948E-6*t**4-1671.01914899229E-3*t**3+1646.51497111425E-1*t**2+3624.95690883228*t))
	return f


def tilt_angle(t):
	#function for approximating tilting angle Y(t)
	#ISO 22675 pg 32
	a = 0.001*(2450.74E-12*t**5.0-3759.84E-9*t**4.0+1775.19E-6*t**3.0-1084.09E-4*t**2.0+2072.17E-2*t-20041)
	return a

	
