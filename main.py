import pygame
import random
import subprocess

pygame.init()

gameDisplay = pygame.display.set_mode((1600, 600))
pygame.display.set_caption('T-Rex Runner')

menu_principal = True
menu_jogar = False
menu_rank = False
menu_configs = False
menu_creditos = False

while menu_principal:
    gameDisplay.fill((112, 154, 209))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    if menu_principal:

        font = pygame.font.Font(None, 36)
        boasvindas_text = font.render("Menu principal", True, (255, 255, 255))
        jogar_text = font.render("1. Jogar", True, (255, 255, 255))
        rank_text = font.render("2. Ranking", True, (255, 255, 255))
        configs_text = font.render("3. Configs", True, (255, 255, 255))
        creditos_text = font.render("4. Créditos", True, (255, 255, 255))

        gameDisplay.blit(boasvindas_text, (575, 150))
        gameDisplay.blit(jogar_text, (600, 200))
        gameDisplay.blit(rank_text, (600, 250))
        gameDisplay.blit(configs_text, (600, 300))
        gameDisplay.blit(creditos_text, (600, 350))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            menu_principal = False
            menu_jogar = True
        elif keys[pygame.K_2]:
            menu_principal = False
            menu_rank = True
        elif keys[pygame.K_3]:
            menu_principal = False
            menu_configs = True
        elif keys[pygame.K_4]:
            menu_principal = False
            menu_creditos = True

        while menu_jogar:
            gameDisplay.fill((112, 154, 209))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            font = pygame.font.Font(None, 36)
            jogos_text = font.render("Modos de jogo:", True, (255, 255, 255))
            tsunami_text = font.render("1. Tsunami", True, (255, 255, 255))
            tornado_text = font.render("2. Tornado", True, (255, 255, 255))
            meteoro_text = font.render("3. Meteoro", True, (255, 255, 255))
            iniciar_jogo_text = font.render("Digite uma das opções acima e pressione SPACE para iniciar", True, (255, 255, 255))
            retornar = font.render("Pressione Esc para retornar", True, (255, 255, 255))

            gameDisplay.blit(jogos_text, (575, 150))
            gameDisplay.blit(tsunami_text, (600, 200))
            gameDisplay.blit(tornado_text, (600, 250))
            gameDisplay.blit(meteoro_text, (600, 300))
            gameDisplay.blit(iniciar_jogo_text, (600, 350))
            gameDisplay.blit(retornar, (575, 450))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                selected_game = "fase_1.py"
            elif keys[pygame.K_2]:
                selected_game = "fase_2.py"
            elif keys[pygame.K_3]:
                selected_game = "fase_3.py"
            elif keys[pygame.K_ESCAPE]:
                menu_jogar = False
                menu_principal = True

            if selected_game and keys[pygame.K_SPACE]:
                subprocess.Popen(["python", selected_game])
                selected_game = None 

            pygame.display.update()

        while menu_rank:
            gameDisplay.fill((112, 154, 209))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            font = pygame.font.Font(None, 36)

            def read_scores():
                with open("scores1.txt", "r") as file:
                    scores = [line.strip().split(": ") for line in file]

                scores.sort(key=lambda x: int(x[1]), reverse=True)
                return scores

            def show_ranking():
                gameDisplay.fill((0, 0, 0))
                scores = read_scores()
                y = 100 
                for name, score in scores[:2]: 
                    score_text = font.render(f"{name}: {score}", True, (255, 255, 255))
                    gameDisplay.blit(score_text, (100, y))
                    y += 40

            show_ranking()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                menu_rank = False
                menu_principal = True

            pygame.display.update()

        while menu_configs:
            gameDisplay.fill((112, 154, 209))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            font = pygame.font.Font(None, 36)
            creditos_text = font.render("Controles: ", True, (255, 255, 255))
            orientacoes_text = font.render("Pressione SPACE para pular", True, (255, 255, 255))
            orientacoes_text2 = font.render("Pressione S para cair mais rapido", True, (255, 255, 255))
            orientacoes_text3 = font.render("Pressione M para silenciar o jogo e U para retomar a música", True, (255, 255, 255))

            retornar = font.render("Pressione Esc para retornar", True, (255, 255, 255))

            gameDisplay.blit(creditos_text, (575, 100))
            gameDisplay.blit(orientacoes_text, (575, 150))
            gameDisplay.blit(orientacoes_text2, (575, 200))
            gameDisplay.blit(orientacoes_text3, (575, 250))
            gameDisplay.blit(retornar, (575, 300))

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
                    
            font = pygame.font.Font(None, 36)
            creditos_text = font.render("Créditos", True, (255, 255, 255))
            desenvolvedores_text = font.render("Desenvolvido por:", True, (255, 255, 255))
            nome_desenvolvedor_1 = font.render("Nome do Desenvolvedor 1", True, (255, 255, 255))
            nome_desenvolvedor_2 = font.render("Nome do Desenvolvedor 2", True, (255, 255, 255))
            retornar = font.render("Pressione Esc para retornar", True, (255, 255, 255))

            gameDisplay.blit(creditos_text, (575, 100))
            gameDisplay.blit(desenvolvedores_text, (600, 150))
            gameDisplay.blit(nome_desenvolvedor_1, (600, 200))
            gameDisplay.blit(nome_desenvolvedor_2, (600, 250))
            gameDisplay.blit(retornar, (575, 350))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                menu_creditos = False
                menu_principal = True

            pygame.display.update()

    pygame.display.update()

pygame.quit()
quit()
