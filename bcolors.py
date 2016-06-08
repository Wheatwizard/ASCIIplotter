#Dark colors
BLACK =   '\033[38;5;0m'
DARKRED =     '\033[38;5;1m'
DARKGREEN =   '\033[38;5;2m'
DARKYELLOW =  '\033[38;5;3m'
DARKBLUE =    '\033[38;5;4m'
DARKMAGENTA = '\033[38;5;5m'
DARKCYAN =    '\033[38;5;6m'
LIGHTGREY = '\033[38;5;7m'
#Light colors
DARKGRAY =   '\033[38;5;0m'
RED =     '\033[38;5;1m'
GREEN =   '\033[38;5;2m'
YELLOW =  '\033[38;5;3m'
BLUE =    '\033[38;5;4m'
MAGENTA = '\033[38;5;5m'
CYAN =    '\033[38;5;6m'
GREY = '\033[38;5;7m'
#Custom colors
ORANGE = '\033[38;5;202m'
DARKORANGE = '\033[38;5;130m'
#True colors
TRUEORANGE = '\033[38;2;255;127;0m'
TRUEDARKORANGE = '\033[38;2;127;63;0m'
TRUEPINK = '\033[38;2;255;127;127m'
TRUEPURPLE = '\033[38;2;255;0;255m'
TRUEBROWN = '\033[38;2;127;63;0m'
#End character
ENDC =  '\033[0m'

def getcolor(r, g, b):
	return '\033[38;2;%d;%d;%dm' %(r,g,b)

def rainbow(x):
	y = 510-abs(510-x%1021)
	return getcolor(255-y/2,255-abs(255-y),y/2)

if __name__ == '__main__':
	for x in range(0,2000):
		print rainbow(x) + '#',
	print ENDC
