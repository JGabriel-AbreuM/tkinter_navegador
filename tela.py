from cProfile import label
from doctest import master
from tkinter import *
from selenium import webdriver
from database import Banco_de_Dados

class Navegador:
    def __init__(self, master):
        self.master = master
        self.fontePadrao = ("Arial", "12")
        self.db = Banco_de_Dados()
        self.container = Frame(master)
        self.container["bg"] = "#f2f2f2"
        self.container["padx"] = 100
        self.container["pady"] = 50
        self.container.pack()

        self.botaoContainer = Frame(master)
        self.botaoContainer["pady"] = 20
        self.botaoContainer.pack()

        self.busca = Entry(self.container)
        self.busca["width"] = 50
        self.busca["font"] = self.fontePadrao
        self.busca.pack()

        self.button_busca = Button(self.botaoContainer)
        self.button_busca["text"] = "Buscar"
        self.button_busca["font"] = self.fontePadrao
        self.button_busca["width"] = 12
        self.button_busca["command"] = self.buscar_web
        self.button_busca.pack()


    def buscar_web(self):
        url = self.busca.get()
        self.db.inserirHistorico(url)
        driver = webdriver.chrome.webdriver.WebDriver(executable_path=r"C:\Users\joseg\OneDrive\Documentos\CactusSearch\chromedriver.exe")

        driver.get(f"https://www.google.com/search?q={url}")
        driver.exit()

    def busca_historico(self, item):
        driver = webdriver.chrome.webdriver.WebDriver(executable_path=r"C:\Users\joseg\OneDrive\Documentos\CactusSearch\chromedriver.exe")

        driver.get(f"https://www.google.com/search?q={item}")
        driver.exit()

root = Tk()


largura = root.winfo_screenwidth()
altura = root.winfo_screenheight() 
root.geometry(f"{largura}x{altura}")
root.title("Cactus Search")
root["bg"] = "#f2f2f2"

img = PhotoImage(file="imagens/logo.png")

label_img = Label(root, image=img).pack()

menubar = Menu(root)

historico_menu = Menu(menubar)

nav = Navegador(root)
for c in nav.db.mostrarHistorico():
    historico_menu.add_command(label=c)

menubar.add_cascade(label="Histórico", menu=historico_menu)
root.config(menu=menubar)
root.mainloop()



