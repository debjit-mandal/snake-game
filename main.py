import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 48)


# Define a function to display the score on the screen
def display_score(score):
    text = score_font.render("Score: " + str(score), True, BLACK)
    window.blit(text, [10, 10])


# Define a function to display the game over message
def display_game_over(score):
    game_over_text = score_font.render("Game Over!", True, RED)
    score_text = font_style.render("Final Score: " + str(score), True, BLACK)
    restart_text = font_style.render("Press R to Play Again", True, BLACK)
    window.blit(game_over_text, [width / 2 - game_over_text.get_width() / 2, height / 3])
    window.blit(score_text, [width / 2 - score_text.get_width() / 2, height / 2])
    window.blit(restart_text, [width / 2 - restart_text.get_width() / 2, height / 2 + 40])


# Define a function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])


# Define the game loop
def game_loop():
    game_over = False
    game_quit = False

    # Set up the snake initial position and direction
    snake_block = 10
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    # Set up the snake body
    snake_list = []
    length_of_snake = 1

    # Set up the initial food position
    food_x = round(random.randrange(0, width - snake_block, 10))
    food_y = round(random.randrange(0, height - snake_block, 10))

    # Set up the game score
    score = 0

    # Game loop
    while not game_quit:

         # Game over loop
        while game_over == True:
            window.fill(BLACK)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again",
                                        True, RED)
            window.blit(message, [width / 6, height / 3])
            display_score(length_of_snake - 1)
            pygame.display.update()

            # Check for events in the game over loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()
        # Check for events in the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check for boundaries and game over conditions
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        window.fill(BLACK)
        pygame.draw.rect(window, RED, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        draw_snake(snake_block, snake_list)
        display_score(score)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block, 10))
            food_y = round(random.randrange(0, height - snake_block, 10))
            length_of_snake += 1
            score += 1

        clock.tick(30)  # Adjust the snake speed here

    pygame.quit()


# Start the game
game_loop()