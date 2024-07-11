import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Font
font = pygame.font.Font(None, 36)

# Game variables
running = True
game_active = False
number_to_guess = 0
guess = 0
attempts = 0
max_attempts = 0
score = 0
high_score = 0
hint = ""
difficulty = "Easy"

# Difficulty settings
difficulty_settings = {
    "Easy": (1, 10, 5),
    "Medium": (1, 50, 7),
    "Hard": (1, 100, 10)
}

# Functions
def start_game(difficulty_level):
    global number_to_guess, attempts, max_attempts, difficulty, game_active, hint, guess
    difficulty = difficulty_level
    number_to_guess = random.randint(*difficulty_settings[difficulty_level][:2])
    attempts = 0
    max_attempts = difficulty_settings[difficulty_level][2]
    game_active = True
    hint = ""
    guess = 0

def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main loop
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif game_active:
                if event.unicode.isdigit():
                    guess = guess * 10 + int(event.unicode)
                elif event.key == pygame.K_RETURN:
                    if guess == number_to_guess:
                        score += max_attempts - attempts
                        high_score = max(high_score, score)
                        hint = f"Correct! The number was {number_to_guess}."
                        game_active = False
                    else:
                        attempts += 1
                        if attempts >= max_attempts:
                            hint = f"Game Over! The number was {number_to_guess}."
                            game_active = False
                        else:
                            if abs(guess - number_to_guess) <= 2:
                                hint = "Very Close!"
                            elif guess > number_to_guess:
                                hint = "Too High!"
                            else:
                                hint = "Too Low!"
                    guess = 0
            else:
                if event.key == pygame.K_1:
                    start_game("Easy")
                elif event.key == pygame.K_2:
                    start_game("Medium")
                elif event.key == pygame.K_3:
                    start_game("Hard")

    if game_active:
        draw_text(f"Attempts: {attempts}/{max_attempts}", 10, 10)
        draw_text(f"Guess the number between {difficulty_settings[difficulty][0]} and {difficulty_settings[difficulty][1]}", 10, 50)
        draw_text(f"Your Guess: {guess}", 10, 90)
        draw_text(hint, 10, 130, RED)
    else:
        draw_text("Press 1 for Easy, 2 for Medium, 3 for Hard", 10, 10)
        draw_text(f"High Score: {high_score}", 10, 50)
        draw_text(f"Score: {score}", 10, 90)
        draw_text(hint, 10, 130, RED)
    
    pygame.display.flip()

pygame.quit()
