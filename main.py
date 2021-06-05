from tkinter import *
from random import randint

app = Tk()
#ikonka
img = Image("photo", file="fairy.png")
app.tk.call('wm','iconphoto',app._w, img)
app.title('Generator cytatów motywacyjnych !')
app.geometry("800x500")

#funkcja wybierajaca cytat na dzis
def pick():

    #pobieranie z pliku txt cytatow
    f_file = open("cytaty.txt", 'r')
    content = []
    content = f_file.readlines()

    #sprawdzanie ilosci cytatow w liscie, zaczyna od 0
    num_of_quo = len(content) - 1

    #losowanie liczby w zaleznosci od ilosci cytatow
    rando = randint(0, num_of_quo)
    winnerLabel = Label(app, text= content[rando])
    winnerLabel.pack(pady=50)
    return rando

topLabel = Label(app, text="Cytat na dziś! ", font=("Helvetica", 24))
topLabel.pack(pady=20)

losButton = Button(app, text="Wylosuj cytat", font=("Helvetica", 24), command=pick)
losButton.pack(pady=20)

app.mainloop()