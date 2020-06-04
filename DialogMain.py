import curses
import Button
import Painter
import ButtonProcessor
from curses.textpad import rectangle


def DrawMenu(stdscr, dialog_name, text):

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    curses.mousemask(1)

    j = 0
    mx = 0
    my = 0
    
    height, width = stdscr.getmaxyx()
    
    stdscr.clear()

    stdscr.addstr(0, width//2 - len(dialog_name)//2, "{}".format(dialog_name))
    
    stdscr.refresh()

    buttonarr = []
    
    for i in text:
        j += 1
        buttonarr.append(Button.CreateMenuButton((width // 2) - 11, 4*j , i, j))

    for i in range(j):
        Painter.PaintButton(stdscr, buttonarr[i])
    
    while(True):
        event = stdscr.getch()
        if event == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
        for i in range(j):
            if ButtonProcessor.IsButtonPressed(buttonarr[i], mx, my):
                raise SystemExit(2+i)
    curses.endwin()
            

def main(dialog_name, text):
    curses.wrapper(DrawMenu, dialog_name, text)

if __name__ == "__main__":
    main(dialog_name, text)