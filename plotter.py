import math

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
	
	#Execute the code in the test file
	exec(open(file_name).read())
	
	#Determine Autofit bounds
	if autofit:
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
	
	plot = Plot(x_min, x_max, x_size, y_min, y_max, y_size, t_min, t_max, t_size)
		
	#Plot axes
	if plot_axes: plot.plot_axes
	
	#Plot functions
	for function in functions:
		if polar:
			plot.plot_polar(function)
		else:
			plot.plot_function(function)
	plot.print_plot()	
