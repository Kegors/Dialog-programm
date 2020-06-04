import curses
import Button
from curses.textpad import rectangle, Textbox


def PaintButton(stdscr, button):
    rectangle(stdscr, button.Y , button.X, button.Y + button.Height, button.X + button.Width)
    stdscr.addstr(button.Y + button.Height//2, button.X + button.Width//2 - len(button.Label)//2, button.Label)