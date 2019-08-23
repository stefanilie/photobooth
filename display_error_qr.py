import pygame


pygame.init()

infoObject = pygame.display.Info()
gameDisplay = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
#gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Imprimanta s-a stricat :( ')

black = (0,0,0)
white = (255,255,255)

crashed = False
carImg = pygame.image.load('error_qr.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (infoObject.current_w *0.4)
y = (infoObject.current_h *0.4)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(black)
    car(x,y)

        
    pygame.display.update()

pygame.quit()
quit()
