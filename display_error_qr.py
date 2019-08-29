import pygame


pygame.init()

screen = pygame.display.Info()
gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Imprimanta s-a stricat :( ')

counter, text = 20, '20'.rjust(3)
message = 'Problema cu imprimanta :('
message2 = 'Scaneaza QRul ca sa salvezi poza'
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
font_message = pygame.font.SysFont('Consolas', 50)
black = (0,0,0)

crashed = False
carImg = pygame.image.load('error_qr.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))
    gameDisplay.blit(font.render(text, True, (255, 255, 255)), (32, 48))
    gameDisplay.blit(font_message.render(message, True, (255, 255, 255)), (400, 200)) 
    gameDisplay.blit(font_message.render(message2, True, (255, 255, 255)), (360, 240)) 



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
