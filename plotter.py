import math

import bcolors

import os

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
	
	truecolors = False

	#Set up colors
	red = lambda x:bcolors.RED
	blue = lambda x:bcolors.BLUE
	green = lambda x:bcolors.GREEN
	yellow = lambda x:bcolors.YELLOW
	magenta = lambda x:bcolors.MAGENTA
	cyan = lambda x:bcolors.CYAN
	grey = lambda x:bcolors.GREY
	orange = lambda x:bcolors.TRUEORANGE if truecolors else bcolors.ORANGE
	pink = lambda x:bcolors.TRUEPINK if truecolors else bcolors.ENDC
	purple = lambda x:bcolors.TRUEPURPLE if truecolors else bcolors.ENDC
	brown = lambda x:bcolors.TRUEBROWN if truecolors else bcolors.ENDC
	#Rainbow frequency is denoted by this arbitrary number (6 for now)
	#later I may make plans to change this to be customizable
	__r = 6
	rainbow = lambda x:bcolors.rainbow(x*__r) if truecolors else [
		bcolors.RED,
		bcolors.ORANGE,
		bcolors.YELLOW,
		bcolors.GREEN,
		bcolors.CYAN,
		bcolors.BLUE,
		bcolors.DARKMAGENTA][(x/__r)%7
	]
	default = lambda x:bcolors.ENDC
	
	#Default all variables for the file
	functions = []
	colors = []
	x_size = 1
	y_size = 1
	x_min = 0
	x_max = 0
	y_min = 0
	y_max = 0
	autofit = False
	plot_axes = False
	t_size = 1
	t_min = 0
	t_max = 2*math.pi
	
	#Set up terminal defaults
	max_y, max_x = os.popen('stty size','r').read().split()
	max_y, max_x = int(max_y)-1,int(max_x)-1
	
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

	#Fix descrepancies betwen functions and colors	
	if len(functions) < len(colors):
		colors = colors[:len(functions)]
	
	if len(functions) > len(colors):
		colors += [default] * (len(functions)-len(colors))
	
	#Plot functions
	for (function, color) in zip(functions,colors):
		if polar:
			plot.plot_polar(function, color)
		else:
			plot.plot_function(function, color)
	plot.print_plot()	
