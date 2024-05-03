from tkinter import *
from win32com.client import Dispatch
import requests
import json

root = Tk()
root.geometry("666x700")
root.title("PBL PROJECT")
root.config(bg="#4a7a8c",borderwidth=9)
root.maxsize(666,777)

def bolo1():
    def speak(str): 
        speak=Dispatch("SAPI.SpVoice")
        speak.Speak(str)
    if __name__ == '__main__': 
        speak("News for today.. Lets begin")
        url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=26b55d01b5d94a169c14ffde08aa0c10"

        news = requests.get(url).text
        news_dict = json.loads(news)
        arts = news_dict['articles']
        for article in arts:
                speak(article['title'])
                print(article['title'])
                speak("Moving on to the next news..")
            
        speak("Thanks for listening...")        
def bolo2():
    def speak(str): 
        speak=Dispatch("SAPI.SpVoice")
        speak.Speak(str)
    if __name__ == '__main__': 
        speak("Sports News for today.. Lets begin")
        url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=26b55d01b5d94a169c14ffde08aa0c10"

        news = requests.get(url).text
        news_dict = json.loads(news)
        arts = news_dict['articles']
        for article in arts:
                speak(article['title'])
                print(article['title'])
                speak("Moving on to the next news..")
            
        speak("Thanks for listening...") 
def bolo3():
    def speak(str): 
        speak=Dispatch("SAPI.SpVoice")
        speak.Speak(str)
    if __name__ == '__main__':
        speak("Entertainment News for today.. Lets begin")
        url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=26b55d01b5d94a169c14ffde08aa0c10"
        news = requests.get(url).text
        news_dict = json.loads(news)
        arts = news_dict['articles']
        for article in arts:
                speak(article['title'])
                print(article['title'])
                speak("Moving on to the next news..")       
def bolo4():
    def speak(str): 
        speak=Dispatch("SAPI.SpVoice")
        speak.Speak(str)
    if __name__ == '__main__': 
        speak("Business News for today.. Lets begin")
        url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=26b55d01b5d94a169c14ffde08aa0c10"
        news = requests.get(url).text
        news_dict = json.loads(news)
        arts = news_dict['articles']
        for article in arts:
                speak(article['title'])
                print(article['title'])
                speak("Moving on to the next news..")       
f2 = Frame(root,bg="#4a7abc",borderwidth=11,relief=SUNKEN)
f2.pack(side=TOP,fill='x')
l1 = Label(f2,text="WELCOME TO\n NEWS SPEAKING PROGRAM",bg= '#116562',fg='Black',font="Arial 11 bold",borderwidth=1,relief= SOLID)
l1.pack(padx= 5,pady=12)
label_text = Label(text="TO LISTEN THE NEWS CLICK ON SPEAK BUTTON",bg= "#D9D8D7",fg ="blue",font = "Times 13 bold")
label_text.pack( side=TOP,padx=125, pady=34,anchor="w")

label_txt2 = Label(text='Top News in India:',bg='#4a7a8c',fg = 'black',font='Times 17 bold')
label_txt2.pack(side=TOP,padx=6,pady=19,anchor='w')
f1 = Frame(root, borderwidth=6, bg="yellow", relief=SUNKEN)
f1.pack(side='top',anchor="w", pady=1,padx=200)
b1 = Button(f1,fg="black",text='SPEAK',command=bolo1)
b1.pack(side='top',padx=23)

label_txt2 = Label(text='Top Sports News in India:',bg='#4a7a8c',fg = 'black',font='Times 17 bold')
label_txt2.pack(side=TOP,padx=6,pady=19,anchor='w')
f3 = Frame(root, borderwidth=6, bg="yellow", relief=SUNKEN)
f3.pack(side='top',anchor="w", pady=1,padx=200)
b2 = Button(f3,fg="black",text='SPEAK',command=bolo2)
b2.pack(side='top',padx=23)

label_txt3 = Label(text='Top Entertainment News in India:',bg='#4a7a8c',fg = 'black',font='Times 17 bold')
label_txt3.pack(side=TOP,padx=6,pady=19,anchor='w')
f4 = Frame(root, borderwidth=6, bg="yellow", relief=SUNKEN)
f4.pack(side='top',anchor="w", pady=1,padx=200)
b2 = Button(f4,fg="black",text='SPEAK',command=bolo3)
b2.pack(side='top',padx=23)

label_txt4 = Label(text='Top Business News in India:',bg='#4a7a8c',fg = 'black',font='Times 17 bold')
label_txt4.pack(side=TOP,padx=6,pady=19,anchor='w')
f5 = Frame(root, borderwidth=6, bg="yellow", relief=SUNKEN)
f5.pack(side='top',anchor="w", pady=1,padx=200)
b2 = Button(f5,fg="black",text='SPEAK',command=bolo4)
b2.pack(side='top',padx=23)

# widget = Button(root, text = 'Click me please')
# widget.pack()
# widget.bind('<Double-1>',quit)
root.mainloop()