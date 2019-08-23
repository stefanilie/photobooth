import pygame


pygame.init()

infoObject = pygame.display.Info()
pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

pygame.display.set_caption('Imprimanta s-a stricat :( ')

black = (0,0,0)
white = (255,255,255)

crashed = False
carImg = pygame.image.load('error_qr.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width *0.5)
y = (display_height *0.5)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(black)
    car(x,y)

        
    pygame.display.update()

pygame.quit()
quit()
