import curses
import Button
import Painter
import ButtonProcessor
import CleanWindow
from curses.textpad import rectangle


def DrawMenu(stdscr, dialog_name, text):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(1)
    curses.mousemask(1)
    index = 0
    ourstr = ""
    x=2
    y=2
    mx = 0
    my = 0
    height, width = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.addstr(0, width//2 - len(dialog_name)//2, "{}".format(dialog_name))
    stdscr.refresh()
    
    OKButton = Button.CreateButton((width // 2) - 5, height - 5, "OK")
    
    lenstr = width - 5
    
    Painter.PaintButton(stdscr, OKButton)
    
    rectangle(stdscr, 1, 1, height - 7, width - 2)
             
    for i in text:
        ourstr = ourstr + i + " "
    stdscr.refresh()
    
    allstr = ourstr[:lenstr*(height-9)]
    
    for i in range(len(allstr)):
        if x == width - 3:
                    
            stdscr.addch(y, x, "-")
                    
            y += 1
            x = 2
                
        stdscr.addch(y, x, "{}".format(allstr[i]))
                
        x += 1  
    
    while(True):
        x = 2
        y = 2
        event = stdscr.getch()
        if event == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
        if ButtonProcessor.IsButtonPressed(OKButton, mx, my):
            break
            
        if event == curses.KEY_PPAGE and index != 0:
            index -= 1
            allstr = ourstr[lenstr*index: lenstr*index + lenstr*(height-9)]
            CleanWindow.main(stdscr, 2, 2, width - 2, height -7)
            for i in range(len(allstr)):
                if x == width - 3:
                    
                    stdscr.addch(y, x, "-")
                    
                    y += 1
                    x = 2
                
                stdscr.addch(y, x, "{}".format(allstr[i]))
                
                x += 1
            
            
        if event == curses.KEY_NPAGE and len(allstr)>lenstr:
            index += 1
            allstr = ourstr[lenstr*index: lenstr*index + lenstr*(height-9)]
            CleanWindow.main(stdscr, 2, 2, width - 2, height -7)
            for i in range(len(allstr)):
                if x == width - 3:
                    
                    stdscr.addch(y, x, "-")
                    
                    y += 1
                    x = 2
                
                stdscr.addch(y, x, "{}".format(allstr[i]))
                
                x += 1   
    curses.endwin()
            

def main(dialog_name, text):
    curses.wrapper(DrawMenu, dialog_name, text)

if __name__ == "__main__":
    main(dialog_name, text)