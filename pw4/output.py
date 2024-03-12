import curses

def init_screen():
    return curses.initscr()

def print_menu(stdscr):
    stdscr.addstr("1. Input student info\n")
    stdscr.addstr("2. Input course info\n")
    stdscr.addstr("3. Input mark\n")
    stdscr.addstr("4. List students\n")
    stdscr.addstr("5. List courses\n")
    stdscr.addstr("6. List marks\n")
    stdscr.addstr("7. Exit\n")
    stdscr.refresh()

def end_screen():
    curses.endwin()
