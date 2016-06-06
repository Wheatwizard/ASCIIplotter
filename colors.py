class bcolors:
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
	ENDC =  '\033[0m'
if __name__ == '__main__':
	print '\033[38;5;130m' + '1'
	print '\033[38;5;202m' + '2' 
	print bcolors.ENDC
