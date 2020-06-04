import curses
import Button
import Painter
import ButtonProcessor
from curses.textpad import rectangle


def DrawMenu(stdscr, dialog_name, text):
    stdscr = curses.initscr()
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
    
    YESButton = Button.CreateButton((width // 3) - 5, height - 5, "YES")
    NOButton = Button.CreateButton((width // 3*2) - 5, height - 5, "NO")
          
    Painter.PaintButton(stdscr, YESButton)
    Painter.PaintButton(stdscr, NOButton)
    
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
            
            if ButtonProcessor.IsButtonPressed(YESButton, mx, my):
                raise SystemExit(3)

            
            if ButtonProcessor.IsButtonPressed(NOButton, mx, my):
               raise SystemExit(4)
            
    curses.endwin()
            

def main(dialog_name, text):
    curses.wrapper(DrawMenu, dialog_name, text)

if __name__ == "__main__":
    main(dialog_name, text)