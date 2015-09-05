
obic_morse={"a":".-", "b":"-...", "c":"-.-.","d":"-..", "e":".","f":"..-.",
    "g":"--.","h":"....","i":"..", "j":".---", "k":"-.-", "l":".-..","m":"--","n":"-.",
    "o":"---","p":".--.", "q":"--.-", "r":".-.","s":"...","t":"-","u":"..-","v":"...-",
    "w":".--","x":"-..-","y":"-.--","z":"--..", " ":"","0":"-----","1":".----", "2":"..---",
    "3":"...--","4":"....-","5":".....","6":"-....", "7":"--...","8":"---..","\n" :"\n", ":":":",
    "9":"----.",",":",", "?":"?","!":"!" , ">":">", "(":"(", ")":")"}
def inverz(sifra):
    inverz={}
    for j,k in sifra.items():
        inverz[k]=j
    return inverz
morse_obic=inverz(obic_morse)
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog
import os
class Prevedi():
    def __init__(self, zaslon):
        menu=Menu(zaslon)
        zaslon.config(menu=menu)
        file_menu = Menu(menu)
        menu.add_cascade(label="Prevajalnik", menu=file_menu)
        file_menu.add_command(label="Shrani", command=self.shrani)
        file_menu.add_command(label="Odpri", command=self.odpri)
        file_menu.add_command(label="Navodila", command=self.navodila)

        help_menu=Menu(menu)
        menu.add_cascade(label="O Programu", menu=help_menu)
        help_menu.add_command(label="O Programu", command=self.program)

        navodila= Label(zaslon, text= " Pred uporabo si preberite navodila \npod zavihkom prevajalnik-->navodila")
        navodila.grid(row=0, column=0)
        
        self.besedilo= StringVar(zaslon,value=None)
        besedilo=Entry(zaslon, textvariable=self.besedilo)
        besedilo.grid(row=1, column=0) # polje kamor pišeš

        gumb_prevedi_morse=Button(zaslon,text="Prevedi v morsa", command=self.prevedivmorse)
        gumb_prevedi_morse.grid(column=1, row=1) #gumb za prevedi v morsa


        gumb_prevedi_nazaj= Button(zaslon, text="Prevedi iz morsa", command=self.prevediizmorsa)
        gumb_prevedi_nazaj.grid(column=1, row=2)
        
        self.prevedeno="Nisi še nič prevedel" #preveden tekst
        self.prevedeno_besedilo=Label(zaslon, text=self.prevedeno)
        self.prevedeno_besedilo.grid(row=1, column=2)


    def prevedivmorse(self):
        tekst=self.besedilo.get()
        novtekst=""
        for i in tekst:
            i=i.lower()
            if i=="\n":
                novtekst=novtekst+obic_morse[i]
            else:
                if i=="č":
                    i="c"
                    novtekst=novtekst+obic_morse[i]+"/"
                elif i=="š":
                    i="s"
                    novtekst=novtekst+obic_morse[i]+"/"
                elif i=="ž":
                    i="z"
                    novtekst=novtekst+obic_morse[i]+"/"
                elif i=="." or i=="-" or i=="/" or i=="_":
                    novtekst=novtekst
                else:
                    novtekst=novtekst+obic_morse[i]+"/"
                self.prevedeno=novtekst
        self.prevedeno_besedilo.config(text = self.prevedeno)

    def prevediizmorsa(self):
        tekst=self.besedilo.get()
        nov_tekst=""
        isci=tekst.split("/")
        for i in isci:
            nov_tekst=nov_tekst+morse_obic[i]
        self.prevedeno=nov_tekst
        self.prevedeno_besedilo.config(text = self.prevedeno)

    def shrani(self): #shrani vneseno in prevedeno besedilo
        vnes_besedilo=self.besedilo.get()
        prev_besedilo=self.prevedeno
        with open ("shranjen_prevod.txt", "wt", encoding="utf8") as f:
            f.write("Vneseno besedilo:"+"\n")
            for x in vnes_besedilo:
                f.write(str(x))
            f.write("\n"+"Prevedeno besedilo:"+"\n")
            for x in prev_besedilo:
                f.write(str(x))
            messagebox.showinfo("Shranjevajne", "Prevod shranjen")
    def odpri(self):
        ime=tkinter.filedialog.askopenfilename()
        bes=""
        with open (ime,encoding="utf8") as x:
            for f in x:
                bes+=f
        self.besedilo.set(bes)#datoteko, ki jo odpreš, napiše v vnosno polje
    def navodila(self):
        os.startfile("navodila.txt")
    def program(self):
        os.startfile("o_programu.txt")
root= Tk()
Aplikacija=Prevedi(root)
root.wm_title("Prevajalnik")
root.mainloop()

