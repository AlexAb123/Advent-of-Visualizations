import pygame
from utils.colors import RED, GREEN, BLUE, WHITE
from utils.helpers import complex_to_pos
from pathlib import Path

def simulate_move(move, left_boxes, right_boxes, walls, robot_pos):

    directions = {"^": -1,
                ">": 1j,
                "v": 1,
                "<": -1j}
    d = directions[move]
    displacements = [robot_pos]
    hit_wall = False

    # Because we need to keep track of everything that has ever been in the queue and it's order,
    # we dont actually remove from 'displacements' and instead just increment i.
    # We could also do this with a for loop and just keep adding to displacements, but while loop is more readable
    i = 0
    while i < len(displacements):
        
        pos = displacements[i]
        next_pos = pos+d
        
        if next_pos in walls:
            hit_wall = True
            break
        
        if next_pos in left_boxes and next_pos not in displacements:
            displacements.append(next_pos)
            if next_pos+1j in right_boxes and next_pos+1j not in displacements:
                displacements.append(next_pos+1j)
                
        if next_pos in right_boxes and next_pos not in displacements:
            displacements.append(next_pos)
            if next_pos-1j in left_boxes and next_pos-1j not in displacements:
                displacements.append(next_pos-1j)

        i += 1

    if not hit_wall:
        for displacement in reversed(displacements):
            for boxes in left_boxes, right_boxes:
                if displacement in boxes:
                    boxes.remove(displacement)
                    boxes.add(displacement+d)
            
            if displacement == robot_pos:
                robot_pos = displacement+d
                
    return left_boxes, right_boxes, robot_pos

def draw_grid(screen: pygame.Surface, robot_pos, left_boxes, right_boxes, walls, grid_size):
    CELL_SIZE = min(screen.get_width(), screen.get_height())//grid_size
    CELL_SIZE_TUPLE = (CELL_SIZE, CELL_SIZE)
    CELL_SPACING = 5

    x, y = complex_to_pos(robot_pos*CELL_SIZE)[::-1]
    rect = pygame.Rect((x+CELL_SPACING, y+CELL_SPACING), (CELL_SIZE - CELL_SPACING,)*2)
    pygame.draw.rect(screen, RED, rect)
    for box in left_boxes:

        x, y = complex_to_pos(box*CELL_SIZE)[::-1]
        rect = pygame.Rect((x+CELL_SPACING, y+CELL_SPACING), (CELL_SIZE - CELL_SPACING,)*2)
        pygame.draw.line(screen, BLUE, (rect.left, rect.top), (rect.right, rect.top), 3)
        pygame.draw.line(screen, BLUE, (rect.left, rect.top), (rect.left, rect.bottom), 3)
        pygame.draw.line(screen, BLUE, (rect.left, rect.bottom), (rect.right, rect.bottom), 3)

    for box in right_boxes:
        x, y = complex_to_pos(box*CELL_SIZE)[::-1]
        rect = pygame.Rect((x+CELL_SPACING, y+CELL_SPACING), (CELL_SIZE - CELL_SPACING,)*2)
        pygame.draw.line(screen, BLUE, (rect.left, rect.top), (rect.right, rect.top), 3)
        pygame.draw.line(screen, BLUE, (rect.right, rect.top), (rect.right, rect.bottom), 3)
        pygame.draw.line(screen, BLUE, (rect.left, rect.bottom), (rect.right, rect.bottom), 3)
    for wall in walls:
        x, y = complex_to_pos(wall*CELL_SIZE)[::-1]
        rect = pygame.Rect((x+CELL_SPACING, y+CELL_SPACING), (CELL_SIZE - CELL_SPACING,)*2)
        pygame.draw.rect(screen, WHITE, rect)


