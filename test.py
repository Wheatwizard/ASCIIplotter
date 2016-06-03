#Define any number of functions written in python
def f(x):
	return 2*x

#Put all the functions you want to plot into this python array
#Priority is given to later functions
functions = [f]

#State whether it should be in polar coordinates
#(true is polar false is cartesian)
polar = True

#Define the x size of each character
#(distance between tick marks on the graph)
x_size = 1

#Define the y size of each character
y_size = 2

#Define the start and end of the x partitions
x_min = -35
x_max = 35

#Define the start and end of the y partitions
y_min = -17
y_max = 17

#State whether or not axes should be plotted
plot_axes = False

#For Polar plots

#Define the t partitions
t_size = .03
t_min = 0
#Angle in radians
t_max = 4*math.pi