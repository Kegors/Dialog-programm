import curses
import Button
import Painter
import ButtonProcessor
import CleanWindow
from curses.textpad import rectangle


def DrawMenu(stdscr, dialog_name, text):
#In this window we can write and edit our text
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
    
    #Create dialog name
    stdscr.addstr(0, width//2 - len(dialog_name)//2, "{}".format(dialog_name))
    
    stdscr.refresh()
    
    #Create button which will close out window
    OKButton = Button.CreateButton((width // 2) - 5, height - 5, "OK")
    Painter.PaintButton(stdscr, OKButton)
    
    rectangle(stdscr, 1, 1, height - 7, width - 2)#Create window borders
    
    stdscr.refresh()
    
    stdscr.move(cursor_y, cursor_x)#move our cursor to desired coordinates
    
    while(True):
    
        event = stdscr.getch()#press button
         
#Next we will write the keys for our buttons
        if event == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif event == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif event == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif event == curses.KEY_LEFT:
            cursor_x = cursor_x - 1
        
        if cursor_x < 2:#Transition from one line to another then crossing the line
            cursor_x = width - 3
            if cursor_y > 2:
                cursor_y -= 1
        elif cursor_x > width -3:
            cursor_x = 2
            if cursor_y < height -8:
                cursor_y += 1

        cursor_y = max(2, cursor_y)#Borders of our cursor moving
        cursor_y = min(height-8, cursor_y)
        
        stdscr.move(cursor_y, cursor_x)#move our cursor to desired coordinates
        
        if event == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()#mx, my - coordinates of our click
            
            if ButtonProcessor.IsButtonPressed(OKButton, mx, my):#Check are we pressed button or not
                break
        
        if event >= 97 and event <= 126 or event==32:#97 -126 ascii is a-z
            a = ((cursor_y-2)*width+ (cursor_x-2))
            allstr = allstr[:a] + chr(event) + allstr[a:]
            
            cursor_x += 1
            
            CleanWindow.main(stdscr, 2, 2, width - 2, height -7)#Clean our window to rewrite it
            
            x = 2
            y = 2
            
            for i in range(len(allstr)):#Character-by-character recording of our text
            
                if x == width - 3:
                    
                    stdscr.addch(y, x, "-")
                    
                    y += 1
                    x = 2
                
                stdscr.addch(y, x, "{}".format(allstr[i]))
                
                x += 1
            
            stdscr.move(cursor_y, cursor_x)#move our cursor to desired coordinates
            
        if event == curses.KEY_HOME:#Home button key 
            
            cursor_x = 2
            cursor_y = 2
            
            stdscr.move(cursor_y, cursor_x)#move our cursor to desired coordinates
            
        if event == curses.KEY_END:#End button key 
            
            cursor_x = x
            cursor_y = y
            
            stdscr.move(cursor_y, cursor_x)#move our cursor to desired coordinates
            
        if event == curses.KEY_BACKSPACE and (cursor_y != 2 or cursor_x != 2):#Backspace button key 
            
            cursor_x -= 1
            
            a = ((cursor_y-2)*width+ (cursor_x-2))
            allstr = allstr[:a] + allstr[a+1:]
            
            CleanWindow.main(stdscr, 2, 2, width - 2, height -7)#Clean our window to rewrite it
            
            x = 2
            y = 2
            
            for i in range(len(allstr)):#Character-by-character recording of our text
            
                if x == width - 3:
                    
                    stdscr.addch(y, x, "-")
                    
                    y += 1
                    x = 2
                
                stdscr.addch(y, x, "{}".format(allstr[i]))
                
                x += 1
            
            stdscr.move(cursor_y, cursor_x)#move our cursor to desired coordinates
        
        if event == curses.KEY_DC and (cursor_y != height -8 or cursor_x != width - 3):#Delete button key 
            
            a = ((cursor_y-2)*width+ (cursor_x-2))
            allstr = allstr[:a] + allstr[a+1:]
            
            CleanWindow.main(stdscr, 2, 2, width - 2, height -7)#Clean our window to rewrite it
            
            x = 2
            y = 2
            
            for i in range(len(allstr)):#Character-by-character recording of our text
            
                if x == width - 3:
                    
                    stdscr.addch(y, x, "-")
                    
                    y += 1
                    x = 2
                
                stdscr.addch(y, x, "{}".format(allstr[i]))
                
                x += 1
            
            stdscr.move(cursor_y, cursor_x)#move our cursor to desired coordinates


    curses.endwin()
            

def main(dialog_name, text):
    curses.wrapper(DrawMenu, dialog_name, text)

if __name__ == "__main__":
    main(dialog_name, text)