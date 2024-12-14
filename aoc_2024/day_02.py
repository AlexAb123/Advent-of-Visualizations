from pathlib import Path
import curses
from utils.colors import colors
from time import sleep
from random import shuffle
from utils.button import Button

def visualize_2024_02(stdscr: curses.window):
    stdscr.clear()
    stdscr.refresh()
    back_button = Button(stdscr, 0, 0, "[Back]")


    def safe(report):
        differences = [report[i+1] - report[i] for i in range(len(report)-1)]
        increasing_or_decreasing = report == sorted(report) or report == sorted(report, reverse=True)
        return increasing_or_decreasing and all(1 <= abs(d) <= 3 for d in differences)
    
    lines = [list(map(int, line.split())) for line in Path(__file__).with_name('day_02_input.txt').open('r').read().strip().split("\n")]
    shuffle(lines)


    curses.resize_term(67, 214)

    max_report_width = max(len(" ".join(map(str, report))) for report in lines)

    max_row, max_col = stdscr.getmaxyx()

    pad = curses.newpad(len(lines), max_report_width)

    stdscr.nodelay(True)
    for i, report in enumerate(lines):

        pad.addstr(i, (max_report_width-len(" ".join(map(str, report))))//2, " ".join(map(str, report)))
    pad.refresh(0, 0, 0, max_col//2-max_report_width//2, max_row-1, max_col//2+max_report_width//2)
    
    for i, report in enumerate(lines):

        if safe(report):

            pad.addstr(i, (max_report_width-len(" ".join(map(str, report))))//2, " ".join(map(str, report)), colors["green"])

        else:
            
            pad.addstr(i, (max_report_width-len(" ".join(map(str, report))))//2, " ".join(map(str, report)), colors["red"])
            for j in range(len(report)):
                new_report = report[:j] + report[j+1:]
                if safe(new_report):
                    offset = 1 if j != 0 else 0
                    pad.addstr(i, offset+len(" ".join(map(str, report[:j]))) + (max_report_width-len(" ".join(map(str, report))))//2, str(report[j]), colors["gold"])
                    break
        
        back_button.draw(True)
        pad.refresh((i//max_row)*max_row, 0, 0, max_col//2-max_report_width//2, max_row-1, max_col//2+max_report_width//2)
        key = stdscr.getch()

        if key == ord("\n"):
            pad.clear()
            stdscr.nodelay(False)
            del pad
            return
        sleep(0.02)

    stdscr.nodelay(False)
    key = stdscr.getch()
    if key == ord("\n"):
        pad.clear()
        return