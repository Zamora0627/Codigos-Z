import pygame
import sys
import random

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego del Cuadrado Móvil")

ccb_img = pygame.image.load("ccb.png")
ccb_img = pygame.transform.scale(ccb_img, (50, 50))
logo_lasalle_img = pygame.image.load("logo_lasalle.png")
logo_lasalle_img = pygame.transform.scale(logo_lasalle_img, (50, 50))

background_color = (0, 0, 0)

square_size = 50
player_speed = 10

projectile_size = 50
projectile_speed = 3
initial_projectile_speed = projectile_speed
projectiles = []

score = 0
font = pygame.font.Font(None, 36)

x = width // 2 - square_size // 2
y = height // 2 - square_size // 2

def create_projectile():
    x = random.randint(0, width - projectile_size)
    y = -projectile_size
    return {"rect": pygame.Rect(x, y, projectile_size, projectile_size), "speed": projectile_speed}

def increase_projectile_speed():
    global projectile_speed
    projectile_speed += 0.5

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= player_speed
    if keys[pygame.K_DOWN]:
        y += player_speed
    if keys[pygame.K_LEFT]:
        x -= player_speed
    if keys[pygame.K_RIGHT]:
        x += player_speed

    if random.randint(0, 100) < 2:
        projectiles.append(create_projectile())

    for projectile in projectiles:
        projectile["rect"].move_ip(0, projectile["speed"])

    projectiles = [p for p in projectiles if p["rect"].top <= height]

    player_rect = pygame.Rect(x, y, square_size, square_size)
    for projectile in projectiles[:]:
        if player_rect.colliderect(projectile["rect"]):
            score += 1
            projectiles.remove(projectile)
            if score % 30 == 0:
                increase_projectile_speed()

    screen.fill(background_color)

    screen.blit(ccb_img, (x, y))

    for projectile in projectiles:
        screen.blit(logo_lasalle_img, projectile["rect"])

    score_text = font.render(f"Puntaje: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()




