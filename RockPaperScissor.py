from tkinter import *
import random

root= Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Sumit\'s Rock,Paper,Scissor')
root.config(bg='blue')
Label(root,text="Rock,paper,Scissors" ,font='calibri' , bg="cyan").pack()


user_take=StringVar()
Label(root,text="Choose anyone:Rock,Paper,Scissor" ,font='calibri' , bg="yellow").place(x=20,y=70)
Entry(root,font="calibri",text=user_take,bg="antiquewhite2").place(x=90,y=130)


comp_pick=random.randint(1,3)
if comp_pick==1:
    comp_pick='Rock'
elif comp_pick==2:
    comp_pick='Paper'
else:
    comp_pick='Scissor'


Result=StringVar()

def play():
    user_pick=user_take.get()
    if user_pick==comp_pick:
        Result.set("Ohh! tie, you both select same")
    elif user_pick=="Rock" and comp_pick=="Paper":
        Result.set("you loose,computer wins")
    elif user_pick=="Rock" and comp_pick=="Scissor":
        Result.set("you win,computer select scissor")
    elif user_pick=="Paper" and comp_pick=="Rock":
        Result.set("you win,computer select Rock")
    elif user_pick=="Paper" and comp_pick=="Scissor":
        Result.set("you loose,computer select scissor")
    elif user_pick=="Scissor" and comp_pick=="Paper":
        Result.set("you win,computer select paper")
    elif user_pick=="Scissor" and comp_pick=="Rock":
        Result.set("you loose,computer select rock")
    else:
        Result.set("invalid,choose anyone-- rock,paper,scissor")


def reset():
    Result.set("")
    user_take.set("")

def exit():
    root.destroy()



Entry(root,font="calibri",text=Result,bg="antiquewhite2",width=50).place(x=25,y=250)
Button(root,font="calibri",text="PLAY",padx=5,bg="antiquewhite2",command=play).place(x=150,y=190)
Button(root,font="calibri",text="RESET",padx=5,bg="antiquewhite2",command=reset).place(x=70,y=310)
Button(root,font="calibri",text="EXIT",padx=5,bg="antiquewhite2",command=exit).place(x=230,y=310)
root.mainloop()