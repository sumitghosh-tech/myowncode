from tkinter import *
import random

root= Tk()
root.geometry('600x600')
root.resizable(0,0)
root.title('Sumit\'s Guessing Game')
root.config(bg='blue')
Label(root,text="Guessing Game" ,font='Georgia' , bg="cyan").pack()

user_take = IntVar()

Result=StringVar()

Label(root, text="Choose any number between 1 and 10", font='Algerian', bg="yellow").place(x=20, y=70)
Entry(root, font="calibri", text=user_take, bg="antiquewhite1").place(x=90, y=130)

l=list()
def shuffle(l):
    l.append(random.randint(1,10))
shuffle(l)
l.append(0)
def play():

    if l[1]==0:
        shuffle(l)
    at = l[0]
    user_pick = user_take.get()
    if at>user_pick:
        Result.set("You guessed too low")
        l[1]=1
    elif at<user_pick:
        Result.set("You guessed too high")
        l[1] = 1
    elif at==user_pick:
        Result.set("You guessed correct,you win!!")
        l[1]=0


def reset():
    Result.set("")
    user_take.set("")

def exit():
    root.destroy()


Entry(root, font="Algerian", text=Result, bg="antiquewhite1").place(x=25, y=250)
Button(root,font="Castellar",text="PLAY",padx=5,bg="antiquewhite2",command=play).place(x=150,y=190)
Button(root,font="Bahnschrift",text="SHUFFLE",padx=5,bg="antiquewhite2",command=shuffle(l)).place(x=250,y=270)

Button(root,font="Elephant",text="RESET",padx=1,bg="antiquewhite2",command=reset).place(x=70,y=310)
Button(root,font="Georgia",text="EXIT",padx=5,bg="antiquewhite2",command=exit).place(x=230,y=310)
root.mainloop()

