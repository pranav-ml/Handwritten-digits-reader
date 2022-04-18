import pygame
import sys

def draw_num():
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    screen.fill((255,255,255))
    col_sq = [[0 for i in range(20)] for j in range(20)]

    pygame.display.set_caption("Drawing Pad")

    for x in range(0,525,25):
        pygame.draw.line(screen,(0,0,0),(x,0),(x,500))
        pygame.display.update()
    for y in range(0,525,25):
        pygame.draw.line(screen,(0,0,0),(0,y),(500,y))
        pygame.display.update()
    loop = True
    press = False
    while loop:

            # pygame.mouse.set_visible(False)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                    return [[col_sq[i][j]] for i in range(19) for j in range(19)]

                    pygame.quit()
            px, py = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()==(1,0,0) and (px-(px%25))/ 25<=19 and (py-(py%25))/ 25<=19:
                pygame.draw.rect(screen, (0,0,0), (px-(px%25), py-(py%25), 25, 25))
                #print(int((px - (px % 25)) / 25), int((py - (py % 25)) / 25))
                col_sq[int((px - (px % 25))/25)][int((py - (py % 25)) / 25)]=1


            pygame.display.update()
    
    
    

