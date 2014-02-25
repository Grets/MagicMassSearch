
#Author: github.com/Grets
#Title: MagicMassSearch
#URL: github.com/Grets/MagicMassSearch/

import urllib.request
from tkinter import *
from tkinter.filedialog import askopenfilename

class GUI:
    def __init__(self,rootWin):
        self.win = rootWin

        self.fileNameLabel = Label(self.win, text='...', relief=SUNKEN,anchor=W,width=50)
        self.fileNameLabel.grid(row=1,column=2)

        self.fileFindButton = Button(self.win, text='Select Card List File',command=self.getFileName)
        self.fileFindButton.grid(row=1,column=1,sticky=EW)

        self.paramEntryBox = Entry(self.win)
        self.paramEntryBox.grid(row=2,column=2,sticky=EW)

        self.paramEntryLabel = Label(self.win, text='Search URL Parameters:',anchor=E)
        self.paramEntryLabel.grid(row=2,column=1)

        self.runButton = Button(self.win,text='Search for matches',command=self.runSearch,state=DISABLED)
        self.runButton.grid(row=3,column=1,columnspan=2)

    def runSearch(self):
        t = Toplevel()
        t.wm_title("Search Results")

        params = self.paramEntryBox.get()
        params = parseParams(params)
        
        cards = loadCardListFromFile(self.fileName)
        text = Text(t)
        firstLine=True
        for card in cards:
            if(search(card,params)):
                if(not firstLine):
                    text.insert(END,'\n')
                firstLine=False
                text.insert(END,card)
        text.pack()
        return

    def getFileName(self):
        result = askopenfilename()
        if(result != ''):
            self.fileName = result
            self.fileNameLabel.config(text=self.fileName)
            self.runButton.config(state=ACTIVE)

def loadCardListFromFile(name):
    f = open(name, 'r')
    line = f.readline()
    cards = []

    while line != '':
        if(line == '\n'):
            line = f.readline()
            continue
        cards.append(line[line.index('\t')+1 if ('\t' in line) else 0:-1])
        line = f.readline()

    f.close()

    return cards

def search(card,params):
    url = 'http://magiccards.info/'+params+'+'+card.replace(' ','+')+'&v=card&s=cname'
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    text = text.lower()
    results = []
    if(('>' + card.lower() + '<') in text):
        return True
    return False

def parseParams(params):
    params = params[params.index('magiccards.info/')+len('magiccards.info/'):]
    params = params[:len(params)-len('&v=card&s=cname')]
    return params

myWin = Tk()
myWin.wm_title("MTG Mass Search")
myObj = GUI(myWin)
myWin.mainloop()
