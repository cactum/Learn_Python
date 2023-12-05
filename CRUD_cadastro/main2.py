import tkinter as tk

class Gui():
    x_pad = 5
    y_pad = 3
    width_entry = 30

    def __init__(self, window):
        self.window = window
        self.window.wm_title("PYSQL versão 1.0")

        # Definição das variáveis que recebem os dados inseridos pelo usuário
        self.txtNome = tk.StringVar()
        self.txtSobrenome = tk.StringVar()
        self.txtEmail = tk.StringVar()
        self.txtCPF = tk.StringVar()

        # Criando objetos que farão parte das janelas
        self.lblnome = tk.Label(window, text="Nome")
        self.lblsobrenome = tk.Label(window, text="Sobrenome")
        self.lblemail = tk.Label(window, text="Email")
        self.lblcpf = tk.Label(window, text="CPF")
        self.entNome = tk.Entry(window, textvariable=self.txtNome, width=Gui.width_entry)
        self.entSobrenome = tk.Entry(window, textvariable=self.txtSobrenome, width=Gui.width_entry)
        self.entEmail = tk.Entry(window, textvariable=self.txtEmail, width=Gui.width_entry)
        self.entCPF = tk.Entry(window, textvariable=self.txtCPF, width=Gui.width_entry)
        self.listClientes = tk.Listbox(window, width=100)
        self.scrollClientes = tk.Scrollbar(window)
        self.btnViewAll = tk.Button(window, text="Ver todos")
        self.btnBuscar = tk.Button(window, text="Buscar")
        self.btnInserir = tk.Button(window, text="Inserir")
        self.btnUpdate = tk.Button(window, text="Atualizar selecionados")
        self.btnDel = tk.Button(window, text="Deletar selecionados")
        self.btnClose = tk.Button(window, text="Fechar")

        # Associando objetos
        self.lblnome.grid(row=0, column=0)
        self.lblsobrenome.grid(row=1, column=0)
        self.lblemail.grid(row=2, column=0)
        self.lblcpf.grid(row=3, column=0)
        self.entNome.grid(row=0, column=1, padx=50, pady=50)
        self.entSobrenome.grid(row=1, column=1)
        self.entEmail.grid(row=2, column=1)
        self.entCPF.grid(row=3, column=1)
        self.listClientes.grid(row=0, column=2, rowspan=10)
        self.scrollClientes.grid(row=0, column=6, rowspan=10)
        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDel.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

        # União do scrollbar com a listbox
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        # Adicionar SWAG (aparência) à interface
        for child in window.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky='WE', padx=self.x_pad, pady=self.y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widget_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky='N')

    def run(self):
        self.window.mainloop()

# Criando a janela principal
window = tk.Tk()
app = Gui(window)
app.run()
