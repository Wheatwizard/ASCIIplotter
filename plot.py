import math

import bcolors

class Plot(object):
	def __init__(self, x_min, x_max, x_size, y_min, y_max, y_size, t_min, t_max, t_size):
		self.x_min = x_min
		self.x_max = x_max
		self.x_size = x_size
		self.y_min = y_min
		self.y_max = y_max
		self.y_size = y_size
		self.t_min = t_min
		self.t_max = t_max
		self.t_size = t_size
		self.internal_plot = [[' ' for y in range(y_min, y_max+1)] for x in range(x_min, x_max+1)]
		self.color = bcolors.ENDC
		self.color_plot = [[bcolors.ENDC for y in range(y_min, y_max+1)] for x in range(x_min, x_max+1)]
	def set(self,a,b,char):
		if (a < self.x_max and a > self.x_min and b < self.y_max and b > self.y_min):
			self.color_plot[a][b] = self.color
			if set([char,self.internal_plot[a][b]]) == set(['\\','/']):
				self.internal_plot[a][b] = 'X'
			elif set([char,self.internal_plot[a][b]]) == set(['-','|']):
				self.internal_plot[a][b] = '+'
			elif char == self.internal_plot[a][b] == '-':
				self.internal_plot[a][b] = '='
			else:
				self.internal_plot[a][b] = char
	def plot_axes(self):
		for x in range(self.x_min, self.x_max):
			plot[x][0] = '.'
		for y in range(self.y_min, self.y_max):
			plot[0][y] = ':'
	def print_plot(self):
		result = ''
		for y in range(self.y_min, len(self.internal_plot[0])+self.y_min)[::-1]:
			for x in range(self.x_min, len(self.internal_plot)+self.x_min):
				result += self.color_plot[x][y] + self.internal_plot[x][y] + bcolors.ENDC
			result += '\n'
		print result
	def plot_polar(self, function, color):
		def f(t):
			try: return function(t*self.t_size)
			except: return max(self.x_max,self.y_max,-self.x_min,-self.y_min)+10
		
		def getX(t):
			return f(t)*math.cos(t*self.t_size)/self.x_size
		
		def getY(t):
			return f(t)*math.sin(t*self.t_size)/self.y_size
		
		#Initialize x_last and y_last to be values the first can never match
		x_last = int(getX(int(self.t_min/self.t_size))) + 1
		y_last = int(getY(int(self.t_min/self.t_size))) + 1
		
		for t in range(int(self.t_min/self.t_size), int(self.t_max/self.t_size)):
			#Set the color so the function graphs in the right color
			self.color = color(t)

			x = int(getX(t))
			y = int(getY(t))
			a = (t*self.t_size) % math.pi
			
			#Get cartesian slope
			
			x_diff = getX(t+.5) - getX(t-.5)
			y_diff = getY(t+.5) - getY(t-.5)
			try:
				c_diff = y_diff/x_diff
			except ZeroDivisionError:
				#Division by zero results in infinite slope
				#This is close enough
				c_diff = x_diff * 2**64
			
			#No use replotting the same point
			if x == x_last and y == y_last:
				continue
			
			if abs(c_diff) > 2:
				self.set(x,y,'|')
			elif c_diff < -.5:
				self.set(x,y,'\\') 
			elif c_diff > .5 :
				self.set(x,y,'/')
			elif abs(c_diff) < .5:
				if getY(t)%1 < .25: 
					self.set(x,y,'_')
				elif getY(t)%1 < .75:
					self.set(x,y,'-')
				else:
					self.set(x,y+1,'_')
			else:
				self.set(x,y,'*')
			x_last = x
			y_last = y
		#Restore the color to its natural state
		self.color = bcolors.ENDC
		
	def plot_function(self, function, color):
		
		#Modify the function
		def f(x):
			try:
				return function(x*self.x_size)/self.y_size
			except:	
				#If x is not in the domain of the function plot it outside of the graph
				return self.y_max+10
		
		for x in range(self.x_min, self.x_max):
			#Set the color so the function graphs in the right color
			self.color = color(x)
		
			back_diff = int(f(x-1)) - int(f(x))
						
			#Check that the last value was valid
			try:
				function((x-1)*self.x_size)/self.y_size
			except:
				back_diff = 0
			
			diff = f(x+.5)-f(x-.5)
			front_diff = int(f(x+1)) - int(f(x))	
			
			#Check that the next value was valid
			try:
				function((x+1)*self.x_size)/self.y_size
			except:
				front_diff = 0
	
			if abs(diff) < .5:
				floor_diff = f(x)-int(f(x))
				if floor_diff > .5:
					self.set(x,int(f(x))+1,'_')
				elif floor_diff < -.5:
					self.set(x,int(f(x)),'_')			
				else:
					self.set(x,int(f(x)),'-')
			elif abs(diff) > 2:
				self.set(x,int(f(x)),'|')
			elif diff < 0:
				self.set(x,int(f(x)),'\\')
			elif diff > 0:
				self.set(x,int(f(x)),'/')
			
			#Complete the line if it is non-continuous
			#TODO compress into single for loop
			if abs(back_diff) > 1:
				for y in range(int(f(x)+math.copysign(1,int(back_diff))), int(f(x-.5))-(back_diff < 0), int(math.copysign(1,back_diff))):
					if not self.y_min < y < self.y_max:break
					self.set(x,y,'|')
			if abs(front_diff) > 1:
				for y in range(int(f(x)+math.copysign(1,int(front_diff))), int(f(x+.5))-(front_diff < 0), int(math.copysign(1,front_diff))):
					if not self.y_min < y < self.y_max:break
					self.set(x,y,'|')
		#Restore the color to its natural state
		self.color = bcolors.ENDC
