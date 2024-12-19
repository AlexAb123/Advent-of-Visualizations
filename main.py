import pygame


from utils.colors import BUTTON_COLOR, BUTTON_HOVER_COLOR



#from aoc_2024.day_02 import visualize_2024_02
#from aoc_2024.day_12 import visualize_2024_12
from aoc_2024.day_15 import visualize_2024_15
visualizations_2024 = [visualize_2024_15]
visualizations = {
    2024: visualizations_2024
}
year = 2024

def draw_main_menu():
    pass

def main():

    pygame.init()
    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    visualize_2024_15(screen)

            elif event.type == pygame.QUIT:
                running = False
                
        pygame.display.flip()


if __name__ == "__main__":
    main()