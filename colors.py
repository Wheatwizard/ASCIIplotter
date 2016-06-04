class bcolors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    WHITE = '\033[0m'+'\033[1m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
	print bcolors.PINK + 'pink'
	print bcolors.BLUE + 'blue'
	print bcolors.GREEN + 'green'
	print bcolors.YELLOW + 'yellow'
	print bcolors.RED + 'red'
	print bcolors.WHITE + 'white'
	print bcolors.ENDC
	
