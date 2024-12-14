import curses

colors = {}
def initialize_colors():
    
    curses.start_color()

    curses.init_color(101, 0, 600, 0)
    curses.init_color(102, 600, 1000, 600)
    curses.init_color(103, 1000, 1000, 400)
    curses.init_color(104, 600, 600, 800)

    curses.init_pair(1, 101, curses.COLOR_BLACK)
    curses.init_pair(2, 102, curses.COLOR_BLACK)
    curses.init_pair(3, 103, curses.COLOR_BLACK)
    curses.init_pair(4, 104, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_RED, curses.COLOR_BLACK)
    
    colors["button_color"] = curses.color_pair(1)
    colors["button_hover_color"] = curses.color_pair(2)
    colors["gold"] = curses.color_pair(3)
    colors["silver"] = curses.color_pair(4)
    colors["white_red"] = curses.color_pair(5)
    colors["white_green"] = curses.color_pair(6)
    colors["green"] = curses.color_pair(7)
    colors["red"] = curses.color_pair(8)