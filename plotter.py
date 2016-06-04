import math

from colors import bcolors

from sys import argv

from plot import Plot
	
def abs(x):
	if x < 0:
		return -x
	return x
	
if __name__ == '__main__':
	if len(argv) < 2:
		print "Please provide a file name for parameters"
		exit(0)
	#Get commandline arguments
	script, file_name = argv
	
	#Set up colors
	red = bcolors.RED
	blue = bcolors.BLUE
	green = bcolors.GREEN
	yellow = bcolors.YELLOW
	pink = bcolors.PINK
	default = bcolors.ENDC

	#Execute the code in the test file
	exec(open(file_name).read())
	
	#Determine Autofit bounds
	if autofit and not polar:
		y_max = 0
		y_min = 0
		for function in functions:
			#define temporary function to prevent domain errors
			def f(x):
				try: return function(x*x_size)/y_size
				except:	return 0
			values = [ f(x) for x in range(x_min, x_max) ]
			y_max = max(y_max,max(values))
			y_min = min(y_min,min(values))
		y_max = int(y_max + 1) + 1
		y_min = int(y_min - 1) - 1		
	
	if autofit and polar:
		x_max = 0
		x_min = 0
		y_max = 0
		y_min = 0
		for function in functions:
			#define temporary version of class functions
			def f(t):
				try: return function(t*t_size)
				except: return 0
			def getX(t):
				return f(t)*math.cos(t*t_size)/x_size
			def getY(t):
				return f(t)*math.sin(t*t_size)/y_size
			x_values = [ getX(t) for t in range(int(t_min/t_size),int(t_max/t_size)) ]
			y_values = [ getY(t) for t in range(int(t_min/t_size),int(t_max/t_size)) ]
			x_max = max(x_max, max(x_values))
			x_min = min(x_min, min(x_values))
			y_max = max(y_max, max(y_values))
			y_min = min(y_min, min(y_values))
		x_max = int(x_max + 1) + 1
		x_min = int(x_min - 1) - 1
		y_max = int(y_max + 1) + 1
		y_min = int(y_min - 1) - 1
		
	plot = Plot(x_min, x_max, x_size, y_min, y_max, y_size, t_min, t_max, t_size)
		
	#Plot axes
	if plot_axes: plot.plot_axes
	
	#Plot functions
	for (function, color) in zip(functions,colors):
		if polar:
			plot.plot_polar(function, color)
		else:
			plot.plot_function(function, color)
	plot.print_plot()	
