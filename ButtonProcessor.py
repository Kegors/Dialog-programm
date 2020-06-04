import Button


def IsButtonPressed(button, x, y):
#Check, is button pressed
    if y >= button.Y and y <= button.Y + button.Height and x >= button.X  and x <= button.X + button.Width:
        return True
    else:
        return False