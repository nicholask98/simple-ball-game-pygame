# gain access to the pygame module
import pygame

# defines guidelines for all "Ball" objects
class Ball:
    # Every time a 'Ball' type object is created it has these attributes and must have an x, y, radius and screen to pass in
	def __init__(self, x, y, radius, screen):
        # all passed in attributes become instance-specific
		self.x = x
		self.y = y
		self.radius = radius
		self.screen = screen
    # draws a blue circle with the instance's radius in the instance's x,y position
	def draw(self):
		pygame.draw.circle(screen, (0, 0, 255), [self.x, self.y], self.radius)

# initializes pygame. Required to start using the module.
pygame.init()

# sets the window at 400px wide by 300 px tall
screen = pygame.display.set_mode((400, 300))

# sets variable for game loop to false
done = False

# Not sure exactly what Clock function is. I'm guessing it tracks the amount of time since Pygame was initialized.
clock = pygame.time.Clock()

# creates a new ball object named "ball1" with position (100, 100), a radius of 20 and on the screen window.
ball1 = Ball(100, 100, 20, screen)

# begin game loop. Will continue to loop until done == True
while not done:
    # loops through event cue checking for Pygame QUIT event. If QUIT is True in any event, done = True and the game loop ends.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			# =================WORK ON THIS NEXT: Ball movement with arrow keys===================
		if event.type == pygame.KEYDOWN:
			if event == K.LEFT:
				pass
			if event == K.RIGHT:
				pass
			if event == K.UP:
				pass
			if event == K.DOWN:
				pass

			# ====================================
    # fills window with black
	screen.fill((0, 0, 0))



    # uses Ball method "draw" to paint the ball in its current position on the screen.
	ball1.draw()

    # updates the window
	pygame.display.flip()

    # game loop updates every 60 ms
	clock.tick(60)