import curses
import Button
import Painter
import ButtonProcessor
import CleanWindow
from curses.textpad import rectangle


def DrawMenu(stdscr, dialog_name, text):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(1)
    curses.mousemask(1)
    
    cursor_x = 2
    cursor_y = 2
    mx = 0
    my = 0
    allstr = ""
    height, width = stdscr.getmaxyx()
    lenstr = width - 5
    
    stdscr.clear()
    
    stdscr.addstr(0, width//2 - len(dialog_name)//2, "{}".format(dialog_name))
    
    stdscr.refresh()
    
    OKButton = Button.CreateButton((width // 2) - 5, height - 5, "OK")
    Painter.PaintButton(stdscr, OKButton)
    
    rectangle(stdscr, 1, 1, height - 7, width - 2)
    
    stdscr.refresh()
    
    stdscr.move(cursor_y, cursor_x)
    
    while(True):
        event = stdscr.getch()
         
        if event == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif event == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif event == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif event == curses.KEY_LEFT:
            cursor_x = cursor_x - 1
        
        if cursor_x < 2:
            cursor_x = width - 3
            if cursor_y > 2:
                cursor_y -= 1
        elif cursor_x > width -3:
            cursor_x = 2
            if cursor_y < height -8:
                cursor_y += 1

        cursor_y = max(2, cursor_y)
        cursor_y = min(height-8, cursor_y)
        
        stdscr.move(cursor_y, cursor_x)
        
        #stdscr.addstr(height-1, 0, "{} {}".format(cursor_x, cursor_y))
        
        if event == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
        if ButtonProcessor.IsButtonPressed(OKButton, mx, my):
            break
        
        if event >= 97 and event <= 126 or event==32:
            a = ((cursor_y-2)*width+ (cursor_x-2))
            allstr = allstr[:a] + chr(event) + allstr[a:]
            
            cursor_x += 1
            
            CleanWindow.main(stdscr, 2, 2, width - 2, height -7)
            
            x = 2
            y = 2
            
            for i in range(len(allstr)):
                if x == width - 3:
                    
                    stdscr.addch(y, x, "-")
                    
                    y += 1
                    x = 2
                
                stdscr.addch(y, x, "{}".format(allstr[i]))
                
                x += 1
            
            stdscr.move(cursor_y, cursor_x)
            
        if event == curses.KEY_HOME:
            
            cursor_x = 2
            cursor_y = 2
            
            stdscr.move(cursor_y, cursor_x)
            
        if event == curses.KEY_END:
            
            cursor_x = x
            cursor_y = y
            
            stdscr.move(cursor_y, cursor_x)
            
        if event == curses.KEY_BACKSPACE and (cursor_y != 2 or cursor_x != 2): 
            
            cursor_x -= 1
            
            a = ((cursor_y-2)*width+ (cursor_x-2))
            allstr = allstr[:a] + allstr[a+1:]
            
            CleanWindow.main(stdscr, 2, 2, width - 2, height -7)
            
            x = 2
            y = 2
            
            for i in range(len(allstr)):
                if x == width - 3:
                    
                    stdscr.addch(y, x, "-")
                    
                    y += 1
                    x = 2
                
                stdscr.addch(y, x, "{}".format(allstr[i]))
                
                x += 1
            
            stdscr.move(cursor_y, cursor_x)
        
        if event == curses.KEY_DC and (cursor_y != height -8 or cursor_x != width - 3): 
            
            a = ((cursor_y-2)*width+ (cursor_x-2))
            allstr = allstr[:a] + allstr[a+1:]
            
            CleanWindow.main(stdscr, 2, 2, width - 2, height -7)
            
            x = 2
            y = 2
            
            for i in range(len(allstr)):
                if x == width - 3:
                    
                    stdscr.addch(y, x, "-")
                    
                    y += 1
                    x = 2
                
                stdscr.addch(y, x, "{}".format(allstr[i]))
                
                x += 1
            
            stdscr.move(cursor_y, cursor_x)


    curses.endwin()
            

def main(dialog_name, text):
    curses.wrapper(DrawMenu, dialog_name, text)

if __name__ == "__main__":
    main(dialog_name, text)