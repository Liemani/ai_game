import pygame
import sys
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snake Game')

    game = Game(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    game.change_direction('UP')
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    game.change_direction('DOWN')
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    game.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    game.change_direction('RIGHT')

        game.update()
        game.render()
        pygame.display.flip()

if __name__ == '__main__':
    main()