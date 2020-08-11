from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

root = Tk()
root.title('Paint')

frame_left = Frame(root,width=1000,height=800)
frame_left.grid(row=0,column=0)


frame_right = Frame(root,width=800,height=400)
frame_right.grid(row=0,column=1)

           
def choose():
    try:
        z = colorchooser.askcolor()[1]
        canvas.config(bg=z)
    except:
        print('')
def color(color1):
    global a
    global b
    a = color1
    b = color1

def paint(event):
    try:
        x1,y1 = (event.x-r.get()),(event.y-r.get())
        x2,y2 = (event.x+r.get()),(event.y+r.get())
        canvas.create_oval(x1,y1,x2,y2,fill=a,outline=b)
    except:
        print('')
def close():
    root.destroy()
    

button_red = Button(frame_left,bg="red",width=5,height=2,command=lambda:color("red"))
button_red.grid(row=0,column=0)

button_green = Button(frame_left,bg="green",width=5,height=2,command=lambda:color("green"))
button_green.grid(row=0,column=1)

button_yellow = Button(frame_left,bg="yellow",width=5,height=2,command=lambda:color("yellow"))
button_yellow.grid(row=0,column=2)

button_blue = Button(frame_left,bg="blue",width=5,height=2,command=lambda:color("blue"))
button_blue.grid(row=1,column=0)

button_orange = Button(frame_left,bg="orange",width=5,height=2,command=lambda:color("orange"))
button_orange.grid(row=1,column=1)

button_voilet = Button(frame_left,bg="orchid",width=5,height=2,command=lambda:color("orchid"))
button_voilet.grid(row=1,column=2)

button_canvas = Button(frame_left,text="Canvas",width=14,command=choose,font=('arial',10,'bold'))
button_canvas.grid(row=2,column=0,columnspan=3,pady=20)

button_exit = Button(frame_left,text="Exit",width=14,command=close,font=('arial',10,'bold'))
button_exit.grid(row=4,column=0,columnspan=3,pady=20)

label = Label(frame_left,text="Brush Size",font=('arial',10,'bold'))
label.grid(row=5,column=0,columnspan=3)

r = IntVar()

scale = ttk.Scale(frame_left,from_=0,variable=r,to_=100,orient='horizontal')
scale.grid(row=6,column=0,columnspan=3,pady=10)

canvas = Canvas(frame_right,width=800,height=780)


canvas.grid(row=0,column=1)

canvas.bind("<B1-Motion>",paint)

root.mainloop()
