import pygame
import random
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Ultra")

clock = pygame.time.Clock()

BLACK = (15, 15, 15)
GREEN = (0, 255, 120)
RED = (255, 50, 50)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont("Arial", 30)
big_font = pygame.font.SysFont("Arial", 60)

# ---------- MUSIC ----------
try:
    pygame.mixer.music.load("bg_music.mp3")
    pygame.mixer.music.play(-1)
except:
    print("bg_music.mp3 not found")

# ---------- HIGH SCORE ----------
if not os.path.exists("highscore.txt"):
    with open("highscore.txt", "w") as f:
        f.write("0")

def get_high():
    with open("highscore.txt", "r") as f:
        return int(f.read())

def save_high(score):
    if score > get_high():
        with open("highscore.txt", "w") as f:
            f.write(str(score))

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def start_screen():
    while True:
        screen.fill(BLACK)

        draw_text("SNAKE ULTRA", big_font, GREEN, 190, 180)
        draw_text("Press SPACE To Start", font, WHITE, 260, 300)

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    return True

def game():

    snake = [(200, 200)]
    dx = BLOCK
    dy = 0

    food = (
        random.randrange(0, WIDTH, BLOCK),
        random.randrange(0, HEIGHT, BLOCK)
    )

    bombs = []

    score = 0
    paused = False

    while True:

        speed = 10 + score // 3

        if score > 0 and score % 5 == 0:
            if len(bombs) < 5:
                bombs.append((
                    random.randrange(0, WIDTH, BLOCK),
                    random.randrange(0, HEIGHT, BLOCK)
                ))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return None

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    paused = not paused

                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -BLOCK
                    dy = 0

                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = BLOCK
                    dy = 0

                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -BLOCK

                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = BLOCK

        if paused:
            draw_text("PAUSED", big_font, YELLOW, 260, 250)
            pygame.display.update()
            continue

        head = (snake[0][0] + dx, snake[0][1] + dy)

        if (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in snake
        ):
            return score

        if head in bombs:
            return score

        snake.insert(0, head)

        if head == food:
            score += 1
            food = (
                random.randrange(0, WIDTH, BLOCK),
                random.randrange(0, HEIGHT, BLOCK)
            )
        else:
            snake.pop()

        screen.fill(BLACK)

        pygame.draw.rect(
            screen,
            RED,
            (food[0], food[1], BLOCK, BLOCK)
        )

        for bomb in bombs:
            pygame.draw.rect(
                screen,
                (255, 120, 0),
                (bomb[0], bomb[1], BLOCK, BLOCK)
            )

        for part in snake:
            pygame.draw.rect(
                screen,
                GREEN,
                (part[0], part[1], BLOCK, BLOCK)
            )

        draw_text(f"Score: {score}", font, WHITE, 10, 10)
        draw_text(f"High: {get_high()}", font, YELLOW, 620, 10)

        pygame.display.update()
        clock.tick(speed)

def game_over(score):

    save_high(score)

    while True:

        screen.fill(BLACK)

        draw_text("GAME OVER", big_font, RED, 210, 180)
        draw_text(f"Score: {score}", font, WHITE, 320, 280)
        draw_text(
            f"High Score: {get_high()}",
            font,
            YELLOW,
            260,
            330
        )
        draw_text(
            "R = Restart | Q = Quit",
            font,
            GREEN,
            220,
            420
        )

        pygame.display.update()

        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                pygame.quit()
                return False

#innclosbe is alnf pf an ma, eof oesso pce od 
# hii bro whats ypoy name p
            if e.type == pygame.KEYDOWN:

                if e.key == pygame.K_r:
                    return True

                if e.key == pygame.K_q:
                    pygame.quit()
                    return False

if start_screen():

    while True:

        score = game()

        if score is None:
            break

        if not game_over(score):
            break