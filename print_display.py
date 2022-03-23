# Author: Nik Delgado
# Created: 3/22/22

import pygame

# This class prints objects to the display window
class Print_Display():
	
	# Initialize class with screen height and width parameters
	def __init__(self, x, y, arr):
		self.width = x
		self.height = y
		self.board = arr

	# Draw sudoku lines onto the scree	
	def draw_lines(self, screen):
		
		# Set starting position
		x_size = 60
		y_size = 60
		
		# Loop through and print lines 
		for i in range(1,10):
			if (i % 3 == 0 and i != 9):
				pygame.draw.line(screen, (0,0,0), (0, y_size), (540, y_size), 4)
				pygame.draw.line(screen, (0,0,0), (x_size, 0), (x_size, 540), 4)
				
			else: 
				pygame.draw.line(screen, (0,0,0), (0, y_size), (540, y_size), 2)
				pygame.draw.line(screen, (0,0,0), (x_size, 0), (x_size, 540), 2)
			
			# Increment size once complete
			y_size += 60
			x_size += 60
		
		# Update display once done
		pygame.display.flip()
		pygame.display.update()
		