import pygame
import time

pygame.init()

# Colors
red = (255, 0, 0)
beige = (251, 235, 173)
blue = (84, 70, 134)

screen_width = 640
screen_height = 480

game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tennis Game")

font = pygame.font.SysFont('monospace', 60)
clock = pygame.time.Clock()

# Ball
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_x_speed = 4
ball_y_speed = 4
ball_radius = 10

# Paddles
paddle1_x, paddle1_y = 10, (screen_height // 2) - 40
paddle2_x, paddle2_y = screen_width - 30, (screen_height // 2) - 40
paddle_width, paddle_height = 15, 80

# Scores
player1_score = 0
player2_score = 0
pygame.mouse.set_visible(0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= 7
    if keys[pygame.K_s] and paddle1_y < screen_height - paddle_height:
        paddle1_y += 7
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= 7
    if keys[pygame.K_DOWN] and paddle2_y < screen_height - paddle_height:
        paddle2_y += 7

    # Ball movement
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= screen_height - ball_radius:
        ball_y_speed = -ball_y_speed

    # Ball collision with paddles
    if (paddle1_x < ball_x < paddle1_x + paddle_width and paddle1_y < ball_y < paddle1_y + paddle_height) or \
            (paddle2_x < ball_x < paddle2_x + paddle_width and paddle2_y < ball_y < paddle2_y + paddle_height):
        ball_x_speed = -ball_x_speed

    # Scoring
    if ball_x <= 0:
        player2_score += 1
        ball_x, ball_y = screen_width // 2, screen_height // 2
        ball_x_speed = -ball_x_speed
    if ball_x >= screen_width:
        player1_score += 1
        ball_x, ball_y = screen_width // 2, screen_height // 2
        ball_x_speed = -ball_x_speed

    # Drawing
    game_window.fill(beige)
    pygame.draw.circle(game_window, red, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(game_window, blue, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(game_window, blue, (paddle2_x, paddle2_y, paddle_width, paddle_height))

    # Display scores
    score_text = font.render(f"{player1_score} - {player2_score}", True, (0, 0, 0))
    game_window.blit(score_text, (screen_width // 2 - 50, 20))

    pygame.display.update()
    clock.tick(40)

pygame.quit()
