from tkinter import * # import all
import webbrowser
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title('My APP')
root.geometry("640x400+100+100")
root.resizable(False, False)

# APP contants
count = 0

# count
def countUP():
    global count
    count += 1
    label1.config(text=str(count))

# webbrowser to bicbucket ssafyseoul
def bitbucket():
    url = "https://bitbucket.org/ssafy-seoul/python_basic"
    webbrowser.open(url)

# show KOSPI index: scrapping code
def kospi():
    response = requests.get('https://finance.naver.com/sise/').text
    parsed = BeautifulSoup(response, 'html.parser')
    kospi = parsed.select_one('#KOSPI_now').text
    label1.config(text=f'{kospi}') # label1 바꾸겠다
    
# my calculator app
def calculator():
    label1.config(text='calculator')


# Label
label1 = Label(root, text="My first program!")
label1.pack() # 윈도우 안에 배치: pack()

# Button
button1 = Button(root, text="Bitbucket", command=bitbucket)
button1.pack()

button2 = Button(root, text="KOSPI", command=kospi)
button2.pack()

button3 = Button(root, text="Calculator", command=calculator)
button3.pack()

entry1 = Entry(root)
entry1.bind("<Return>", calculator)
entry1.pack()

# Program loop
root.mainloop()
