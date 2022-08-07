#from antigravity import geohash
from tkinter import *
from urllib import response
from PIL import ImageTk, Image
import requests
import json

cor1 = '#484f60'

# --------Criando a janela principal------------           Bitcoin icon by Icons8         {"USD":23210.03,"EUR":22800.54,"BRL":120346.1}
janela = Tk()
janela.geometry('400x400')
janela.title('Conversor')
janela.configure(background=cor1)

# --------separando os frames ------------
frame_topo = Frame(janela, width=400, height=60, bg='#484f60', pady=0, padx=0, relief='flat')
frame_topo.grid(row=1, column=0)

frame_baixo = Frame(janela, width=400, height=250, bg='#484f60', pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)
def info():
    # HTTP link
    Apilink = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,BRL'
    response = requests.get(Apilink)

    # Converterndo em dicionario
    dados = response.json()

    # Convertendo os dados em dicionario
    valor_USD = float(dados['USD'])
    valor_formatado_usd = '$ {:,.3f}'.format(valor_USD)
    l_p_usd['text'] = 'Em Dolar é $ '+ valor_formatado_usd

    valor_BRL = float(dados['BRL'])
    valor_formatado_brl = 'R$ {:,.3f}'.format(valor_BRL)
    l_p_real['text'] = 'Em Real é R$ '+  valor_formatado_brl

    valor_EUR = float(dados['EUR'])
    valor_formatado_eur = '£ {:,.3f}'.format(valor_EUR)
    l_p_eur['text'] = 'Em Euro é £ '+ valor_formatado_eur

    frame_baixo.after(1000, info)






# --------Configurando imagens ------------
imagem = Image.open('imagens/BIT.png')
imagem = imagem.resize((50,50))
imagem = ImageTk.PhotoImage(imagem)


l_icon = Label(frame_topo, image=imagem, compound=LEFT, bg='#484f60', relief='flat')
l_icon.place(x=10, y=7)

l_nome = Label(frame_topo, text='Bitcoin Price Tracker', bg='#484f60', fg='#FFF', 
relief=FLAT, anchor='center', font=('Arial 20'))
l_nome.place(x=70, y=15)

l_p_usd = Label(frame_baixo,  text='', bg='#484f60', fg='#FFF', relief=FLAT, anchor='center', font=('Arial 14'))
l_p_usd.place(x=10, y=130)

l_p_real = Label(frame_baixo, text='', bg='#484f60', fg='#FFF', 
relief=FLAT, anchor='center', font=('Arial 14'))
l_p_real.place(x=10, y=160)

l_p_eur = Label(frame_baixo, text='', bg='#484f60', fg='#FFF', 
relief=FLAT, anchor='center', font=('Arial 14'))
l_p_eur.place(x=10, y=190)


info()

janela.mainloop()