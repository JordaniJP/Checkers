from Tkinter import *

window=Tk()



def checkerboard(board):
    w=board.winfo_width()
    h=board.winfo_height()
    boxW = w/10
    boxH=h/10
    for row in range(8):
        for col in range(8):
            if (row+col)%2==0:
                board.create_rectangle(col*boxW,row*boxH,(col+1)*boxW,(row+1)*boxH,fill='red')
            




thecanvas = Canvas(window, width=700,height=700)
thecanvas.grid(row=0,column=0)
window.update_idletasks()
checkerboard(thecanvas)
window.mainloop()