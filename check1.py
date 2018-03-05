from tkinter import *

root = Tk()
frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)
btn = Button(frame)
btn1 = Button(frame, bg="red")
Checker = False
blackCheckers=True
whiteCheckers=False





for x in range(8):
    for y in range(8):
        if (x + y) % 2 != 0:
            btn1 = Button(frame, bg="red")
            btn1.grid(row=x, column=y, sticky=N + S + E + W)
        if (x+y) % 2 != 0 and x < 3:
            btn1 = Button(frame, bg="blue")
            btn1.grid(row=x, column=y, sticky=N + S + E + W)
        if (x+y) % 2 !=0 and x == 7:
            btn1 = Button(frame, bg="blue")
            btn1.grid(row=x, column=y, sticky=N + S + E + W)
        if (x + y) % 2 != 0 and x == 6:
            btn1 = Button(frame, bg="blue")
            btn1.grid(row=x, column=y, sticky=N + S + E + W)
        if (x + y) % 2 != 0 and x == 5:
            btn1 = Button(frame, bg="blue")
            btn1.grid(row=x, column=y, sticky=N + S + E + W)









for x in range(8):
    Grid.columnconfigure(frame, x, weight=1)

for y in range(8):
    Grid.rowconfigure(frame, y, weight=1)
root.mainloop()
