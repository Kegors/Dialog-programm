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
    lenstr = width - 5
    
    
    stdscr.clear()
    
    stdscr.addstr(0, width//2 - len(dialog_name)//2, "{}".format(dialog_name))#Create dialog name
    
    stdscr.refresh()
    
    OKButton = Button.CreateButton((width // 2) - 5, height - 5, "OK")#Create button
    
    Painter.PaintButton(stdscr, OKButton)#Draw button
    
    rectangle(stdscr, 1, 1, height - 7, width - 2)#Create window borders
             
    for i in text:
        ourstr = ourstr + i + " "
    stdscr.refresh()
    
    allstr = ourstr[:lenstr*(height-9)]
    
    for i in range(len(allstr)):#Character-by-character recording of our text
        if x == width - 3:
                    
            stdscr.addch(y, x, "-")
                    
            y += 1
            x = 2
                
        stdscr.addch(y, x, "{}".format(allstr[i]))
                
        x += 1  
    
    while(True):
        x = 2
        y = 2
        
        event = stdscr.getch()#press button
        
        if event == curses.KEY_MOUSE:
        
            _, mx, my, _, _ = curses.getmouse()#mx, my - coordinates of our click
            
        if ButtonProcessor.IsButtonPressed(OKButton, mx, my):#Check are we pressed button or not
        
            break
            
        if event == curses.KEY_PPAGE and index != 0:#Page up button key
        
            index -= 1
            allstr = ourstr[lenstr*index: lenstr*index + lenstr*(height-9)]
            
            CleanWindow.main(stdscr, 2, 2, width - 2, height -7)#Clean our window to rewrite it
            
            
            for i in range(len(allstr)):#Character-by-character recording of our text
                if x == width - 3:
                    
                    stdscr.addch(y, x, "-")
                    
                    y += 1
                    x = 2
                
                stdscr.addch(y, x, "{}".format(allstr[i]))
                
                x += 1
            
            
        if event == curses.KEY_NPAGE and len(allstr)>lenstr:#Page down button key
            index += 1
            allstr = ourstr[lenstr*index: lenstr*index + lenstr*(height-9)]
            
            CleanWindow.main(stdscr, 2, 2, width - 2, height -7)#Clean our window to rewrite it
            
            for i in range(len(allstr)):#Character-by-character recording of our text
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