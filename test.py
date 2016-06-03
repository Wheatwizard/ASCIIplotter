#Define any number of functions written in python
def f(x):
	return math.sin(x)

def g(x):
	return math.cos(x)

#Put all the functions you want to plot into this python array
#Priority is given to later functions
functions = [f,g]

#Define the x size of each character
#(distance between tick marks on the graph)
x_size = 1./22

#Define the y size of each character
y_size = 1./16

#Define the start and end of the x partitions
x_min = -89
x_max = 89

#Define the start and end of the y partitions
y_min = -17
y_max = 17

#State whether or not axes should be plotted
plot_axes = False
