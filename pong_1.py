#!/usr/bin/env python3
import pygame
import random

win_width = 1920
win_height = 1080

# Setup
pygame.init()

# Game State
game_start = False
screen = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()
running = True
player1_points = 0
player2_points = 0
font = pygame.font.SysFont("Consolas", 36)

font2 = pygame.font.SysFont("Consolas", 60)
text = font.render(f"Press Enter To Start the Round", True, "white")

# Ball Varibles
ball_position = pygame.Vector2(win_width // 2, win_height // 2)
dt = 0
i = 0
ballDY = 10
ballDX = random.choice([10, -10])
ball_size = 30

# Paddle Position
paddle_height = 250


p1_paddle_position = pygame.Vector2(
    win_width * 2 / 30 - 50, win_height // 2 - paddle_height // 2
)

p2_paddle_position = pygame.Vector2(
    win_width * 28 / 30, win_height // 2 - paddle_height // 2
)


while running:
    # draw
    screen.fill("cyan3")
    screen.fill("cyan4", (0, 0, screen.get_width() // 2, screen.get_height()))
    pygame.draw.circle(
        screen, "cadetblue1", (win_width / 2, win_height / 2), win_height / 6
    )
    pygame.draw.line(screen, "grey", (win_width / 2, 0), (win_width / 2, win_height), 2)
    pygame.draw.circle(screen, "yellow", ball_position, ball_size)
    p1_paddle = pygame.Rect(p1_paddle_position, (50, 250))
    pygame.draw.rect(screen, "white", p1_paddle)
    p2_paddle = pygame.Rect(p2_paddle_position, (50, 250))
    pygame.draw.rect(screen, "white", p2_paddle)

    # Point Counter:
    p1text = font2.render(f"{player1_points}", True, "white")
    p2text = font2.render(f"{player2_points}", True, "white")
    screen.blit(
        p1text,
        (
            win_width * 1 / 8 - p1text.get_width() // 2,
            win_height * 1 / 20 - p1text.get_height() // 2,
        ),
    )
    screen.blit(
        p2text,
        (
            win_width * 7 / 8 - p2text.get_width() // 2,
            win_height * 1 / 20 - p2text.get_height() // 2,
        ),
    )

    # X Closes Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Win Counter and Ball Physics
    if ball_position.x > win_width - ball_size / 2:
        game_start = False
        player1_points += 1
        text = font.render(f"Press Enter To Start the Round", True, "white")

    if ball_position.x < ball_size / 2:
        game_start = False
        player2_points += 1
        text = font.render(f"Press Enter To Start the Round", True, "white")

    if ball_position.y > win_height - ball_size / 2 or ball_position.y < ball_size / 2:
        ballDY = -ballDY

    # Collision
    if ball_position.y in range(
        int(p1_paddle_position.y) - 15, int(p1_paddle_position.y) + paddle_height + 15
    ) and ball_position.x in range(
        int(p1_paddle_position.x), int(p1_paddle_position.x) + 75
    ):
        print("\t\tP1 Hit")
        ballDX = 10
    if ball_position.y in range(
        int(p2_paddle_position.y) - 15, int(p2_paddle_position.y) + paddle_height + 15
    ) and ball_position.x in range(
        int(p2_paddle_position.x) - 15, int(p2_paddle_position.x) + 50
    ):
        print("\t\tP2 Hit")
        ballDX = -10

    # Round Running?
    keys = pygame.key.get_pressed()
    if game_start:
        ball_position.y += ballDY
        ball_position.x += ballDX
        # Input
        if keys[pygame.K_w]:
            p1_paddle_position.y -= 500 * dt
        if keys[pygame.K_s]:
            p1_paddle_position.y += 500 * dt

        if keys[pygame.K_UP]:
            p2_paddle_position.y -= 500 * dt
        if keys[pygame.K_DOWN]:
            p2_paddle_position.y += 500 * dt

    else:
        ball_position = pygame.Vector2(win_width // 2, win_height // 2)
        screen.blit(
            text,
            (
                win_width // 2 - text.get_width() // 2,
                win_height * 1 / 20 - text.get_height() // 2,
            ),
        )
        p1_paddle_position = pygame.Vector2(
            win_width * 1 / 30 - 50, win_height // 2 - 125
        )
        p2_paddle_position = pygame.Vector2(win_width * 29 / 30, win_height // 2 - 125)
        ballDX = -ballDX

        if keys[pygame.K_RETURN]:
            game_start = True

    # Like Ncurses Refresh
    pygame.display.update()
    i += 1
    dt = clock.tick(60) / 1000

pygame.quit()
