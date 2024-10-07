from tkinter import *
window = Tk()
window.title('event handler')
window.geometry('100x100')

def handle_keypress(event):
    print(event.char)
window.bind('<Key>', handle_keypress)
def handle_click(event):
    print('\n the button was clicked')
btn = Button(text='click me')

btn.pack()
btn.bind('<Button-1>', handle_click)

window.mainloop()