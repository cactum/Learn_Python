import tkinter as tk
from cgitb import text
from tkcalendar import Calendar, DateEntry

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

#Nome
l_nome = tk.Label(frame_baixo, text='Nome: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = tk.Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

#CPF
l_cpf = tk.Label(frame_baixo, text='CPF: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_cpf.place(x=10, y=70)
e_cpf = tk.Entry(frame_baixo, width=45, justify='left', relief='solid')
e_cpf.place(x=15, y=100)

#Email
l_email = tk.Label(frame_baixo, text='Email: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_email.place(x=10, y=130)
e_email = tk.Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=160)

#Telefone
l_telefone = tk.Label(frame_baixo, text='Telefone: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_telefone.place(x=10, y=190)
e_telefone = tk.Entry(frame_baixo, width=45, justify='left', relief='solid')
e_telefone.place(x=15, y=220)

#Data consulta
l_cal = tk.Label(frame_baixo, text='Data da Consulta: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_cal.place(x=15, y=250)
e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023)
e_cal.place(x=15, y=280)

#Estado consulta
l_estado = tk.Label(frame_baixo, text='Estado da Consulta: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_estado.place(x=150, y=250)
e_estado = tk.Entry(frame_baixo, width=20, justify='left', relief='solid')
e_estado.place(x=150, y=280)

"""
#Observações (VERSAO ALTERNATIVA CAIXA)
l_obs = tk.Label(frame_baixo, text='Observações: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_obs.place(x=15, y=310)
e_obs = tk.Text(frame_baixo, width=32, height=3, relief='solid')
e_obs.place(x=15, y=340)
"""
#Observações
l_obs = tk.Label(frame_baixo, text='Observações: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_obs.place(x=15, y=310)
e_obs = tk.Entry(frame_baixo, width=45, justify='left', relief='solid')
e_obs.place(x=15, y=340)

janela.mainloop()