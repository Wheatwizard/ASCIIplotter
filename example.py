#Define any number of functions written in python
def f(x):
	return math.exp(abs(x))

#Put all the functions you want to plot into this python array
#Priority is given to later functions
functions = [f]

#Put colors for each plot
#Available colors are:
#-magenta
#-red
#-orange
#-yellow
#-green
#-blue
#-cyan
#-grey
#-black

#Default for no color
colors = [red]

#State whether it should be in polar coordinates
#(true is polar false is cartesian)
polar = False

#Define the x size of each character
#(distance between tick marks on the graph)
x_size = 1/4.

#Define the y size of each character
y_size = 1/2.

#Define the start and end of the x partitions
x_min = -20
x_max = 20

#Define the start and end of the y partitions
y_min = -1
y_max = 30

#Turn autofit on or off
autofit = False

#State whether or not axes should be plotted
plot_axes = False

#For Polar plots

#Define the t partitions
t_size = .003
t_min = 0
#Angle in radians
t_max = 4*math.pi
