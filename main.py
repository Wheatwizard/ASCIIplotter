import math

def f(x):
	return 8*math.tan(x/8.)

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
	x_min = -90
	x_max = 90
	y_min = -90
	y_max = 90
	plot = [[' ' for y in range(y_min, y_max+1)] for x in range(x_min, x_max+1)]
	for x in range(x_min, x_max):
		plot[x][0] = '.'
	for y in range(y_min, y_max):
		plot[0][y] = ':'
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
	
