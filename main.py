# Author: Nik Delgado
# Created: 3/22/22

import pygame
from sys import exit
import print_display
import solver
import button

# Unsolved Sudoku number array
num_arr = [
	[7, 8, 0, 4, 0, 0, 1, 2, 0],
	[6, 0, 0, 0, 7, 5, 0, 0, 9],
	[0, 0, 0, 6, 0, 1, 0, 7, 8],
	[0, 0, 7, 0, 4, 0, 2, 6, 0],
	[0, 0, 1, 0, 5, 0, 9, 3, 0],
	[9, 0, 4, 0, 6, 0, 0, 0, 5],
	[0, 7, 0, 3, 0, 0, 0, 1, 2],
	[1, 2, 0, 0, 0, 7, 4, 0, 0],
	[0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Initialize Pygame
pygame.init()

# Define display window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 540

# Initialize display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set screen background
screen.fill((255, 255, 255))

# Set application name
pygame.display.set_caption("Sudoku Solver")
	
# Set framerate
clock = pygame.time.Clock()

# Initialize sudoku board
board = print_display.Print_Display(SCREEN_WIDTH, SCREEN_HEIGHT, num_arr)


# Initialize game start button
button = button.Button((0, 255, 0), 210, 550, 120, 40, 'Start')


# Initialze solver
sudoku = solver.Solver(num_arr, screen)

# Game loop
while True:
	
	# If user exits program window, program ends
	for event in pygame.event.get():
		pos = pygame.mouse.get_pos()
		
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	
	# Print Sudoku Lines
	board.draw_lines(screen)
	
	# Print unsolved sudoku numbers onto the screen
	sudoku.print_numbers()

	# Print start button onto screen
	button.draw(screen)
	
	
	# If user clicks the button: run solver and set to done once complete
	if event.type == pygame.MOUSEBUTTONDOWN:
		if button.is_over(pos):
			
			# Set color and text
			button.text = ('Done')
			button.color = (255, 0, 0)
			
			# Update Display
			pygame.display.update()
			
			#Call solve method
			sudoku.solve()
		
		
	

	