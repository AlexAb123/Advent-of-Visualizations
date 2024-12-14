import curses
from collections.abc import Callable
from utils.colors import colors

class Button:

    def __init__(self, window: curses.window, row: int, col: int, text: str, function: Callable = lambda x: None):
        self.row = row
        self.col = col
        self.text = text
        self.function = function
        self.window = window
    
    def draw(self, selected: bool):
        self.window.addstr(self.row, self.col, self.text, colors["button_hover_color"] if selected else colors["button_color"])

    def function(self, *args):
        return self.function(*args)
