import tkinter as tk

# Criando a janela principal
janela = tk.Tk()
janela.title("Exemplo com Entry")
janela.geometry("400x300")

# Criando um rótulo
rotulo = tk.Label(janela, text="Digite seu nome:", font=("Noto", 12))
rotulo.pack(pady=10) 

# Criando um rótulo
entrada = tk.Entry(janela, font=("Oto", 12)) 
entrada.pack(pady=10)

# Função para ixibir o testo inserido
def mostrar_nome():
    nome = entrada.get() 
    rotulo.config(text=f"Olá, {nome}")
    
# Criando um botão 
botao = tk.Button(janela, text="Enviar", command=mostrar_nome,font=("Noto", 12))
botao.pack(pady=10)

# Iniciando o loop principal 
janela.mainloop()
    
