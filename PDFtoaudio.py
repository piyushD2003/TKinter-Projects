from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox as tmsg
import os
import threading
from PyPDF2 import*
import pyttsx3
import pdfplumber
class PDFtoMP3(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("454x416")
        self.maxsize(454,496)
        self.minsize(454,496)
        self.title()
    def design(self):
        f1 = Frame(self,borderwidth=1, relief=SUNKEN)
        f1.pack(side = TOP, ipadx=35, pady=20)
        f2 = Frame(self,borderwidth=1)
        f2.pack(side = TOP, anchor=NW)
        f3 = Frame(self,borderwidth=1)
        f3.pack(side = TOP, anchor=NW, pady=15)
        f4 = Frame(self,borderwidth=1)
        f4.pack(side = TOP, anchor=NW, pady=4)
        f5 = Frame(self,borderwidth=1)
        f5.pack(anchor=NW)
        f6 = Frame(self,borderwidth=1)
        f6.pack(anchor=NW)

        Label(f1,text ="Book",padx=34).pack(side = LEFT, pady=34)
        self.bookname = StringVar()
        self.bookname.set("Waiting for your Book ")
        Label(f1,textvariable= self.bookname,padx=104, relief= SUNKEN,width=1,height=2).pack(side = LEFT)
        Button(f1, text="Search",command=self.analyse, height=1,pady=6).pack(side = LEFT)
        self.startvalue = IntVar()
        self.endvalue = IntVar()
    
        Label(f2,text ="Number of Pages", padx=10).pack(side = LEFT, pady=23)
        self.pagenumber = IntVar()
        self.pagenumber.set(" ")
        Label(f2,textvariable= self.pagenumber,padx=24, relief= SUNKEN,width=1,height=2, anchor=W).pack(side = LEFT, ipadx=3)

        Label(f3,text="Enter the Page number You wanted Convert:",padx=10 ).pack(anchor= SW, pady=10)
        Label(f3,text="Starting Page", padx=10).pack(side = LEFT)
        Entry(f3, textvariable=self.startvalue,width= 10,borderwidth=2, relief= SUNKEN).pack(side = LEFT,padx=21, ipady=8)
        Label(f3,text="Ending Page",padx=30).pack(side = LEFT)
        Entry(f3, textvariable=self.endvalue,width= 10,borderwidth=2, relief= SUNKEN).pack(side = LEFT, ipady=8, padx=28)
        
        self.Speedvalue = IntVar()
        self.Voicevalue = IntVar()
        Label(f4,text="Speed of Audio",padx=10).pack(side= LEFT)
        Entry(f4, textvariable=self.Speedvalue,width= 10,borderwidth=2, relief= SUNKEN).pack(side =LEFT, padx=9, ipady=8)
        Label(f4,text="Type of Voice ",padx=10).pack(side= LEFT, padx=34)
        Entry(f4, textvariable=self.Voicevalue,width= 10,borderwidth=2, relief= SUNKEN).pack(side =LEFT, ipady=8)

        Button(f5,text="*see the paramter of speed", font="Corbel 8 normal", fg= "#37474f", relief=FLAT).pack(side = LEFT, padx=10)
        Button(f5,text="*see the type of audio    ", font="Corbel 8 normal", fg= "#37474f", relief=FLAT).pack(side = LEFT, padx=91)

        
        self.CaP= Button(f6,text='Convert and Play', command=self.th).pack(side = LEFT, padx=32, pady=20)
        Button(f6,text="Convert and Save", command= self.th1).pack(side = LEFT, padx=70, pady =20)
    def analyse(self):
        self.book = askopenfilename(defaultextension=".pdf",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        self.bookname.set(os.path.basename(self.book))
        # a = open(self.book,'rb')
        # b = PdfFileReader(a)
        # c = b.numPages
        #self.pagenumber.set(c)
        self.pagenumber.set(f"{(PdfFileReader(open(self.book,'rb'))).numPages}")
    def th(self):
        threading.Thread(target= self.convertandplay).start()
    def th1(self):
        threading.Thread(target= self.convertandsave).start()

    def convertandplay(self):
        c =[]
        window.update()
        for i in range(int(self.startvalue.get()),int(self.endvalue.get())):
            window.update()
            string = pdfplumber.open(self.book).pages[i].extract_text()

            def remove_last_line_from_string(s):return s[:s.rfind('\n')]
            c.append(f"...............................Page Nummber {i}............................")
            string = remove_last_line_from_string(string)
            c.append(string)

        rep = []
        rep1 = []

        for x in c:
            rep.append(x.replace(" ", "  "))
            rep1.append(x.replace("\n", "  "))

        window.update()
        self.engine = pyttsx3.init("sapi5")
        self.engine.setProperty('rate',self.Speedvalue.get())
        self.engine.setProperty('voice',self.engine.getProperty("voices")[self.Voicevalue.get()].id)
        window.update()
        self.engine.say(rep1)
        # engine.save_to_file(rep1,"HP3.mp3")
        self.engine.runAndWait()
    def convertandsave(self):
        c =[]
        window.update()
        for i in range(int(self.startvalue.get()),int(self.endvalue.get())):
            window.update()
            string = pdfplumber.open(self.book).pages[i].extract_text()

            def remove_last_line_from_string(s):return s[:s.rfind('\n')]
            c.append(f"...............................Page Nummber {i}............................")
            string = remove_last_line_from_string(string)
            c.append(string)
        rep = []
        rep1 = []
        for x in c:
            rep.append(x.replace(" ", "   "))
            rep1.append(x.replace("\n", " "))
        window.update()
        self.engine = pyttsx3.init("sapi5")
        self.engine.setProperty('rate',self.Speedvalue.get())
        self.engine.setProperty('voice',self.engine.getProperty("voices")[self.Voicevalue.get()].id)
        window.update()
        a = asksaveasfilename(initialfile='Untitled.mp3',defaultextension=".mp3",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        self.engine.save_to_file(rep1,a)
        self.engine.runAndWait()

if __name__ == "__main__":
    window = PDFtoMP3()
    window.update()
    window.design()
    window.update_idletasks()
    window.mainloop()
    