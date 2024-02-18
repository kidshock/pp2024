import curses

def output_with_curses(stdscr, message):
    stdscr.addstr(message)
    stdscr.refresh()