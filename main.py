import pygame
import random
import math
from time import sleep

#Define variables wich represent the size of the map we want
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

#Create the ball class
class Ball:
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
		#Add a variable to the PlayerBall class for the cooldown of touching the green ball
		self.green_cooldown = 0
		self.red_cooldown = 0

	#The move function is responsible for changing the position of the ball based on the user input
	def move(self, mv_type):
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

	#This function checks if the player's ball is touching another ball
	def check_contact(self, greenBall, redBall):
		#If the distance between the two centers is less that the sum of the radius of both balls then they are touching
		if math.sqrt((self.y - greenBall.y) ** 2 + (self.x - greenBall.x) ** 2) < self.radius + greenBall.radius:
			#If the same ball hasn't been touched recently update the cooldown and return 10
			if self.green_cooldown == 0:
				self.green_cooldown = 10
				return 10
		if math.sqrt((self.y - redBall.y) ** 2 + (self.x - redBall.x) ** 2) < self.radius + redBall.radius:
			#If the same ball hasn't been touched recently update the cooldown and return 10
			if self.red_cooldown == 0:
				self.red_cooldown = 10
				return -50
		return 0

#This class represents the green ball that gives points when the player's ball touches it
class GreenBall(Ball):
	#Similarly to the player's ball, this class extends Ball but has two new variables
	def __init__(self, x, y, radius, color, screen):
		Ball.__init__(self, x, y, radius, color, screen)
		#vx and vy are the velocity values for this ball and are generated randomly when a GreenBall object is created
		self.vy = random.randint(0, 4) - 2
		self.vx = random.randint(0, 4) - 2
		while self.vy == 0 or self.vx == 0:
			self.vy = random.randint(0, 4) - 2
			self.vx = random.randint(0, 4) - 2

	#This function will update the ball's position
	def move(self):
		#Add the velocity value to the position
		self.x += self.vx
		self.y += self.vy

		#If the ball is outside the bounds put it inside and multiply the velocity to -1 to change the ball's direction
		if self.x - self.radius < 0:
			self.x = self.radius
			self.vx *= -1
		elif self.x + self.radius > SCREEN_WIDTH:
			self.x = SCREEN_WIDTH - self.radius
			self.vx *= -1
		if self.y - self.radius < 0:
			self.y = self.radius
			self.vy *= -1
		elif self.y + self.radius > SCREEN_HEIGHT:
			self.y = SCREEN_HEIGHT - self.radius
			self.vy *= -1
	
class RedBall(Ball):
	#Similarly to the player's ball, this class extends Ball but has two new variables
	def __init__(self, x, y, radius, color, screen):
		Ball.__init__(self, x, y, radius, color, screen)
		#vx and vy are the velocity values for this ball and are generated randomly when a RedBall object is created
		self.vy = random.randint(3, 6) - 2
		self.vx = random.randint(3, 6) - 2

	#This function will update the ball's position
	def move(self):
		#Add the velocity value to the position
		self.x += self.vx
		self.y += self.vy

		#If the ball is outside the bounds put it inside and multiply the velocity to -1 to change the ball's direction
		if self.x - self.radius < 0:
			self.x = self.radius
			self.vx *= -1
		elif self.x + self.radius > SCREEN_WIDTH:
			self.x = SCREEN_WIDTH - self.radius
			self.vx *= -1
		if self.y - self.radius < 0:
			self.y = self.radius
			self.vy *= -1
		elif self.y + self.radius > SCREEN_HEIGHT:
			self.y = SCREEN_HEIGHT - self.radius
			self.vy *= -1

#The next two lines initiate the game and set the window size by the values we defined on the variables SCREEN_HEIGHT and SCREEN_WIDTH
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#The next variable represents if the user wants to quit the game (when the value is True) or not (when the value is False)
#Since we want the game to run we start it with as False
done = False
#The score variable will store the player's current score
score = 0

#Set the font and size that will be used
myfont = pygame.font.SysFont("monospace", 15)

#Create a clock value that allows us to set the FPS value we want
clock = pygame.time.Clock()

#Create two ball: the player's ball (PlayerBall class) and the green ball (GreenBall class)
ball1 = PlayerBall(100, 100, 20, (0, 0, 0), screen)
ball2 = GreenBall(200, 200, 5, (0, 255, 0), screen)
ball3 = RedBall(300, 200, 40, (255, 0, 0), screen)

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
	if pressed[pygame.K_UP]:
		ball1.move("UP")
	if pressed[pygame.K_DOWN]:
		ball1.move("DOWN")
	if pressed[pygame.K_LEFT]:
		ball1.move("LEFT")
	if pressed[pygame.K_RIGHT]:
		ball1.move("RIGHT")

	#Paint the screen white
	screen.fill((255, 255, 255))
	
	#Set the label value to be black and write the actual score
	label = myfont.render("SCORE: " + str(score), 1, (0,0,0))

	#Print that label in the screen
	screen.blit(label, (10, SCREEN_HEIGHT - 20))

	if score == 1000:
		game_over = myfont.render("YOU WIN!", 1, (0,0,0))
		screen.blit(game_over, (10, SCREEN_HEIGHT - 50))
		pygame.display.flip()
		sleep(5)
		done = True
	if score == -1000:		
		game_over = myfont.render("YOU LOSE!", 1, (0,0,0))
		screen.blit(game_over, (10, SCREEN_HEIGHT - 50))
		pygame.display.flip()
		sleep(5)
		done = True
	
	

	#Call the move function for the green ball
	ball2.move()
	ball3.move()
	
	#Add to the score the value returned. (Returns 10 if touching the green ball and 0 otherwise)
	score += ball1.check_contact(ball2, ball3)

	#Draw both the player's ball and the green ball
	ball3.draw()
	ball2.draw()
	ball1.draw()

	#Update the cooldown for touching the green ball at every frame. When it's value is 0 then we can touch a ball again
	if ball1.green_cooldown > 0:
			ball1.green_cooldown -= 1
	if ball1.red_cooldown > 0:
			ball1.red_cooldown -= 1

	#Update the screen
	pygame.display.flip()
	#Set the FPS value to 60
	clock.tick(60)