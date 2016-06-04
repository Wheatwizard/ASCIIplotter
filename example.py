#Define any number of functions written in python
def f(x):
	return math.sin(x)

def g(x):
	return math.cos(x)

def h(x):
	return -math.sin(x)

#Put all the functions you want to plot into this python array
#Priority is given to later functions
functions = [f,g,h]

#Put colors for each plot
#Default for no color

colors = [red, default, blue]

#State whether it should be in polar coordinates
#(true is polar false is cartesian)
polar = False

#Define the x size of each character
#(distance between tick marks on the graph)
x_size = 1/16.

#Define the y size of each character
y_size = 1/10.

#Define the start and end of the x partitions
x_min = -89
x_max = 89

#Define the start and end of the y partitions
y_min = 0
y_max = 0

#Turn autofit on or off
autofit = True

#State whether or not axes should be plotted
plot_axes = False

#For Polar plots

#Define the t partitions
t_size = .03
t_min = 0
#Angle in radians
t_max = 4*math.pi
