#Define any number of functions written in python
def f(x):
	return math.sin(x)
def g(x):
	return math.cos(x)
def h(x):
	return -math.sin(x)
def i(x):
	return -math.cos(x)

#Put all the functions you want to plot into this python array
#Priority is given to later functions
functions = [f,g,h,i]

#Enable or disable truecolors
#True colors does not work in all environments
#To find out if your environment supports truecolors follow this link
#https://gist.github.com/XVilka/8346728
truecolors = False

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
#Available with truecolors enabled:
#-purple
#-pink
#-brown

#Default for no color
colors = [rainbow,rainbow,rainbow,rainbow]

#State whether it should be in polar coordinates
#(true is polar false is cartesian)
polar = False

#Define the x size of each character
#(distance between tick marks on the graph)
x_size = 1/32.

#Define the y size of each character
y_size = 1/16.

#Define the start and end of the x partitions
x_min = -65
x_max = 65

#Define the start and end of the y partitions
y_min = -70
y_max = 70

#Turn autofit on or off
autofit = True

#State whether or not axes should be plotted
plot_axes = False

#For Polar plots

#Define the t partitions
t_size = .003
t_min = 0
#Angle in radians
t_max = 4*math.pi
