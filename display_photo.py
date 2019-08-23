import sys
import pygame

def main():
  if len(sys.argv) == 2:
    pygame.init()

    screen = pygame.display.Info()
    gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    counter, text = 15, '15'.rjust(3)
    message = 'Se printeaza poza...'
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    font_message = pygame.font.SysFont('Consolas', 70)
    black = (0,0,0)

    crashed = False
    picture = pygame.image.load(sys.argv[1])
    picture = pygame.transform.scale(picture, (998, 665))
    
    def car(x,y):
        gameDisplay.blit(picture, (x,y))
        gameDisplay.blit(font.render(text, True, (255, 255, 255)), (32, 48))
        gameDisplay.blit(font_message.render(message, True, (255, 255, 255)), (420, 200)) 



    x =  (screen.current_w *0.13)
    y = (screen.current_h *0.3)

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
  else:
      print("Invalid argument count.")
if __name__ == "__main__":
    main()
