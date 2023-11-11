import pygame
import random
import sys

pygame.init()

gameDisplay = pygame.display.set_mode((1600, 600))
pygame.display.set_caption('T-Rex Runner')

player_image = pygame.image.load("sprites_jogo/player.png")
player_image = pygame.transform.scale(player_image, (40, 60))
ground_image = pygame.image.load("sprites_jogo/ground.png").convert()
ground_image = pygame.transform.scale(ground_image, (2600, 190))
obstacle_image = pygame.image.load("sprites_jogo/obstacle.png")
obstacle_image = pygame.transform.scale(obstacle_image, (70, 70))

obstacle_image_jump = pygame.image.load("sprites_jogo/tire.png")
obstacle_image_jump = pygame.transform.scale(obstacle_image_jump, (50, 50))

obstacle_image_ast = pygame.image.load("sprites_jogo/asteroid.png")
obstacle_image_ast = pygame.transform.scale(obstacle_image_ast, (50, 50))

background = pygame.image.load("sprites_jogo/fundo_3.png").convert()
background = pygame.transform.scale(background, (3200, 430))

pygame.mixer.init()
pygame.mixer.music.load("sprites_jogo/musica.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(1)
music_playing = True

player_x = 400
player_y = 400
player_y_change = 0
player_y_limit = 360

ground_x = 0
ground_speed = 8
obstacle_speed = 8
tsunami_x = -1750
tsunami_speed = 10
background_speed = 3
background_x = 0
score = 0

obstacles = []
obstacles_jump = []
obstacles_low = []  #
obstacles_low_speed = []

obstacles_jump_y = 360
obstacles_jump_speed = 2
obstacles_jump_direction = 1


def check_collision(player_x, player_y, obstacles):
    player_rect = pygame.Rect(player_x, player_y, player_image.get_width(), player_image.get_height())
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return True
    return False


game_over = False
game_over_text = None

font = pygame.font.Font(None, 70)
game_over_font = pygame.font.Font(None, 70)

clock = pygame.time.Clock()


def save_score(name, score):
    with open("scores.txt", "a") as file:
        file.write(f"Fase 3 - {name}: {score}\n")


while True:
    gameDisplay.fill((135, 41, 1))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if not game_over:

        score_text = font.render(f"Score: {int(score)}", True, (255, 0, 0))
        score += 0.095

        keys = pygame.key.get_pressed()

        if keys[pygame.K_m] and music_playing == True:
            pygame.mixer.music.stop()
            music_playing = False

        if keys[pygame.K_u] and music_playing == False:
            pygame.mixer.music.play()
            music_playing = True

        if keys[pygame.K_SPACE] and player_y == player_y_limit:
            player_y_change = -18
        if player_y < player_y_limit:
            player_y_change += 0.9
        player_y += player_y_change

        if keys[pygame.K_s] and player_y < player_y_limit:
            player_y_change = +20

        if player_y > player_y_limit:
            player_y = player_y_limit

        ground_x -= ground_speed
        if ground_x <= -1600:
            ground_x = 0

        background_x -= background_speed
        if background_x <= -2600:
            background_x = 1600

        if random.randint(0, 500) < 4:
            obstacles.append(pygame.Rect(1600, 350, obstacle_image.get_width(), obstacle_image.get_height()))

        if random.randint(0, 500) < 2:
            obstacles_jump.append(
                pygame.Rect(1600, obstacles_jump_y, obstacle_image_jump.get_width(), obstacle_image_jump.get_height()))

        if random.randint(0, 500) < 3:
            y = 50
            speed = 7
            obstacles_low.append(pygame.Rect(1600, y, obstacle_image_ast.get_width(), obstacle_image_ast.get_height()))

        for i, obstacle in enumerate(obstacles):
            obstacle.x -= obstacle_speed

        for i, obstacle in enumerate(obstacles_jump):
            obstacle.x -= (obstacle_speed + 2)

        for i, obstacle in enumerate(obstacles_low):
            obstacle.x -= speed
            obstacle.y += random.randint(1, 3)

        if check_collision(player_x, player_y, obstacles):
            game_over = True
            game_over_text = pygame.font.Font(None, 70).render("Game Over", True, (255, 0, 0))

        if check_collision(player_x, player_y, obstacles_jump):
            game_over = True
            game_over_text = pygame.font.Font(None, 70).render("Game Over", True, (255, 0, 0))

        if check_collision(player_x, player_y, obstacles_low):
            game_over = True
            game_over_text = pygame.font.Font(None, 70).render("Game Over", True, (255, 0, 0))

    else:
        tsunami_x += tsunami_speed
        if tsunami_x > 20:
            tsunami_speed = 0

        name = ""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha():
                        name += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif event.key == pygame.K_RETURN:
                        save_score(name, int(score))
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            block = font.render(f"Enter Name: {name}", True, (255, 255, 255))
            game_over = True
            game_over_text = pygame.font.Font(None, 70).render("Game Over", True, (255, 0, 0))
            gameDisplay.blit(game_over_text, (700, 200))
            gameDisplay.blit(block, (700, 300))
            pygame.display.update()

    obstacles_jump_y += obstacles_jump_speed * obstacles_jump_direction
    if obstacles_jump_y < 260:
        obstacles_jump_direction = 1
    if obstacles_jump_y > 370:
        obstacles_jump_direction = -1

    gameDisplay.blit(background, (background_x, 0))
    gameDisplay.blit(ground_image, (ground_x, 410))
    gameDisplay.blit(ground_image, (ground_x + 600, 410))
    gameDisplay.blit(player_image, (player_x, player_y))
    gameDisplay.blit(score_text, (150, 50))

    for i, obstacle in enumerate(obstacles):
        gameDisplay.blit(obstacle_image, (obstacle.x, obstacle.y))

    for i, obstacle in enumerate(obstacles_jump):
        gameDisplay.blit(obstacle_image_jump, (obstacle.x, obstacles_jump_y))

    for i, obstacle in enumerate(obstacles_low):
        gameDisplay.blit(obstacle_image_ast, (obstacle.x, obstacle.y))

    if game_over_text:
        gameDisplay.blit(game_over_text, (700, 200))

    ground_speed += 0.0095
    obstacle_speed += 0.0095

    pygame.display.update()
    clock.tick(60)