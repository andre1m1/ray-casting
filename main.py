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


def grid_to_world(point: Vector2) -> Vector2:
    return Vector2(point.x * WIDTH / GRID_SIZE, point.y * HEIGHT / GRID_SIZE)


def world_to_grid(point: Vector2) -> Vector2:
    return Vector2(point.x / WIDTH * GRID_SIZE, point.y / HEIGHT * GRID_SIZE)


def draw_point(screen, pos_vector: Vector2) -> None:
    world_coords = grid_to_world(pos_vector)
    pygame.draw.circle(screen, RED, (world_coords.x, world_coords.y), RADIUS)


def draw_line(screen, p1: Vector2, p2: Vector2) -> None:
    pf = grid_to_world(p1)
    pe = grid_to_world(p2) 
    pygame.draw.line(screen, GREEN, (pf.x, pf.y), (pe.x, pe.y))


def main() -> None: 
    grid : list(list(int)) = [[0 for i in range(GRID_SIZE)] for i in range(GRID_SIZE)]

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Raycasting Prototype")
    clock = pygame.time.Clock()

    player = Vector2(3.7, 3.2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                print("Exit succesfully!")
                sys.exit(0)


        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse = Vector2(mouse_x, mouse_y)
        mouse = world_to_grid(mouse)

        if (mouse.x == player.x):
            m = 0
            new_p = Vector2(mouse.x, HEIGHT if mouse.x >= player.x else 0)
        else:
            m = (mouse.y - player.y) / (mouse.x - player.x)
        
            n = mouse.y - m * mouse.x

            new_p = Vector2(x = player.x - mouse.x, y = m*(player.x - mouse.x)+n)



        screen.fill(BLACK)
        draw_grid(screen, grid)
        draw_line(screen, player, mouse)
        draw_line(screen, mouse, new_p)
        draw_point(screen, player)
        draw_point(screen, mouse)
        draw_point(screen, new_p)
        pygame.display.update()
        clock.tick(FPS)
    

if __name__ == "__main__":
    main()


