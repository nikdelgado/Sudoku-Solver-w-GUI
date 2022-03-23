# Author: Nik Delgado
# Created: 3/22/22

import pygame
import time
import print_display

# This class solves a sudoku number array
class Solver():
	
	# initialize the class with an array and a display to print to
	def __init__(self, arr, display):
		self.board = arr
		self.display = display
	
	# print numbers to display
	def print_numbers(self):
		# Define font of numbers
		font = pygame.font.Font(None, 30)	
		
		# Define starting position of numbers
		y_size = 25
		x_size = 25
		
		# Row and col counter for board array
		row = 0
		col = 0
		
		# Loop through board array and place numbers. If number is zero, ignore.
		for j in range (1,10):
			for i in range (1,10):
				if (self.board[row][col] != 0):
					
					pygame.draw.rect(self.display, (255, 255, 255), (x_size, y_size, 20, 20))
					number = font.render(str(self.board[row][col]), True, (0, 0, 0))
					
					
					self.display.blit(number, (x_size, y_size))
					
				# Increment x position, and get next element in array	
				x_size += 60
				col += 1
			
			# Increment y position and set x position back to starting position
			y_size += 60
			x_size = 25
			
			# Get the next row of elements from array
			row += 1	
			col = 0
		# Update display after complete
		pygame.display.flip()
		pygame.display.update()
		
	# This method returns the position of an empty slot on the board
	def get_empty_slot(self):
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				if (self.board[row][col] == 0):
					return row, col
		
		# Row and col are default set as none if no empty slots are available. 
		row = None
		col = None
		return row, col
	
	# This method takes in a number and checks if the number is valid to place in the given position on the sudoku board
	def check_valid(self, row, col, num):
		
		# Check if row is valid
		for i in range(len(self.board[row])):
			if (self.board[row][i] == num):
				return False
			
		# Check if column is valid
		for i in range(len(self.board[col])):
			if (self.board[i][col] == num):
				return False
			
		# Set quadrant row and column to check
		quadrant_row = row // 3
		quadrant_col = col // 3
		
		# Check quadrant
		for i in range(quadrant_row * 3, quadrant_row * 3 + 3):
			for j in range(quadrant_col * 3, quadrant_col * 3 + 3):
				if (self.board[i][j] == num):
					return False
				
		# if all tests pass return true
		return True
	
	# This method solves the sudoku puzzle by using the backtracking algorithim
	def solve(self):
		
		# set timer to slow down and allow user to visualize algorithm working
		time.sleep(0.2)
		
		# Print numbers after each iteration of solve() method
		self.print_numbers()
		
		# Get a new empty slot
		row, col = self.get_empty_slot()
		
		# if row and col are empty, job is done
		if(row == None and col == None):
			return True
		
		# loop that sends a number from 1-10 to check if the number will fit in slot
		for i in range(1,10):
			
			# Check if number will work in the slot
			is_valid = self.check_valid(row, col, i)
			
			# If its valid, place item in slot
			if (is_valid == True):
				self.board[row][col] = i
				
				# If the next layer of the function returns true, return true
				if self.solve():
					return True
				
				# Else, set slot to zero
				self.board[row][col] = 0
				
		return False
		