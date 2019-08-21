import pygame


pygame.init()


display_width = 1200
display_height = 900

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Imprimanta s-a stricat :( ')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
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
    clock.tick(5)

pygame.quit()
quit()
