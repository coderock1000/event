from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry('250x250')

def msg():
    messagebox.showwarning('Alert', 'stop virus found')
btn = Button(window, text = 'scan for virus', command = msg)
btn.place(x = 40, y = 80)

window.mainloop()