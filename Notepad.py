#We will start this from 20/8/2022 3:00pm
from tkinter import *
import tkinter.messagebox as tmsg
class Notepad(Tk):
    def menu(self):
        MainMenu = Menu(self)
        Menu1 = Menu(MainMenu,tearoff=0)
        Menu2 = Menu(MainMenu,tearoff=0)
        Menu1.add_command(label="New", command=self.new)
        Menu1.add_command(label="Open", command=self.open)
        Menu1.add_command(label="Save", command=self.save)
        Menu1.add_command(label="Save as", command=self.save_as)
        Menu1.add_command(label="Exit", command=self.destroy)

        Menu2.add_command(label="Font", command=self.font)
        Menu2.add_command(label="Size", command=self.ok)
        Menu2.add_command(label="Colour", command=self.ok)

        self.config(menu=MainMenu)
        MainMenu.add_cascade(label="file",menu = Menu1)
        MainMenu.add_cascade(label="format",menu = Menu2)
    
    def screen(self):
        Scroll = Scrollbar(self)
        Scroll.pack(side =RIGHT,fill=Y)
        self.TextScrn = Text(self, yscrollcommand=Scroll.set)
        self.TextScrn.pack(fill=BOTH)
        Scroll.config(command=self.TextScrn.yview)
    
    def open(self):
        root = Tk()
        def opeen():
            global b
            b = self.FileName.get(1.0,"end-1c")
            self.TextScrn.delete(1.0,END)
            file        =  open(f"{b}.txt","r+")
            Afile = file.read()
            self.TextScrn.insert(1.0,Afile)
            #self.TextScrn.configure(font=t1)
            file.close()
            root.destroy()
        Label(root, text="FileName", pady=24, padx=9).grid(row=2, column=1)
        self.FileName = Text(root,width=20,height=1, padx=4,font="Arial 10 bold")
        self.FileName.grid(row =2, column=2, padx=10)
        Button(root, text="Open", command =opeen).grid(row=3, column=2,padx=10,pady=10)
        root.mainloop()
    def save(self):
        root = Tk()
        root.maxsize(310,150)
        root.maxsize(310,150)
        def name():
            Filename    =  Filetext.get(1.0,"end-1c")
            NotepadData =  self.TextScrn.get(1.0,"end-1c")
            file        =  open(f"{Filename}.txt","w")
            file.write(f"{NotepadData}")
            file.close()  
            root.destroy()
        Label(root, text="FileName", pady=24, padx=9).grid(row=2, column=1)
        Filetext =Text(root,width=20,height=1, padx=4,font="Arial 10 bold")
        Filetext.grid(row =2, column=2, padx=10)
        Button(root, text="Save", command =name).grid(row=3, column=2,padx=10,pady=10)
        root.mainloop()
    
    def save_as(self):
        Filename = b
        print(Filename)
        
        NotepadData =  self.TextScrn.get(1.0,"end-1c")
        file        =  open(f"{Filename}.txt","w")
        file.write(f"{NotepadData}")
        file.close()  

    def new(self):
        tmsg.showinfo("Important Info", "If you want to change previous open file data with present one click on 'Save as'")
        tmsg.showinfo("Important Info", "If you want to genrate new file click on 'Save'")
        self.TextScrn.delete(1.0,END)

    def font(self):
        root = Tk()
        Label(root, text="Font").grid(row=1,column=1)
        font = ["Impact",'Jokerman','Latin','Mistral','Modern','Roman','System','Symbol','Tahoma','Algerian','Arial','Calibri','Cambria','Candara','Cooper','Courier','Corbel','Fixedsys','Forte','Georgia','Harrington','Magneto','Elephant','Stencil','Perpetua','Rage','Script','Vivaldi','Webdlings','Wingdings']
        LBX= Listbox(root)
        LBX.grid(row=2,column=1)
        for x in font:LBX.insert(END,x)

        Label(root, text="Size").grid(row=1,column=3)
        LBX2= Listbox(root)
        LBX2.grid(row=2,column=3)
        for m in range(1,75):LBX2.insert(END,m)

        Label(root, text="Style").grid(row=1,column=2)
        style = ["normal", "bold","roman", "italic"]
        LBX1= Listbox(root)
        LBX1.grid(row=2,column=2)
        for m in style:LBX1.insert(END,m)
        global t1
        t =[]
        t1 =t 
        def selected0():
            for i in LBX.curselection():
                global fontvalue
                fontvalue =LBX.get(i)
                print((LBX.get(i)))
            t.append(fontvalue)
        def selected2():
            for i in LBX2.curselection():
                global sizevalue
                sizevalue = LBX2.get(i)
            t.append(sizevalue)
        def selected1():
            for i in LBX1.curselection():
                global stylevalue
                stylevalue =LBX1.get(i)
            t.append(stylevalue)
        def selected3():
            print(t)
            self.TextScrn.configure(font=t)
            t.clear()
            print(t)
        Button(root,text = "Set",command=selected0).grid(row=3,column=1)
        Button(root,text = "Set",command=selected1).grid(row=3,column=2)
        Button(root,text = "Set",command=selected2).grid(row=3,column=3)
        Button(root,text = "Apply",command=selected3).grid(row=4,column=1)
        
        #self.TextScrn.configure(font=t)
        #print(t)
        root.mainloop()
    def ok(self):pass
if __name__ == "__main__":
    window = Notepad()
    window.title("PD-Notepad")
    window.menu()
    window.screen()
    window.mainloop()