from genericpath import isdir
from pandas.core.indexes.base import Index
import time
import pandas as pd
import urllib 
import os
import shutil
import requests
from bs4 import BeautifulSoup

# Buscar games
def Buscar_game(df):

    #Criar pasta temporaria para armazenar imagens
    criar_pasta()

    # obter lista de game
    game = df['Item'].to_list()

    for g in game:
        # Parametros de Pesuisa
        pesquisa = {'q': g}

        # Requisição da pagina
        page = requests.get("https://www.grouvee.com/search/", params=pesquisa)
        time.sleep(2)

        # Transformar em objeto  BeautifulSoup
        soup_page = BeautifulSoup(page.text, 'html.parser')

        try:
            # Procurar Div da Img
            div = soup_page.find(class_='box-art')

            # Procurar tag da Img
            img = div.find('a').find('img')

            # Obter Link da Img
            link_img = img.get('src')


            # Salvar imagem
            urllib.request.urlretrieve(link_img, 'img/{}.jpg'.format(g))

        except:
            pass
    
    Planilha(df)
    
# Criar Planilha
def Planilha(df):

    df['Capa'] = None
    # Converter dataframe em excel
    writer = pd.ExcelWriter('Estoque_Games.xlsx', engine='xlsxwriter')

    # definir sheet
    df.to_excel(writer, sheet_name='Sheet1')
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    # Formato das células
    data_format = workbook.add_format({'align':'center', 'valign':'vcenter'})
   

    # Tamanho das células
    worksheet.set_default_row(150)
    worksheet.set_row(0, 20)
    worksheet.set_column('A:D', 20, data_format)
    worksheet.set_column('E:E', 10, data_format)
    worksheet.set_column('F:F', 25, data_format)


    game = df['Item'].to_list()
    count = 1
    # Colocar imagem na planilha se ela existir
    # Se não existir colocar '?'
    for g in game:
        count+=1
        imgPath = f'img/{g}.jpg'
        if(os.path.isfile(imgPath)):
            # Inserir imagens e centralizar
            worksheet.insert_image('F{}'.format(count), imgPath,
            {'x_offset': 20, 'y_offset': 20})
            
        else:
            worksheet.write(f'F{count}', '?') 



    # Fechar pandas e gerar planilha
    writer.save()
    # Apagar pasta temporaria
    apagar_pasta()

#apagar pasta com imagens
def apagar_pasta():
    dir = 'img'
    if(os.path.isdir(dir)):
        shutil.rmtree(dir)

#  Criar pasta para salvar as imagens
def criar_pasta():
    dir = 'img'
    if(not os.path.isdir(dir)):
        os.makedirs(dir)
