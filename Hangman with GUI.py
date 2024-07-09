import pygame  # GUI using pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 1000, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HANGMAN")

FPS = 60
clock = pygame.time.Clock()
run = True

# buttons
radius = 24
space = 20
letters = []  # [399,122,"A",True]
x_start = round((WIDTH-(radius*2 + space)*13)/2)
y_start = 540

A = 65  # Using ACII value to print letters on the button. A->65, B->66 and so on

for i in range(26):
	x = x_start + space*2 + ((radius*2 + space) * (i % 13))
	y = y_start + ((i//13) * (space + radius*2))
	letters.append([x, y, chr(A+i), True])

# Fonts
font = pygame.font.SysFont("comicsans", 45)
WORD = pygame.font.SysFont("comicsans", 40)
TITLE = pygame.font.SysFont("comicsans", 70)


# Time to load images so we can draw a hangman
images = []
for i in range(0, 7):
	image = pygame.image.load("man"+str(i+1)+".png")
	images.append(image)

print(images)

# game variable
hangman = 0
lists = ["GEEKS", "GFG", "DOCKER", "DEVELOPER", "RUST", "GITHUB", "R", "PYTHON", "BASH", "NATURE", "NATUREBOY", "MARK"]
words = random.choice(lists)
guessed = []  # to track the letters we have guessed


# function to draw buttons, and hangman
def draw():
	win.fill((255, 255, 255))  # display with white color

	# TITLE for the game

	title = TITLE.render("HangMan",1,(0, 0, 0, 0))
	win.blit(title, (WIDTH/1.9 - title.get_width()/2, 10))  # Title in center and then y-axis= 24

	# draw word on the screen
	disp_word = ""
	for letter in words:
		if letter in guessed:
			disp_word += letter + " "

		else:
			disp_word += "_ "

	text = WORD.render(disp_word, 1, (0, 0, 0, 0))
	win.blit(text, (500, 250))

	# buttons at center
	for btn_pos in letters:
		x, y, ltr, visible = btn_pos  # making button visible and invisible after clicKing it

		if visible:
			pygame.draw.circle(win, (0, 0, 0, 0), (x, y), radius, 4)
			txt = font.render(ltr, 1, (0, 0, 0, 0))
			win.blit(txt, (x-txt.get_width()/2, y-txt.get_height()/2))

	win.blit(images[hangman], (50, 50))
	pygame.display.update()


while run:
	clock.tick(FPS)
	draw()

	for event in pygame.event.get():  # Triggering the event
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:

			x_mouse, y_mouse = pygame.mouse.get_pos()
			# print(pos)

			for letter in letters:
				x, y, ltr, visible = letter

				if visible:
					dist = math.sqrt((x - x_mouse) ** 2 + (y - y_mouse) ** 2)

					if dist <= radius:
						letter[3] = False  # to invisible the clicked button
						guessed.append(ltr)
						if ltr not in words:
							hangman += 1

# --------------------------------------------------------------------------------
# deciding if you won the game or not
	won = True
	for letter in words:
		if letter not in guessed:
			won = False
			break

	if won:
		draw()
		pygame.time.delay(1000)
		win.fill((0, 0, 0, 0))
		text = WORD.render("YOU WON", 1, (129, 255, 0, 255))
		win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
		pygame.display.update()
		pygame.time.delay(4000)
		print("WON")
		break

	if hangman == 6:
		draw()
		pygame.time.delay(1000)
		win.fill((0, 0, 0, 0))
		text = WORD.render("YOU LOST", 1, (255, 0, 5, 255))
		answer = WORD.render("The answer is "+words, 1, (129, 255, 0, 0))
		win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
		win.blit(answer, ((WIDTH / 2 - answer.get_width() / 2), (HEIGHT / 2 - text.get_height() / 2)+70))

		pygame.display.update()
		pygame.time.delay(4000)
		print("LOST")
		break


pygame.quit()
