import curses


class Button:
    X = None
    Y = None
    Height = None
    Width = None
    Label = None


def CreateButton(x, y, label):
    button = Button()
    button.X = x
    button.Y = y
    button.Height = 2
    button.Width = 10
    button.Label = label
    return button
 
 
def CreateMenuButton(x, y, label, j):
    button = Button()
    button.X = x
    button.Y = y
    button.Height = 2
    button.Width = 22
    button.Index = j
    if len(label) > button.Width:
        button.Label = label[0:button.width-3]+"..."
    else:
        button.Label = label
    return button