def visualize_2024_15(screen: pygame.Surface):
    grid, moves = Path(__file__).with_name('day_15_input.txt').open('r').read().strip().split("\n\n")
    grid = [list(line) for line in grid.split("\n")]
    moves = moves.replace("\n", "")

    walls1, walls2, boxes, left_boxes, right_boxes = set(), set(), set(), set(), set()
    robot_pos1, robot_pos2 = None, None
    for r in range(len(grid)):
        for c in range(len(grid[0])):

            if grid[r][c] == "@":
                robot_pos1 = r+c*1j
                robot_pos2 = r+c*2*1j

            elif grid[r][c] == "O":
                boxes.add(r+c*1j)
                left_boxes.add(r+c*2*1j)
                right_boxes.add(r+(c*2+1)*1j)

            elif grid[r][c] == "#":
                walls1.add(r+c*1j)
                walls2.add(r+c*2*1j)
                walls2.add(r+(c*2+1)*1j)

    draw_grid(screen, robot_pos2, left_boxes, right_boxes, walls2, len(grid)*2)
    pygame.display.flip()


    running = True
    while running:
        move = wait_for_input()
        left_boxes, right_boxes, robot_pos2 = simulate_move(move, left_boxes.copy(), right_boxes.copy(), walls2, robot_pos2)
        draw_grid(screen, robot_pos2, left_boxes, right_boxes, walls2, len(grid)*2)
        pygame.display.flip()
        screen.fill((0,0,0))

def wait_for_input():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    return "^"
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    return ">"
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    return "v"
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    return "<"



def solve():
    grid, moves = Path(__file__).with_name('day_15_input.txt').open('r').read().strip().split("\n\n")
    grid = [list(line) for line in grid.split("\n")]
    moves = moves.replace("\n", "")

    walls1, walls2, boxes, left_boxes, right_boxes = set(), set(), set(), set(), set()
    robot_pos1, robot_pos2 = None, None
    for r in range(len(grid)):
        for c in range(len(grid[0])):

            if grid[r][c] == "@":
                robot_pos1 = r+c*1j
                robot_pos2 = r+c*2*1j

            elif grid[r][c] == "O":
                boxes.add(r+c*1j)
                left_boxes.add(r+c*2*1j)
                right_boxes.add(r+(c*2+1)*1j)

            elif grid[r][c] == "#":
                walls1.add(r+c*1j)
                walls2.add(r+c*2*1j)
                walls2.add(r+(c*2+1)*1j)
    
    directions = {"^": -1,
                ">": 1j,
                "v": 1,
                "<": -1j}
    
    
    
    def simulate_moves(moves, left_boxes, right_boxes, walls, robot_pos):

        for move in moves:

            d = directions[move]
            displacements = [robot_pos]
            hit_wall = False

            # Because we need to keep track of everything that has ever been in the queue and it's order,
            # we dont actually remove from 'displacements' and instead just increment i.
            # We could also do this with a for loop and just keep adding to displacements, but while loop is more readable
            i = 0
            while i < len(displacements):
                
                pos = displacements[i]
                next_pos = pos+d
                
                if next_pos in walls:
                    hit_wall = True
                    break
                
                if next_pos in left_boxes and next_pos not in displacements:
                    displacements.append(next_pos)
                    if next_pos+1j in right_boxes and next_pos+1j not in displacements:
                        displacements.append(next_pos+1j)
                        
                if next_pos in right_boxes and next_pos not in displacements:
                    displacements.append(next_pos)
                    if next_pos-1j in left_boxes and next_pos-1j not in displacements:
                        displacements.append(next_pos-1j)

                i += 1

            if not hit_wall:
                for displacement in reversed(displacements):
                    for boxes in left_boxes, right_boxes:
                        if displacement in boxes:
                            boxes.remove(displacement)
                            boxes.add(displacement+d)
                    
                    if displacement == robot_pos:
                        robot_pos = displacement+d
        score = 0
        for box in left_boxes:
            score += 100 * int(box.real) + int(box.imag)
        return score
    
    part1 = simulate_moves(moves, boxes, set(), walls1, robot_pos1)
    part2 = simulate_moves(moves, left_boxes, right_boxes, walls2, robot_pos2)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")