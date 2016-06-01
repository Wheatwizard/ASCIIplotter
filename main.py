import math

from sys import argv

def abs(x):
	if x < 0:
		return -x
	return x

def print_plot(plot, x_min, y_min):
	result = ''
	for y in range(y_min, len(plot[0])+y_min)[::-1]:
		for x in range(x_min, len(plot)+x_min):
			result += plot[x][y]
		result += '\n'
	print result

if __name__ == '__main__':
	if len(argv) < 2:
		print "Please provide a file name for parameters"
		exit(0)
	#Get commandline arguments
	script, file_name = argv
	
	#Execute the code in the test file
	exec(open(file_name).read())
	
	#Modify the function
	def f(x):
		try:
			return function(x*x_size)/y_size
		except:	
			#If x is not in the domain of the function plot it outside of the graph
			#(This causes some issues with slope to be fixed later)
			return y_max+10
	
	plot = [[' ' for y in range(y_min, y_max+1)] for x in range(x_min, x_max+1)]
	
	#Plot axes
	if plot_axes:
		for x in range(x_min, x_max):
			plot[x][0] = '.'
		for y in range(y_min, y_max):
			plot[0][y] = ':'
	
	#Plot function
	for x in range(x_min, x_max):
		if int(f(x)) > y_max or int(f(x)) < y_min:
			continue
		diff = f(x+.5)-f(x-.5)
		if abs(diff) < .5:
			floor_diff = f(x)-int(f(x))
			if floor_diff > .5 and int(f(x))+1 < y_max:
				plot[x][int(f(x))+1] = '_'
			elif floor_diff < -.5:
				plot[x][int(f(x))] = '_'				
			else:
				plot[x][int(f(x))] = '-'
		elif abs(diff) > 2:
			plot[x][int(f(x))] = '|'
		elif diff < 0:
			plot[x][int(f(x))] = '\\'
		elif diff > 0:
			plot[x][int(f(x))] = '/'
	print_plot(plot, x_min, y_min)
	
