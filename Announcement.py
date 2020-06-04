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
    
    x = 0
    y = 0
    c = 0
    mx = 0
    my = 0
    height, width = stdscr.getmaxyx()
    lenstr = width - 5
    
    stdscr.clear()
    stdscr.addstr(0, width//2 - len(dialog_name)//2, "{}".format(dialog_name))
    stdscr.refresh()
    
    OKButton = Button.CreateButton((width // 2) - 5, height - 5, "OK")
    Painter.PaintButton(stdscr, OKButton)
    rectangle(stdscr, 1, 1, height - 7, width - 2)
    
    for i in text:
        while len(i) != 0 and y + 2 < height - 7:
            if x + 2 > lenstr:
                stdscr.addch(y + 2, x + 2, "-")
                y += 1
                x = 0
            stdscr.addch(y + 2, x + 2, "{}".format(i[0]))
            x += 1
            i = i[1:]
        if x + 2 > lenstr:
            y += 1
            x = 0
        stdscr.addch(y + 2, x + 2, " ")
        x += 1
     
    stdscr.refresh()
    
    while(True):
        event = stdscr.getch()
        if event == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
        if ButtonProcessor.IsButtonPressed(OKButton, mx, my):
            break
    curses.endwin()
            

def main(dialog_name, text):
    curses.wrapper(DrawMenu, dialog_name, text)

if __name__ == "__main__":
    main(dialog_name, text)
	