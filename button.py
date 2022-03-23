# Author: Nik Delgado
# Created: 3/22/22

import pygame

# This class defines button characteristics and draws a button onto the screen and determines if the mouse is hovering over the button
class Button():
	
	# Initialize the class
	def __init__(self, color, x, y, width, height, text=''):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text
	
	# take in paramaters and print a rectangle with text onto the screen
	def draw(self, display):
		pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height), 0)
		
		font = pygame.font.Font(None, 30)	
		text = font.render(self.text, 1, (0, 0, 0))
		
		display.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
	
	# Determine of the mouse position is over the screen
	def is_over(self, position):
		if position[0] > self.x and position[0] < self.x + self.width:
			if position[1] > self.y and position[1] < self.y + self.height:
				return True
		return False
