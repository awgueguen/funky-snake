import pygame
import random
import time

# global variables ---------------------------------------------------------- #
green = (0, 250, 0)
dark_grey = (30, 30, 30)
white = (200, 200, 200)
orange = (220, 100, 0)
black = (20, 20, 20)
red = (255, 0, 0)
dis_width = 300
dis_height = 400

# variables snake ----------------------------------------------------------- #
snake_move_x = 0
snake_move_y = 0
snake_pos_x = 200
snake_pos_y = 150
snake_size = 1
snake_tail_positions = []

# variables diverses -------------------------------------------------------- #
fruit_pos_x = random.randrange(0, dis_width, 10)
fruit_pos_y = random.randrange(20, dis_height, 10)
speed_inc = 0
score_value = 0
angle = 0
game_over = False
close = False

# time variables ------------------------------------------------------------ #
clock = pygame.time.Clock()
speed = 10

# functions ----------------------------------------------------------------- #
clamp = lambda n, nmin=0, nmax=250: (max(min(nmax, n), nmin))


def foodNotSnake(fruit_pos_x, fruit_pos_y):
    return [fruit_pos_x, fruit_pos_y] not in snake_tail_positions


# particles ----------------------------------------------------------------- #

# pygame setup -------------------------------------------------------------- #
pygame.init()  # affichage de l'écran
pygame.font.init()
pygame.display.set_caption("Funky Snake")  # définir le nom de l'écran
display = pygame.display.set_mode((dis_width, dis_height), 0, 32)

# text setup ---------------------------------------------------------------- #
title_font = pygame.font.SysFont("Arial", 30)
reg_font = pygame.font.SysFont("Arial", 15)

# loop ---------------------------------------------------------------------- #
while not close:
    while game_over is False:
        # starting ---------------------------------------------------------- #

        # backgroung -------------------------------------------------------- #
        display.fill(dark_grey)

        # test -------------------------------------------------------------- #

        # buttons ----------------------------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and\
                            snake_pos_x != -10 and\
                            snake_pos_x != dis_width and\
                            snake_pos_y != 10 and\
                            snake_pos_y != dis_height:
                if event.key == pygame.K_UP:
                    snake_move_x = 0
                    snake_move_y = -10
                elif event.key == pygame.K_DOWN:
                    snake_move_x = 0
                    snake_move_y = 10
                elif event.key == pygame.K_LEFT:
                    snake_move_x = -10
                    snake_move_y = 0
                elif event.key == pygame.K_RIGHT:
                    snake_move_x = 10
                    snake_move_y = 0
            elif event.type == pygame.QUIT:
                close = True
                game_over = True

        # mvt & position ---------------------------------------------------- #
        snake_head_pos = [snake_pos_x, snake_pos_y]
        snake_pos_x += snake_move_x
        snake_pos_y += snake_move_y

        if snake_size > 1:
            snake_tail_positions.append(snake_head_pos)
            if len(snake_tail_positions) >= snake_size:
                del snake_tail_positions[0]

        # fruit event ------------------------------------------------------- #
        if snake_pos_x == fruit_pos_x and snake_pos_y == fruit_pos_y:
            # for i in range(10):
            #     img = pygame.Surface((dis_width, dis_height),
            #                           pygame.SRCALPHA, 32)
            #     pygame.draw.circle(img,
            #                        (random.randrange(0, 255),
            #                         random.randrange(0, 255),
            #                         random.randrange(0, 255),
            #                         50),
            #                        (fruit_pos_x + 5,
            #                         fruit_pos_y + 5),
            #                         i * 10)
            #     display.blit(img, (0,0))
            fruit_not_snake = False
            while not fruit_not_snake:
                fruit_pos_x = random.randrange(0, dis_width, 10)
                fruit_pos_y = random.randrange(20, dis_height, 10)
                fruit_not_snake = foodNotSnake(fruit_pos_x, fruit_pos_y)

            speed_inc += 0.2
            score_value += 1
            snake_size += 1
                    # for i in range(10):
                    #     img = pygame.Surface((dis_width, dis_height),
                    #                           pygame.SRCALPHA, 32)
                    #     pygame.draw.circle(img,
                    #                        (random.randrange(0, 255),
                    #                         random.randrange(0, 255),
                    #                         random.randrange(0, 255),
                    #                         50),
                    #                        (fruit_pos_x + 5,
                    #                         fruit_pos_y + 5),
                    #                         i * 10)
                    #     display.blit(img, (0,0))

        # out of bound event ------------------------------------------------ #
        if snake_pos_x == dis_width:
            snake_pos_x = -10
        elif snake_pos_x == -10:
            snake_pos_x = dis_width
        elif snake_pos_y == dis_height:
            snake_pos_y = 10
        elif snake_pos_y == 10:
            snake_pos_y = dis_height

        # art, kinda -------------------------------------------------------- #
        for j, i in enumerate(snake_tail_positions):
            pygame.draw.rect(display,
                             (clamp(180 - j * 10),
                              clamp(100 + j * 10),
                              clamp(80 - j * 10)),
                             [i[0], i[1], 10, 10],
                             border_radius=2)

        pygame.draw.rect(display,
                         green,
                         [snake_pos_x, snake_pos_y, 10, 10],
                         border_radius=2)

        pygame.draw.rect(display,
                         orange,
                         [fruit_pos_x, fruit_pos_y, 10, 10],
                         width=2,
                         border_radius=5
                         )

        # angle += 6
        # img.set_colorkey((0,0,0))
        # pygame.draw.rect(img, white, (dis_width/2, dis_height/2, 10, 10))
        # display.blit(img, (0, 0))
        # img_copy = pygame.transform.rotate(img, angle).copy()
        # display.blit(img_copy, (0, 0))
        # display.blit(img_copy,
        #              (dis_width/2 - int((img_copy.get_width()) / 2),
        #               dis_height/2 - int(img_copy.get_height() / 2)))

        # score display ----------------------------------------------------- #
        pygame.draw.rect(display,
                         black,
                         [0, 0, dis_width, 20],
                         )
        score = reg_font.render(f'score : {score_value}', True, white)
        score_rect = score.get_rect(center=(dis_width/2, 10))
        display.blit(score, score_rect)

        # game over --------------------------------------------------------- #
        if [snake_pos_x, snake_pos_y] in snake_tail_positions:
            game_over = True

        # update ------------------------------------------------------------ #
        pygame.display.update()
        clock.tick(speed + speed_inc)

    # game over menu -------------------------------------------------------- #
    pygame.display.flip()
    display.fill((230, 230, 230))

    game_over = title_font.render('GAME OVER.', True, orange)
    f_score = reg_font.render(f'SCORE : {score_value}', True, orange)
    restart = reg_font.render('PRESS R TO RESTART.', True, black)
    quit = reg_font.render('PRESS ESC TO QUIT.', True, black)

    game_over_rect = game_over.get_rect(center=(dis_width/2, dis_height/3))
    f_score_rect = f_score.get_rect(center=(dis_width/2, dis_height/3 + 25))
    restart_rect = restart.get_rect(center=(dis_width/2, dis_height/2))
    quit_rect = quit.get_rect(center=(dis_width/2, dis_height/2 + 25))

    display.blit(game_over, game_over_rect)
    display.blit(f_score, f_score_rect)
    display.blit(restart, restart_rect)
    display.blit(quit, quit_rect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            elif event.key == pygame.K_r:
                game_over = False
                snake_size = 1
                snake_tail_positions = []
                speed_inc = 0
                score_value = 0
        elif event.type == pygame.QUIT:
            close = True

quit()  # quitte l'écran actuel
