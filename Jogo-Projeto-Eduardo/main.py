import pygame
import random
import subprocess


pygame.init()

gameDisplay = pygame.display.set_mode((1600, 600))
pygame.display.set_caption('T-Rex Runner')

# Carregue as imagens e defina as variáveis de jogo

# ...

# Defina as opções do menu
menu_principal = True
menu_jogar = False
menu_configs = False
menu_creditos = False

while menu_principal:
    gameDisplay.fill((112, 154, 209))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    if menu_principal:
        # Desenhe as opções do menu principal
        font = pygame.font.Font(None, 36)
        boasvindas_text = font.render("Menu principal", True, (255, 255, 255))
        jogar_text = font.render("1. Jogar", True, (255, 255, 255))
        configs_text = font.render("2. Configs", True, (255, 255, 255))
        creditos_text = font.render("3. Créditos", True, (255, 255, 255))

        gameDisplay.blit(boasvindas_text, (575, 150))
        gameDisplay.blit(jogar_text, (600, 200))
        gameDisplay.blit(configs_text, (600, 250))
        gameDisplay.blit(creditos_text, (600, 300))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            menu_principal = False
            menu_jogar = True
        elif keys[pygame.K_2]:
            menu_principal = False
            menu_configs = True
        elif keys[pygame.K_3]:
            menu_principal = False
            menu_creditos = True

        while menu_jogar:
            gameDisplay.fill((112, 154, 209))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Desenhe as opções para escolher entre "Tsunami", "Tornado" ou "Meteoro"
            font = pygame.font.Font(None, 36)
            jogos_text = font.render("Modos de jogo", True, (255, 255, 255))
            tsunami_text = font.render("1. Tsunami", True, (255, 255, 255))
            tornado_text = font.render("2. Tornado", True, (255, 255, 255))
            meteoro_text = font.render("3. Meteoro", True, (255, 255, 255))
            return_text = font.render("4. Voltar", True, (255, 255, 255))

            gameDisplay.blit(jogos_text, (575, 150))
            gameDisplay.blit(tsunami_text, (600, 200))
            gameDisplay.blit(tornado_text, (600, 250))
            gameDisplay.blit(meteoro_text, (600, 300))
            gameDisplay.blit(return_text, (600, 350))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                subprocess.Popen(["python", "fase_1"])
            elif keys[pygame.K_2]:
                subprocess.Popen(["python", "fase_2"])
            elif keys[pygame.K_3]:
                subprocess.Popen(["python", "fase_3"])
            elif keys[pygame.K_4]:
                menu_jogar = False
                menu_principal = True
            elif keys[pygame.K_ESCAPE]:
                menu_jogar = False
                menu_principal = True

            pygame.display.update()

        while menu_configs:
            gameDisplay.fill((112, 154, 209))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    

            # Conteúdo dos créditos
            font = pygame.font.Font(None, 36)
            creditos_text = font.render("Controles: ", True, (255, 255, 255))
            orientacoes_text = font.render("Pressione SPACE para pular", True, (255, 255, 255))
            # Adicione mais informações sobre os desenvolvedores, música, arte, etc.

            gameDisplay.blit(creditos_text, (600, 100))
            gameDisplay.blit(orientacoes_text, (600, 150))
            # Adicione mais linhas de texto para outras informações de créditos

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                menu_configs = False
                menu_principal = True

            pygame.display.update()

        while menu_creditos:
            gameDisplay.fill((112, 154, 209))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    

            # Conteúdo dos créditos
            font = pygame.font.Font(None, 36)
            creditos_text = font.render("Créditos", True, (255, 255, 255))
            desenvolvedores_text = font.render("Desenvolvido por:", True, (255, 255, 255))
            nome_desenvolvedor_1 = font.render("Nome do Desenvolvedor 1", True, (255, 255, 255))
            nome_desenvolvedor_2 = font.render("Nome do Desenvolvedor 2", True, (255, 255, 255))
            # Adicione mais informações sobre os desenvolvedores, música, arte, etc.

            gameDisplay.blit(creditos_text, (600, 100))
            gameDisplay.blit(desenvolvedores_text, (600, 150))
            gameDisplay.blit(nome_desenvolvedor_1, (600, 200))
            gameDisplay.blit(nome_desenvolvedor_2, (600, 250))
            # Adicione mais linhas de texto para outras informações de créditos

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                menu_creditos = False
                menu_principal = True

            pygame.display.update()

    pygame.display.update()


# Loop principal do jogo (inserir aqui)

pygame.quit()
quit()
