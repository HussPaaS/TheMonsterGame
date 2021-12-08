import curses
import pick

def main(stdscr):
    stdscr.addstr("hello world?\n")
    stdscr.get_wch()

    y, x = stdscr.getyx()
    
    title = "Please 