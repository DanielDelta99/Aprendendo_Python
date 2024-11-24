import tkinter as tk
from tkinter import messagebox

# Funções que serão executadas ao clicar nos botões
def opcao_1():
    messagebox.showinfo("Opção 1", "Você escolheu a opção 1")

def opcao_2():
    messagebox.showinfo("Opção 2", "Você escolheu a opção 2")

def sair():
    janela.quit()

# Criando a janela principal
janela = tk.Tk()
janela.title("Menu Gráfico Interativo")
janela.geometry("300x200")  # Definir o tamanho da janela

# Criando um menu de opções
menu_barra = tk.Menu(janela)

# Adicionando um menu dropdown
menu_opcoes = tk.Menu(menu_barra, tearoff=0)
menu_opcoes.add_command(label="Opção 1", command=opcao_1)
menu_opcoes.add_command(label="Opção 2", command=opcao_2)
menu_opcoes.add_separator()
menu_opcoes.add_command(label="Sair", command=sair)

# Adicionando o menu à barra
menu_barra.add_cascade(label="Opções", menu=menu_opcoes)
janela.config(menu=menu_barra)

# Criando botões na janela principal
botao1 = tk.Button(janela, text="Opção 1", command=opcao_1)
botao1.pack(pady=10)

botao2 = tk.Button(janela, text="Opção 2", command=opcao_2)
botao2.pack(pady=10)

botao_sair = tk.Button(janela, text="Sair", command=sair)
botao_sair.pack(pady=10)

# Iniciando o loop principal da interface gráfica
janela.mainloop()