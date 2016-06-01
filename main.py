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
		back_diff = f(x)-f(x-1)
		diff = f(x+.5)-f(x-.5)
		front_diff = f(x+1)-f(x)	
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
		
		#Complete the line if it is non-continuous
		if back_diff < -1:
			y = int(f(x))+1
			while y < f(x-.5) and y < y_max:
				plot[x][y] = '|'
				y += 1
		elif back_diff > 1:
			y = int(f(x))-1
			while y > f(x-.5) and y > y_min:
				plot[x][y] = '|'
				y -= 1
		if front_diff < -1:
			y = int(f(x))-1
			while y > f(x+.5) and y > y_min:
				plot[x][y] = '|'
				y -= 1
		elif front_diff > 1:
			y = int(f(x))+1
			while y < f(x+.5) and y < y_max:
				plot[x][y] = '|'
				y += 1	
	print_plot(plot, x_min, y_min)
	
