import curses
from enum import Enum
from typing import Tuple

menu = ["Monitoring", "Adaptation", "Topologie", "Mode auto."]
row = 0
color = 1

class Action(Enum):
    NONE = 0
    SELECT = 1
    QUIT = 2

def user_input(stdscr, action)-> Tuple[Action, int]:
    # Get user input
    key = stdscr.getch()
    global row

    if action == Action.NONE:
        if key == curses.KEY_UP and row > 0:
            row -= 1
        elif key == curses.KEY_DOWN and row < len(menu) - 1:
            row += 1
        # ENTER key
        elif key in [10, 13]:
            return Action.SELECT, row
    
    # ESCAPE Key
    if key == 27:
        return Action.QUIT, 0
    
    return action, row

def display(stdscr):
    global row, color

    # Display menu
    for id, item in enumerate(menu):
        if id == row:
            stdscr.addstr(item+"\n", curses.color_pair(color))
        else:
            stdscr.addstr(item+"\n")
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    global color
    action = Action.NONE

    while True:
        stdscr.clear()
        display(stdscr)
        newaction, value = user_input(stdscr, action)
        action = newaction
        if action == Action.QUIT:
            break
        elif action == Action.SELECT:
            color = 2

curses.wrapper(main)
