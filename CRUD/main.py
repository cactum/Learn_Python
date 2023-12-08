import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from view import *

####### cores #######
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # profit
co6 = "#038cfc"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # verde
co9 = "#e9edf5"  # sky blue

# criando janela
janela = tk.Tk()
janela.title("PYSQLITE")
janela.geometry('1090x485')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

# Dividindo a janela em frames
frame_cima = tk.Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = tk.Frame(janela, width=310, height=450, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=tk.NSEW, padx=0, pady=1)

frame_direita = tk.Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=tk.NSEW)

# Label no frame_cima (alterado para um Label)
app_nome = tk.Label(frame_cima, text='Formulário de Consultoria', font=('Arial', 10, 'bold'), bg=co2, fg=co1)
app_nome.place(x=10, y=20)

#variavel tree global
global tree

# função inserir
def inserir():
    nome = e_nome.get()
    cpf = e_cpf.get()
    email = e_email.get()
    telefone = e_telefone.get()
    dia = e_cal.get()
    estado = e_estado.get()
    assunto = e_obs.get()

    lista = [nome, cpf, email, telefone, dia, estado, assunto]

    if nome == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'dados inseridos')

        e_nome.delete(0, 'end')
        e_cpf.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_obs.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    exibir()


# função atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor = tree_lista[0]

        e_nome.delete(0, 'end')
        e_cpf.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_obs.delete(0, 'end')

        e_nome.insert(0,tree_lista[1])
        e_cpf.insert(0,tree_lista[2])
        e_email.insert(0,tree_lista[3])
        e_telefone.insert(0,tree_lista[4])
        e_cal.insert(0,tree_lista[5])
        e_estado.insert(0,tree_lista[6])
        e_obs.insert(0,tree_lista[7])

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

    def update():
        nome = e_nome.get()
        cpf = e_cpf.get()
        email = e_email.get()
        telefone = e_telefone.get()
        dia = e_cal.get()
        estado = e_estado.get()
        assunto = e_obs.get()

        lista = [nome, cpf, email, telefone, dia, estado, assunto]

        if nome == '':
            messagebox.showerror('Erro', 'O nome não pode ser vazio')
        else:
            atualizar_info(lista)
            messagebox.showinfo('Sucesso', 'dados atualizados')

            e_nome.delete(0, 'end')
            e_cpf.delete(0, 'end')
            e_email.delete(0, 'end')
            e_telefone.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_estado.delete(0, 'end')
            e_obs.delete(0, 'end')

        for widget in frame_direita.winfo_children():
            widget.destroy()

    b_confirmar = tk.Button(frame_baixo, command=update, text='Confirmar', width=10, anchor=tk.NW, font=('Arial', 9, 'bold'),
                                bg=co2,
                                fg=co1,
                                relief='raised', overrelief='ridge')
    b_confirmar.place(x=105, y=400)

    exibir()



# Configurando Frame baixo

# Nome
l_nome = tk.Label(frame_baixo, text='Nome: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = tk.Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

# CPF
l_cpf = tk.Label(frame_baixo, text='CPF: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_cpf.place(x=10, y=70)
e_cpf = tk.Entry(frame_baixo, width=45, justify='left', relief='solid')
e_cpf.place(x=15, y=100)

# Email
l_email = tk.Label(frame_baixo, text='Email: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_email.place(x=10, y=130)
e_email = tk.Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=160)

# Telefone
l_telefone = tk.Label(frame_baixo, text='Telefone: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_telefone.place(x=10, y=190)
e_telefone = tk.Entry(frame_baixo, width=45, justify='left', relief='solid')
e_telefone.place(x=15, y=220)

# Data consulta
l_cal = tk.Label(frame_baixo, text='Data da Consulta: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_cal.place(x=15, y=250)
e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023)
e_cal.place(x=15, y=280)

# Estado consulta
l_estado = tk.Label(frame_baixo, text='Estado da Consulta: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_estado.place(x=150, y=250)
e_estado = tk.Entry(frame_baixo, width=20, justify='left', relief='solid')
e_estado.place(x=150, y=280)

# Observações
l_obs = tk.Label(frame_baixo, text='Observações: ', font=('Arial', 10, 'bold'), bg=co1, fg=co4)
l_obs.place(x=15, y=310)
e_obs = tk.Entry(frame_baixo, width=45, justify='left', relief='solid')
e_obs.place(x=15, y=340)

# Botão inserir
b_inserir = tk.Button(frame_baixo, command=inserir, text='Inserir', width=10, anchor=tk.NW, font=('Arial', 9, 'bold'), bg=co6, fg=co1,
                      relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=370)

# Botão Atualizar
b_atualizar = tk.Button(frame_baixo, command=atualizar, text='Atualizar', width=10, anchor=tk.NW, font=('Arial', 9, 'bold'), bg=co6,
                        fg=co1,
                        relief='raised', overrelief='ridge')
b_atualizar.place(x=105, y=370)

# Botão Deletar
b_deletar = tk.Button(frame_baixo, text='Deletar', width=10, anchor=tk.NW, font=('Arial', 9, 'bold'), bg=co7, fg=co1,
                      relief='raised', overrelief='ridge')
b_deletar.place(x=195, y=370)


# Frame direita

def exibir():

    global tree

    lista = exibir_info()

    tabela_head = ['Id', 'Nome', 'CPF', 'Email', 'Telefone', 'Data', 'Estado', 'Observação']

    df_list = lista

    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)
    frame_direita.grid_columnconfigure(0, weight=12)

    # Ajuste dos elementos para a exibição correta na Treeview
    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center", "center"]
    h = [30, 120, 120, 150, 120, 60, 70, 100]
    n = 0

    # Configuração da tabela
    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=tk.CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in df_list:
        tree.insert('', 'end', values=item)


# chamando a funcao exibir
exibir()

janela.mainloop()
