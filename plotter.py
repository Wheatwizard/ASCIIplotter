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
	
	plot = Plot(x_min, x_max, x_size, y_min, y_max, y_size)
		
	#Plot axes
	if plot_axes: plot.plot_axes
	
	#Plot function
	plot.plot_function(function)
	plot.print_plot()	
