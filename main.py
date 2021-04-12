import pygame

#Define variables wich represent the size of the map we want
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

#Create the ball class
class Ball:
	#Ball class constructor
	def __init__(self, x, y, radius, color, screen):
		#A ball need a position (x,y), a radius, a color and the screen where we will paint it, therefore
		#the constructor will take these as arguments and save their values in variables of the ball class by using the word self
		self.x = x
		self.y = y
		self.radius = radius
		self.screen = screen
		self.color = color

	#The draw function will be responsible for drawing the ball in the screen	
	def draw(self):
		pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius)

#New class for the player's ball. This class extends Ball because it has the same base features but is more specific
class PlayerBall(Ball):
	def __init__(self, x, y, radius, color, screen):
		Ball.__init__(self, x, y, radius, color, screen)
		self.score = 0

	#The move function is responsible for changing the position of the ball based on the user input
	def move(self, mv_type):
		#Update the coordinates based on the key that was pressed
		if mv_type == "UP":
			self.y -= 2
		elif mv_type == "DOWN":
			self.y += 2
		elif mv_type == "LEFT":
			self.x -= 2
		elif mv_type == "RIGHT":
			self.x += 2

		#If the ball has passed the bounds of the map then update it's position so that it stays inside
		if self.x - self.radius < 0:
			self.x = self.radius
		elif self.x + self.radius > SCREEN_WIDTH:
			self.x = SCREEN_WIDTH - self.radius
		if self.y - self.radius < 0:
			self.y = self.radius
		elif self.y + self.radius > SCREEN_HEIGHT:
			self.y = SCREEN_HEIGHT - self.radius

	def input_check(self, pressed):
		if pressed[pygame.K_UP]:
			self.move("UP")
		if pressed[pygame.K_DOWN]:
			self.move("DOWN")
		if pressed[pygame.K_LEFT]:
			self.move("LEFT")
		if pressed[pygame.K_RIGHT]:
			self.move("RIGHT")

class AutoBall(Ball):
	def __init__(self, x, y, radius, color, screen):
		Ball.__init__(self, x, y, radius, color, screen)
		self.hori_wall = 'TOP'
		self.vert_wall = 'RIGHT'

	def move(self):
		if self.hori_wall == 'TOP':
			if self.vert_wall == 'RIGHT':
				self.x -= 3
				self.y += 2
			elif self.vert_wall == 'LEFT':
				self.x += 3
				self.y += 2
		elif self.hori_wall == 'BOTTOM':
			if self.vert_wall == 'RIGHT':
				self.x -= 3
				self.y -= 2
			elif self.vert_wall == 'LEFT':
				self.x += 3
				self.y -= 2

	# vvv Keeps green ball on the screen but doesn't yet change its direction
	def wall_check(self):
		if self.x - self.radius < 0:
			self.vert_wall = "LEFT"
		elif self.x + self.radius > SCREEN_WIDTH:
			self.vert_wall = "RIGHT"
		if self.y - self.radius < 0:
			self.hori_wall = "TOP"
		elif self.y + self.radius > SCREEN_HEIGHT:
			self.hori_wall = "BOTTOM"
	

def increment_score():
	# if ball1 overlaps ball2:
		# ball1.score += 10
		

#The next two lines initiate the game and set the window size by the values we defined on the variables SCREEN_HEIGHT and SCREEN_WIDTH
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#The next variable represents if the user wants to quit the game (when the value is True) or not (when the value is False)
#Since we want the game to run we start it with as False
done = False

#Create a clock value that allows us to set the FPS value we want
clock = pygame.time.Clock()

#Create a new ball object
ball1 = PlayerBall(100, 100, 20, (0,0,0), screen)

# Create goal ball AutoBall Instance object
ball2 = AutoBall(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100, 5, (0, 255, 0), screen)

#While the user doesn't quit
while not done:
	#Listen to all events that happen
	for event in pygame.event.get():
		#If it's a quit event then set done to true so the game will finish
		if event.type == pygame.QUIT:
			done = True

	#Listen for keys pressed
	pressed = pygame.key.get_pressed()

	#Call the function to update the ball's position based on the keys that are being pressed
	ball1.input_check(pressed)

	# Checks last two walls the green ball contacted, then moves the green ball
	ball2.wall_check()
	ball2.move()

	# FIXME: NEXT TO DO!!!
	# Add Score variable (Not sure if right here is the best place). Detect if the two balls are
	# in contact, and if so, increment score variable by 10
	

	#Paint the screen white
	screen.fill((255, 255, 255))

	#Call the draw method of the ball object we created
	ball2.draw()
	ball1.draw()

	#Update the screen
	pygame.display.flip()
	
	#Set the FPS value to 60
	clock.tick(60)