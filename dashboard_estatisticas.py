from distutils.cmd import Command
from tkinter import *
from tkinter import ttk
from turtle import position
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv(r'C:/Users/didico/Documents/arquivos/teste_dtf.csv')

def grafico_partida():
    
    ################# cores ###############
    co0 = "#f0f3f5"  # Preta
    co1 = "#feffff"  # branca
    co2 = "#6f9fbd"  # azul
    co3 = "#38576b"  # valor
    co4 = "#403d3d"   # para letra
    co5 = "#e06636"   
    co6 = "#6dd695" 

    fundo = "#3F729B"

    janela = Tk()
    #janela.state('zoomed')
    janela.title('')

    ################# Frames ####################
    # Neste frame iremos Mostrar o nome do Aplicativo
    frame_app_nome = Frame(janela, width=1370, height=40, pady=0,padx=0, bg=co1,  relief="flat")
    frame_app_nome.grid(row=0, column=0)

    #Aqui iremos mostrar as estatisticas
    frame_quadros = Frame(janela, width=1370, height=700,bg=co0, pady=15, padx=7, relief="flat",)
    frame_quadros.grid(row=1, column=0, sticky=NW)

    ################# Criando label para o frame_app_nome #############
    app_nome = Label(frame_app_nome, text=f"{dados.loc[0, 'time_mandante']} X {dados.loc[0,'time_visitante']}", width=30, height=2,pady=1, padx=0, relief="flat", anchor=N, font=('Ivy 14 bold'), bg=co1, fg=co4)
    app_nome.place(x=500, y=5)

    #------------------------------------------------------------------------------------------------------
    # Estadio - data
    frame_estadio = Frame(frame_quadros, width=200, height=90,bg=co1, relief="flat",)
    frame_estadio.place(x=0, y=0)

    app_pr = Label(frame_estadio, text="", width=1, height=10,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_pr.place(x=0, y=0)

    app_nome_rev = Label(frame_estadio, text="ESTADIO", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_rev.place(x=20, y=5)

    app_nome_va = Label(frame_estadio, text=f"{dados.loc[0, 'estadio']}", height=1, pady=0, padx=0,relief="flat", anchor=CENTER, font=('Ivy 11 bold'), bg=co1, fg=co3)
    app_nome_va.place(x=40, y=35)

    app_nome_p = Label(frame_estadio, text=f"{dados.loc[0, 'data_realizacao']} |", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 8 bold'), bg=co1, fg=co6)
    app_nome_p.place(x=60, y=70)

    app_nome_p = Label(frame_estadio, text=f"{dados.loc[0, 'hora_realizacao']}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 8 bold'), bg=co1, fg=co6)
    app_nome_p.place(x=120, y=70)

    #------------------------------------------------------------------------------------------------------
    # Cartoes
    frame_cartoes = Frame(frame_quadros, width=200, height=90,bg=co1, relief="flat",)
    frame_cartoes.place(x=210, y=0)

    app_pr = Label(frame_cartoes, text="", width=1, height=10,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_pr.place(x=0, y=0)

    app_nome_rev = Label(frame_cartoes, text="CARTOES", height=1,pady=0, padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_rev.place(x=20, y=5)

    app_nome_va = Label(frame_cartoes, text=f"{dados.loc[0, 'time_mandante']}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co3)
    app_nome_va.place(x=20, y=35)

    app_nome_va = Label(frame_cartoes, text=f"{dados.loc[0, 'time_visitante']}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co3)
    app_nome_va.place(x=20, y=60)

    app_nome_p = Label(frame_cartoes)

    # ------------------------------------------------------------------------------------------------------

    # Placar
    frame_placar = Frame(frame_quadros, width=410, height=100,bg=co1, relief="flat",)
    frame_placar.place(x=0, y=100)

    app_pr = Label(frame_placar, text="", width=1, height=10,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_pr.place(x=0, y=0)

    app_nome_rev = Label(frame_placar, text="PLACAR", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_rev.place(x=20, y=5)

    app_nome_va = Label(frame_placar, text=f"{dados.loc[0, 'placar_mandante']} x {dados.loc[0, 'placar_visitante']}", height=1, pady=0, padx=0,relief="flat", anchor=CENTER, font=('Ivy 30 bold'), bg=co1, fg=co3)
    app_nome_va.place(x=150, y=35)


    # ------------------------------------------------------------------------------------------------------
    # Posse de bola

    frame_possebola = Frame(frame_quadros, width=500, height=200, bg=co1, relief="flat",)
    frame_possebola.place(x=420, y=0)

    # dados para valores de posse de bola
    #vlr_posses_bola = [f"{dados.loc[0, 'posse_bolatime1']}", f"{dados.loc[0, 'posse_bolatime2']}"]
    vlr_posses_bola = [5, 10]

    # Nomes dos times para plotagem
    times = [f"{dados.loc[0,'time_mandante']}", f"{dados.loc[0, 'time_visitante']}"]

    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(11.4, 2.5), dpi=80)
    ax = figura.add_subplot(111)


    ax.bar(times, vlr_posses_bola,  color="#82b1ff")
    # create a list to collect the plt.patches data
    totals = []

    c = 0
    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.03, i.get_height()+.5,'('+str(vlr_posses_bola[c])+')', fontsize=12, fontstyle='italic',  verticalalignment='baseline', color='dimgrey')
        c += 1

    # Personalizando o gráfico
    ax.patch.set_facecolor('#FFFFFF')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)

    app_pr = Label(frame_possebola, text="", width=1, height=10, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_pr.place(x=0, y=0)
    app_nome_rev = Label(frame_possebola, text="POSSE DE BOLA", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_rev.grid(row=0, column=0, padx=20, pady=0, sticky=NSEW)
    canva = FigureCanvasTkAgg(figura, frame_possebola)
    canva.get_tk_widget().grid(row=1, column=0, sticky=NSEW)

    # ------------------------------------------------------------------------------------------------------
    # EXEMPLO GRAF PIZZA
    # Faturamento por Categoria 

    frame_categoria = Frame(frame_quadros, width=200,height=200, bg=co1, relief="flat",)
    frame_categoria.place(x=420, y=230)

    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5.15, 4), dpi=80)
    ax = figura.add_subplot(111)

    # Vendas 
    categoria_total = [5701, 4275, 8385, 5934, 6934]

    # Categorias
    labels = ["Categoria - 1", "Categoria - 2 ", "Categoria - 3", "Categoria - 4", "Categoria - 5"]

    # only "explode
    explode = (0.1, 0.1, 0.1, 0.1, 0.1)

    # colors = ['#665191', '#a05195','#d45087',  "#f95d6a", "#ff7c43", "#ffa600"]
    colors = ['#ff9999',  '#c5cae9', '#bbdefb', '#99ff99', '#ffcc99']


    ax.pie(categoria_total, explode=explode, wedgeprops=dict(width=0.64), labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

    app_cat = Label(frame_categoria, text="", width=1, height=10, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_cat.place(x=0, y=0)
    app_categoria = Label(frame_categoria, text="Desempenho de categorias Top - 5", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_categoria.grid(row=0, column=0, pady=0, padx=20, columnspan=2, sticky=NSEW)
    canva_categoria = FigureCanvasTkAgg(figura, frame_categoria)
    canva_categoria.get_tk_widget().grid(row=1, column=0, sticky=NSEW)


    # ------------------------------------------------------------------------------------------------------
    # EXEMPLOS GRAF BAR
    # Faturamento por Vendedores 

    frame_vendedor = Frame(frame_quadros, width=200, height=200,bg=co1, relief="flat",)
    frame_vendedor.place(x=840, y=230)

    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(7.3, 4.6), dpi=70)
    ax = figura.add_subplot(111)

    # vendas
    vlr_posses_bola = [2701, 4275, 6385, 8693, 3622]

    # vendedores
    vendedor = ["Vendedor - 1", "Vendedor - 2 ", "Vendedor - 3", "Vendedor - 4", "Vendedor - 5"]

    ax.bar(vendedor, vlr_posses_bola,  color=colors)

    # create a list to collect the plt.patches data
    totals = []


    c = 0
    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.03, i.get_height()+.5, str(vlr_posses_bola[c])+'$', fontsize=12, fontstyle='italic', color='dimgrey', weight='bold', verticalalignment='baseline',)
        c += 1

    ax.patch.set_facecolor('#FFFFFF')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)


    app_vend = Label(frame_vendedor, text="", width=1, height=10, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_vend.place(x=0, y=0)
    app_categoria_vendedor = Label(frame_vendedor, text="Faturamento por Vendedor Top - 5", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_categoria_vendedor.grid(row=0, column=0, pady=0, padx=20, columnspan=2, sticky=NSEW)
    canva_vendedor = FigureCanvasTkAgg(figura, frame_vendedor)
    canva_vendedor.get_tk_widget().grid(row=1, column=0, sticky=NSEW)

    janela.mainloop()