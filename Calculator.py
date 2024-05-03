from tkinter import*

class Calculator(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("254x216")
        self.maxsize(254,216)
        self.minsize(254,216)
        self.title("PD Calculator")
    def menu(self):
        self.MainMenu = Menu(self)
        self.Menu1 = Menu(self.MainMenu,tearoff=0)
        self.Menu1.add_command(label="History", command=self.history)
        self.config(menu=self.MainMenu)
        self.MainMenu.add_cascade(label="file",menu = self.Menu1)
    def screen(self):
        f1 = Frame(self,bg="#1a237e",borderwidth=1,relief=SUNKEN)
        f1.pack(side = TOP,fill=X)
        self.scvalue = StringVar()
        self.scvalue.set("")
        self.Scrn = Entry(f1,bg="#1a237e", textvariable=self.scvalue,fg="#18ffff",font= "Arial 11 bold")
        self.Scrn.pack(fill=X,ipady=20)
    def buttons(self):
        f2 = Frame(self,borderwidth=1,relief=SUNKEN)
        f2.pack(side = TOP, anchor=NW)
        f3 = Frame(self,borderwidth=1,relief=SUNKEN)
        f3.pack(side = TOP, anchor=NW)
        f4 = Frame(self,borderwidth=1,relief=SUNKEN)
        f4.pack(side = TOP, anchor=NW)
        f5 = Frame(self,borderwidth=1,relief=SUNKEN,bg="#455a64")
        f5.pack(side=RIGHT)

        Button(f2,text="1",command=self.One,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", padx=20, pady=6).pack(side = LEFT)
        Button(f2,text="2",command=self.Two,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", padx=20, pady=6).pack(side = LEFT)
        Button(f2,text="3",command=self.Three,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", padx=20, pady=6).pack(side = LEFT)
        Button(f2,text="=",command=self.Equalto,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", padx=20, pady=6).pack(side = LEFT)
        Button(f2,text="AC",command=self.AC, padx=20,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", pady=6).pack(side = LEFT)

        Button(f3,text="4",command=self.Four,bg="#37477f",fg="#18ffff",font= "Arial 9 bold",padx=20, pady=6).pack(side = LEFT)
        Button(f3,text="5",command=self.Five,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", padx=20, pady=6).pack(side = LEFT)
        Button(f3,text="6",command=self.Six,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", padx=20, pady=6).pack(side = LEFT)
        Button(f3,text="+",command=self.Add, padx=14,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", pady=6).pack(side = LEFT)
        Button(f3,text="-",command=self.Minus, padx=20,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", pady=6).pack(side = LEFT)
        
        Button(f4,text="7",command=self.Seven,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", padx=20, pady=6).pack(side = LEFT)
        Button(f4,text="8",command=self.Eight,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", padx=20, pady=6).pack(side = LEFT)
        Button(f4,text="9",command=self.Nine,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", padx=20, pady=6).pack(side = LEFT)
        Button(f4,text="x", padx=14,command=self.Multi,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", pady=6).pack(side = LEFT)
        Button(f4,text="/",command=self.Divide, padx=20,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", pady=6).pack(side = LEFT)

        Button(f5,text="0",command=self.Zero,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", padx=20, pady=6).pack(side = LEFT)
        Button(f5,text="DEL",command=self.DEL,bg="#37477f",fg="#18ffff",font= "Arial 9 bold", padx=20, pady=6).pack(side = RIGHT, padx=64)

    def One(self):
        self.scvalue.set(self.scvalue.get()+"1")
    def Two(self):
        self.scvalue.set(self.scvalue.get()+"2")
    def Three(self):
        self.scvalue.set(self.scvalue.get()+"3")
    def Four(self):
        self.scvalue.set(self.scvalue.get()+"4")
    def Five(self):
        self.scvalue.set(self.scvalue.get()+"5")
    def Six(self):
        self.scvalue.set(self.scvalue.get()+"6")
    def Seven(self):
        self.scvalue.set(self.scvalue.get()+"7")
    def Eight(self):
        self.scvalue.set(self.scvalue.get()+"8")
    def Nine(self):
        self.scvalue.set(self.scvalue.get()+"9")
    def Zero(self):
        self.scvalue.set(self.scvalue.get()+"0")
    def AC(self):
        self.scvalue.set("")
    def DEL(self):
        self.scvalue.set(self.Scrn.get()[:-1])
    def Add(self):
        self.scvalue.set(self.scvalue.get()+"+")
    def Minus(self):
        self.scvalue.set(self.scvalue.get()+"-")
    def Multi(self):
        self.scvalue.set(self.scvalue.get()+"*")
    def Divide(self):
        self.scvalue.set(self.scvalue.get()+"/")
    def Equalto(self):
            if self.scvalue.get().isdigit():
                self.value = int(self.scvalue.get())
            else:
                trial = open("Calculations.txt", 'a')
                trial.write(str(self.scvalue.get()))
                self.value = eval(self.scvalue.get())
                trial.write(f"={str(self.value)}\n")
                trial.close()
            self.result = self.scvalue.set(self.value)
            self.Scrn.update()
    
    def clear(self):
        self.trial = open("Calculations.txt","w")
        self.trial.write("")
        self.trial.close()

    def history(self):
        root = Tk()
        root.title("History")
        root.maxsize(194,196)
        root.minsize(194,196)
        LBX =Listbox(root,bg="#0a151a",fg="yellow", width=50)
        LBX.grid()
        self.trial = open("Calculations.txt","r")
        for x in self.trial:
            LBX.insert(END,x)
        self.trial.close()
        root.mainloop()
if __name__ == "__main__":
    window = Calculator()
    window.menu()
    window.screen()
    window.buttons()
    window.mainloop()