import pygame
import random

pygame.init()

gameDisplay = pygame.display.set_mode((1600, 600))
pygame.display.set_caption('T-Rex Runner')

player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (60, 60))
ground_image = pygame.image.load("ground.png")
ground_image = pygame.transform.scale(ground_image, (2600, 190))
obstacle_image = pygame.image.load("obstacle.png")
obstacle_image = pygame.transform.scale(obstacle_image, (40, 60))
tsunami_image = pygame.image.load("tsunami.png")
tsunami_image = pygame.transform.scale(tsunami_image, (2200, 300))
background = pygame.image.load("fundo.png")
background = pygame.transform.scale(background, (3200, 430))


player_x = 400
player_y = 400
player_y_change = 0
player_y_limit = 360

ground_x = 0
ground_speed = 7
obstacle_speed = 7
tsunami_x = -1750
tsunami_speed = 10
background_speed = 3
background_x = 0


obstacles = []

def check_collision(player_x, player_y, obstacles):
    player_rect = pygame.Rect(player_x, player_y, player_image.get_width(), player_image.get_height())
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return True
    return False

game_over = False
game_over_text = None

clock = pygame.time.Clock()

while True:
    gameDisplay.fill((112,154,209))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and player_y == player_y_limit:
            player_y_change = -18
        if player_y < player_y_limit:
            player_y_change += 1.2
        player_y += player_y_change

        if player_y > player_y_limit:
            player_y = player_y_limit

        ground_x -= ground_speed
        if ground_x <= -1600:
            ground_x = 0
            
        background_x -= background_speed
        if background_x <= -2600:
            background_x = 1600

        if random.randint(0, 500) < 5:
            obstacles.append(pygame.Rect(1600, 350, obstacle_image.get_width(), obstacle_image.get_height()))

        for obstacle in obstacles:
            obstacle.x -= obstacle_speed

        if check_collision(player_x, player_y, obstacles):
            game_over = True
            game_over_text = pygame.font.Font(None, 70).render("Game Over", True, (255, 0, 0))

    else:
        tsunami_x += tsunami_speed
        if tsunami_x > 5:
            tsunami_speed = 0
        
  

    
    gameDisplay.blit(background, (background_x, 0))
    gameDisplay.blit(ground_image, (ground_x, 410))
    gameDisplay.blit(ground_image, (ground_x + 600, 410))

    
    
    gameDisplay.blit(player_image, (player_x, player_y))
    

    for obstacle in obstacles:
        gameDisplay.blit(obstacle_image, (obstacle.x, obstacle.y))

    gameDisplay.blit(tsunami_image, (tsunami_x, 120))



    if game_over_text:
        gameDisplay.blit(game_over_text, (700, 200))


    ground_speed += 0.0095
    obstacle_speed += 0.0095

    pygame.display.update()
    clock.tick(60)
