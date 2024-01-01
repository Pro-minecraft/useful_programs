from tkinter import *

window = Tk()
window.title("Pro-minecraft Game")
lbl = Label(window, text="Добро пожаловать в игру. Надеемся что она вам понравиться. Чтобы начать "
                         "играть нажмите конопку Play.")
lbl.pack()
canvas = Canvas(window, height=300, width=250)
canvas.pack()
frame = Frame(window, height=300, width=250)
frame.pack()
btn_play = Button(window, text="Play")
btn_play.pack()
window.mainloop()
