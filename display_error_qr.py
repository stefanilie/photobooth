import pygame


pygame.init()

screen = pygame.display.Info()
gameDisplay = pygame.display.set_mode((screen.current_w, screen.current_h))
#gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Imprimanta s-a stricat :( ')

counter, text = 15, '15'.rjust(3)
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
black = (0,0,0)

crashed = False
carImg = pygame.image.load('error_qr.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))
    gameDisplay.blit(font.render(text, True, (0, 0, 0)), (32, 48))


x =  (screen.current_w *0.4)
y = (screen.current_h *0.4)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
            if counter > 0:
                text = str(counter).rjust(3)  
            else:
                 crashed = True
        # if event.type == pygame.QUIT:
        #     crashed = True

    gameDisplay.fill(black)
    car(x,y) 
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
