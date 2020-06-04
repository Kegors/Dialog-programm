import Announcement
import YesOrNo
import LineInput
import TextMessage
import DialogMain

 
def main(cmp, dialog_name, text):
#This function will choose type of our dialog 
    if cmp == 's':
        Announcement.main(dialog_name, text)
    elif cmp == 'd':
        YesOrNo.main(dialog_name, text)
    elif cmp == 'p':
        LineInput.main(dialog_name, text)
    elif cmp == 't':
        TextMessage.main(dialog_name, text)
    elif cmp == 'm':
        DialogMain.main(dialog_name, text)
    else:
        raise Exception("wrong args")


if __name__ == "__main__":
    main(cmp, dialog_name, text)