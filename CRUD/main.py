import tkinter as tk


####### cores #######
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # verde
co9 = "#e9edf5"   # sky blue


# criando janela
janela = tk.Tk()
janela.title("PYSQLITE")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

# Dividindo a janela em frames
frame_cima = tk.Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = tk.Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=tk.NSEW, padx=0, pady=1)

frame_direita = tk.Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=tk.NSEW)

# Label no frame_cima (alterado para um Label)
app_nome = tk.Label(frame_cima, text='Formulário de Consultoria', font=('Arial', 10, 'bold'), bg=co2, fg=co1)
app_nome.place(x=10, y=20)

# Configurando Frame baixo
l_nome = tk.Label(frame_baixo, text='Nome: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)

e_nome = tk.Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=10, y=40)



janela.mainloop()