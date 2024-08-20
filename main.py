import pygame
import sys
from vector import Vector2
from settings import *

pygame.init()


# SCREEN_WIDTH must be equal to SCREEN_HEIGHT for now
def draw_grid(screen, grid) -> None:
    cell_size = WIDTH / GRID_SIZE
    for i in range(GRID_SIZE):
        pygame.draw.line(screen, WHITE, (i*cell_size, 0), (i*cell_size, HEIGHT)) 
        pygame.draw.line(screen, WHITE, (0, i*cell_size), (WIDTH, i*cell_size)) 
    
    pygame.draw.line(screen, WHITE, (WIDTH - 1, 0), (WIDTH - 1, HEIGHT)) 
    pygame.draw.line(screen, WHITE, (0, HEIGHT - 1), (WIDTH, HEIGHT - 1)) 



def grid_to_world_coords(coords: Vector2) -> Vector2:
    vector = Vector2()
    vector.x = coords.x * WIDTH / GRID_SIZE
    vector.y = coords.y * HEIGHT / GRID_SIZE

    return vector


def draw_player(screen, coords: Vector2) -> None:
    
    world_coords = grid_to_world_coords(coords)
    pygame.draw.circle(screen, RED, (world_coords.x, world_coords.y), RADIUS)



def main() -> None: 
    grid : list(list(int)) = [[0 for i in range(GRID_SIZE)] for i in range(GRID_SIZE)]

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Raycasting Prototype")
    clock = pygame.time.Clock()

    coords = Vector2(3.7, 3.2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit(0)
                   
        screen.fill(BLACK)
        draw_grid(screen, grid)
        draw_player(screen, coords)
        pygame.display.update()
        clock.tick(FPS)
    


if __name__ == "__main__":
    main()
