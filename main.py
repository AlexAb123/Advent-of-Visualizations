import curses
from utils.colors import initialize_colors
from utils.helpers import create_buttons
from aoc_2024.day_02 import visualize_2024_02
from aoc_2024.day_12 import visualize_2024_12

visualizations_2024 = [visualize_2024_02, visualize_2024_12]
visualizations = {
    2024: visualizations_2024
}
year = 2024


def exit_visualizer():
    curses.endwin()
    exit()



def back(stdscr: curses.window):
    print("HI")
def day_select_screen(stdscr: curses.window):
    selected_button = 0

    stdscr.clear()
    curses.resize_term(20, 20)

    # Initialize buttons
    button_texts = ["[Back]"]
    functions = [back]
    for visualization in visualizations[year]:
        button_texts.append("[Day"+visualization.__name__.split("_")[-1]+"]")
        functions.append(visualization)

    buttons = create_buttons(stdscr, 0, 0, button_texts, functions)

    while True:
        stdscr.clear()
        for i, button in enumerate(buttons):
            button.draw(selected_button==i)

        key = stdscr.getkey().upper()
        if key == "KEY_UP" or key == "W":
            selected_button = (selected_button - 1) % len(buttons)
        elif key == "KEY_DOWN" or key == "S":
            selected_button = (selected_button + 1) % len(buttons)
        elif key == "\n":
            buttons[selected_button].function(stdscr)
        stdscr.refresh()



def main(stdscr: curses.window):
    initialize(stdscr)

    day_select_screen(stdscr)

def initialize(stdscr: curses.window):
    curses.curs_set(0)
    initialize_colors()

curses.wrapper(main)
