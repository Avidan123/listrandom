from tkinter import *
import random
root=Tk()
root.title("list")
root.geometry("400x400")

rand=Label(root,text="list of random numbers: ")
rand.place(relx=0.5,rely=0.5,anchor=CENTER)

rand_sort=Label(root,text="list of sorted numbers : ")
rand_sort.place(relx=0.5,rely=0.6,anchor=CENTER)




def randomlist():
    random_numbers=random.sample(range(1,60),10)
    rand["text"]=rand["text"]+str(random_numbers)
    
    random_numbers.sort()
    rand_sort["text"]=rand_sort["text"]+str(random_numbers)

b=Button(root,text="generate random list",command=randomlist)
b.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()