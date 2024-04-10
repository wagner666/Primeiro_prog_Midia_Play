from tkinter import ACTIVE, END, LEFT, NSEW, RAISED, RIDGE, SINGLE, Button, Image, Label, Listbox, Scrollbar, Tk, Frame
from PIL import ImageTk, Image
import pygame
from pygame import mixer
import os

#cores
co0 = "#f0f3f5" # cinzeta / grey
co1 = "#feffff" # branca
co2 = "#3fb5a3" # verde
co3 = "#2e2d2c" # preta / black
co4 = "#403d3d" # preta / black
co5 = "#4a88e8" # azul / blue

# criar janela
janela = Tk()
janela.title("")
janela.geometry('352x255')
janela.resizable(width=False, height=False)

# frames
frame_esquerdo = Frame(janela, width=150, height=150, bg=co3)
frame_esquerdo.grid(row=0, column=0, pady=1, padx=1, sticky="nsew")

frame_direita = Frame(janela, width=150, height=150, bg=co3)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky="nsew")

frame_baixo = Frame(janela, width=404, height=100, bg=co3)
frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky="nsew")

# configurando o frame esquerdo
img_1 = Image.open('1.png')
img_1 = img_1.resize((130,130))  # Correção na dimensão passada para o método resize
img_1 = ImageTk.PhotoImage(img_1)

l_logo = Label(frame_esquerdo, height=130, image=img_1, compound=LEFT, padx=10, anchor='nw', bg=co3, fg=co3)
l_logo.place(x=14, y=15)

# criando funçoes


# tocar musica
def play_musica():
    rodando = listabox.get(ACTIVE)
    l_rodando['text'] = rodando
    mixer.music.load(rodando)
    mixer.music.play()

# pausar musica
def pausar_musica():
    mixer.music.pause()

# continuar musica
def continuar_musica():
    mixer.music.unpause()

# para musica
def para_musica():
    mixer.music.stop() 

# proxima musica
def proxima_musica():
    tocando = l_rodando['text']
    index = musicas.index(tocando)

    novo_index = index + 1

    tocando = musicas[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()

    # deletando so elementos na playlista
    listabox.delete(0,END)

    mostrar()

    listabox.select_set(novo_index)
    listabox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando

# musica anterior
def anterior_musica():
    tocando = l_rodando['text']
    index = musicas.index(tocando)

    novo_index = index - 1

    tocando = musicas[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()

    # deletando so elementos na playlista
    listabox.delete(0,END)

    mostrar()

    listabox.select_set(novo_index)
    listabox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando




# configirando o frame direito
listabox = Listbox(frame_direita, width=22, height=10, selectmode=SINGLE, font=('areal 9 bold'), bg=co3, fg=co1)
listabox.grid(row=0, column=0)

s = Scrollbar(frame_direita)
s.grid(row=0, column=1, sticky=NSEW)

listabox.config(yscrollcommand= s.set)
s.config(command=listabox.yview)

# configurando frame baixo
l_rodando = Label(frame_baixo, text='Escolha música na lista', width=44, justify=LEFT, anchor='nw', font=('ivy 10'), bg=co1, fg=co4)
l_rodando.place(x=0, y=1)

img_2 = Image.open('2.png')
img_2 = img_2.resize((30,30))  
img_2 = ImageTk.PhotoImage(img_2)
b_anterior = Button(frame_baixo,command=anterior_musica, width=40, height=40, image=img_2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=co3, fg=co1)
b_anterior.place(x=38, y=35)

img_3 = Image.open('3.png')
img_3 = img_3.resize((30,30))  
img_3 = ImageTk.PhotoImage(img_3)
b_play = Button(frame_baixo, command=play_musica, width=40, height=40, image=img_3, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=co3, fg=co1)
b_play.place(x=84, y=35)

img_4 = Image.open('4.png')
img_4 = img_4.resize((30,30))  
img_4 = ImageTk.PhotoImage(img_4)
b_proximo = Button(frame_baixo,command=proxima_musica, width=40, height=40, image=img_4, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=co3, fg=co1)
b_proximo.place(x=130, y=35)

img_5 = Image.open('5.png')
img_5 = img_5.resize((30,30))  
img_5 = ImageTk.PhotoImage(img_5)
b_pausar = Button(frame_baixo,command=pausar_musica, width=40, height=40, image=img_5, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=co3, fg=co1)
b_pausar.place(x=176, y=35)

img_6 = Image.open('6.png')
img_6 = img_6.resize((30,30))  
img_6 = ImageTk.PhotoImage(img_6)
b_continuar = Button(frame_baixo,command=continuar_musica, width=40, height=40, image=img_6, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=co3, fg=co1)
b_continuar.place(x=222, y=35)

img_7 = Image.open('7.png')
img_7 = img_7.resize((30,30))  
img_7 = ImageTk.PhotoImage(img_7)
b_stop = Button(frame_baixo,command=para_musica, width=40, height=40, image=img_7, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=co3, fg=co1)
b_stop.place(x=268, y=35)

# Configurar o diretório de trabalho
os.chdir(r'c:\Users\eloca\OneDrive\Área de Trabalho\music Baixadas')
musicas = os.listdir()

def mostrar():
    listabox.delete(0, END)  # Limpa a lista antes de adicionar os novos itens
    for i in musicas:
        listabox.insert(END, i)

mostrar()

# Inicializando o mixer
mixer.init()

janela.mainloop()
