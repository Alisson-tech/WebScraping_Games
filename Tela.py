from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter
import pandas as pd
import Web_Scraping


class Tela:
    def __init__(self, janela):
        
        #Configurando Janela
        janela.geometry("650x400+100+100")
        janela['bg'] = '#25222f'
        janela.title("tela principal")

        # Texto de erro
        self.text = StringVar()
        self.text.set('* Inválido')

        # Label erro marca
        self.lbErroM = Label(janela, textvariable=self.text, background='#25222f',foreground='#ff0000')
        self.lbErroM.place(x=50, y=30)
        self.lbErroM.place_forget()

        # textbox marca
        self.tbMarc = Entry(janela, width=15)
        self.tbMarc.place(x=50, y=50)
        self.tbMarc.insert(0, 'Distribuidora')
        self.tbMarc.bind("<Button-1>", lambda event: self.clear_entry(self.tbMarc))

        self.lbErroI = Label(janela, textvariable=self.text, background='#25222f',foreground='#ff0000')
        self.lbErroI.place(x=180, y=30)
        self.lbErroI.place_forget()

        # textbox Item
        self.tbItem = Entry(janela, width=15)
        self.tbItem.place(x=180, y=50)
        self.tbItem.insert(0, 'Jogo')
        self.tbItem.bind("<Button-1>", lambda event: self.clear_entry(self.tbItem))

        # label error Plataforma
        self.lbErroP = Label(janela, textvariable=self.text, background='#25222f',foreground='#ff0000')
        self.lbErroP.place(x=310, y=30)
        self.lbErroP.place_forget()

        # textbox Plataforma
        self.tbPlat = Entry(janela, width=13)
        self.tbPlat.place(x=310, y=50)
        self.tbPlat.insert(0, 'Plataforma')
        self.tbPlat.bind("<Button-1>", lambda event: self.clear_entry(self.tbPlat))

        #label erro quantidade
        self.lbErroQ = Label(janela, textvariable=self.text, background='#25222f',foreground='#ff0000')
        self.lbErroQ.place(x=430, y=30)
        self.lbErroQ.place_forget()

        # Spinbox qtd
        self.tbQtd = Spinbox(janela, width=5, from_=0, to=100)
        self.tbQtd.place(x=430, y=50)

        # Botão para Inserir dado no treeview
        self.btnInsert  = Button(janela, width=2, height=1, text="+", command= lambda:[self.btnInsert_click(self.tbMarc.get(), self.tbItem.get(), self.tbPlat.get(), self.tbQtd.get())])
        self.btnInsert.place (x=505, y=50)
        self.btnInsert['bg'] = '#5f5dff'

        # Botão para Excluir dado no treeview
        self.btnDel  = Button(janela, width=2, height=1, text="-", command= lambda:[self.btnDel_click()])
        self.btnDel .place (x=555, y=50)
        self.btnDel ['bg'] = '#ff5d5b'

        # Criar treeview
        self.columns = ('#1', '#2', '#3', '#4')
        self.tree = ttk.Treeview(janela, columns=self.columns, show='headings')
        self.tree.column('#1',width=150)
        self.tree.column('#2',width=150)
        self.tree.column('#3',width=150)
        self.tree.column('#4',width=100)

        # define headings(colunas)
        self.tree.heading('#1', text='Marca')
        self.tree.heading('#2', text='Item')
        self.tree.heading('#3', text='Plataforma')
        self.tree.heading('#4', text='QTD')
        self.tree.place(x=50, y=100)

        # Botão Confirmar para realizar o web scraping
        self.btnConf  = Button(janela, width=15, text="Confirmar",
        command= lambda:[self.btnConf_click()])
        self.btnConf.place (x=455, y=340)
        self.btnConf['bg'] = '#00ff14'


    # limpa os textbox
    def clear_entry(self,tb):
        tb.delete(0, END)

    # Validar dados
    def Validar(self, Marc, Item, Plat, QTD):

        self.lbErroM.place_forget()
        self.lbErroI.place_forget()
        self.lbErroP.place_forget()
        self.lbErroQ.place_forget()
        erro = False
        try:
            Marc = str(Marc)
            if(Marc=='Distribuidora' or Marc==''):
                erro = True
                self.lbErroM.place(x=50, y=30)
        except:
            erro = True
            self.lbErroM.place(x=50, y=30)
        
        try:
            Item = str(Item)
            if(Item=='Jogo' or Item==''):
                erro = True
                self.lbErroI.place(x=180, y=30)

        except:
            erro = True
            self.lbErroI.place(x=180, y=30)

        try:
            Plat = str(Plat)
            if(Plat=='Plataforma' or Plat==''):
                erro = True
                self.lbErroP.place(x=310, y=30)

        except:
            erro = True
            self.lbErroP.place(x=310, y=30)

        try:
            QTD = int(QTD)
            if(QTD==''):
                self.lbErroQ.place(x=430, y=30)
                erro = True

        except:
            self.lbErroQ.place(x=430, y=30)
            erro = True

        if erro==False:
            dados = [Marc, Item, Plat, QTD]
        else:
            dados = 'erro'
            
        return dados

    # Inserir no treeView
    def btnInsert_click(self, Marc, Item, Plat, QTD):
        dados = self.Validar(Marc, Item, Plat, QTD)

        if(dados!='erro'):
            self.tree.insert('', tkinter.END, values=dados)

    # Excluir dados do treeview
    def btnDel_click(self):

        try:
            selected_item = self.tree.selection()[0]
            self.tree.delete(selected_item)

        except:
            pass
    
    # Chamar função de web scraping
    def btnConf_click(self):
        lista = [] 
        for dado in self.tree.get_children():
            lista.append(self.tree.item(dado)['values'])

        colunas = ['Marca', 'Item', 'Plataforma', 'QTD']
        df = pd.DataFrame(data= lista, columns=colunas)

        Web_Scraping.Buscar_game(df)

# criar janela
janela = Tk()

#passar janela para a tela
Tela(janela)

#manter janela aberta
janela.mainloop()




