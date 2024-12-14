from pathlib import Path
import curses
from utils.button import Button
from utils.helpers import complex_to_row_col
from utils.colors import colors
from time import sleep

from time import sleep
def find_region(pos, grid, visited):
    region = {pos}
    visited.add(pos)
    for adj in pos+1, pos-1, pos+1j, pos-1j:
        if adj in grid and adj not in visited and grid[pos] == grid[adj]:
            region |= find_region(adj, grid, visited)
    return region

def region_perimeter(region):
    perimeter = set()
    for pos in region:
        for adj in pos+1, pos-1, pos+1j, pos-1j:
            if adj not in region:
                perimeter.add((pos, adj-pos))
    return perimeter

def region_sides(perimeter):
    return len(perimeter - {(pos+d*1j, d) for pos, d in perimeter})

def visualize_2024_12(stdscr: curses.window):
    stdscr.clear()
    stdscr.refresh()
    back_button = Button(stdscr, 0, 0, "[Back]")

    lines = Path(__file__).with_name('day_12_input.txt').open('r').read().strip().split("\n")
    grid = {r+c*1j: lines[r][c] for c in range(len(lines[0])) for r in range(len(lines))}
    curses.resizeterm(len(lines), len(lines[0])+10)
    stdscr.refresh()

    window = curses.newwin(len(lines), len(lines[0])+10, 0, 10)
    
    visited = set()
    regions = []
    for pos in grid:
        if pos in visited:
            continue
        region = find_region(pos, grid, visited)
        perimeter = region_perimeter(region)
        regions.append((region, grid[pos], len(region), perimeter, region_sides(perimeter)))
    
    content = [["" for _ in range(len(lines[0]))] for _ in range(len(lines))]
    for region in regions:
        for pos in region[0]:
            row, col = complex_to_row_col(pos)
            content[row][col] = "#"
            window.addstr(row, col, "#", colors["button_hover_color"])
        for pos, _ in region[3]:
            row, col = complex_to_row_col(pos)
            content[row][col] = "."
            window.addstr(row, col, ".", colors["button_color"]) 
        window.refresh()

    html_content = "\n".join("".join(line) for line in content)
    with open("index.html", "w") as file:
        file.write(html_content)
    sleep(3)

