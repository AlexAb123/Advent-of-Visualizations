import curses
from utils.button import Button
from collections.abc import Callable

def create_buttons(stdscr: curses.window, start_row: int, col: int, texts: list[str], functions: list[Callable]) -> list[Button]:
    buttons: list[Button] = []
    for i, text in enumerate(texts):
        buttons.append(Button(stdscr, start_row+i, col, text, functions[i]))
    return buttons

def draw_wrapped_text(stdscr, start_row, start_col, text, width, color_pair_id=None):
    for i in range(0, len(text), width):
        stdscr.addstr(start_row + i//width, start_col, text[i:i+width], color_pair_id)

def complex_to_row_col(num):
    return (int(num.real), int(num.imag))

import os
def resize_terminal(rows, cols):
    os.system(f'printf "\\e[8;{rows};{cols}t"')
