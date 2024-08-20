import pygame
import sys
from pygame.math import Vector2

from settings import *

pygame.init()

GRID_SIZE = 5

# SCREEN_WIDTH must be equal to SCREEN_HEIGHT for now
def draw_grid(screen, grid) -> None:
    cell_size = WIDTH / GRID_SIZE
    for i in range(GRID_SIZE):
        pygame.draw.line(screen, WHITE, (i*cell_size, 0), (i*cell_size, HEIGHT)) 
    

    for i in range(GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, i*cell_size), (WIDTH, i*cell_size)) 

    pygame.draw.line(screen, WHITE, (WIDTH - 1, 0), (WIDTH - 1, HEIGHT)) 
    pygame.draw.line(screen, WHITE, (0, HEIGHT - 1), (WIDTH, HEIGHT - 1)) 


def main() -> None:
    
    grid : list(list(int)) = [[0 for i in range(GRID_SIZE)] for i in range(GRID_SIZE)]

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Raycasting Prototype")
    clock = pygame.time.Clock()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit(0)
                   
        
        screen.fill(BLACK)
        draw_grid(screen, grid)
        pygame.display.update()
        clock.tick(FPS)
    


if __name__ == "__main__":
    main()
