from tkinter import *
from tkinter import ttk

# Inicializa a janela principal
root = Tk()
root.title("Opções de Seleção")
root.geometry("300x400")
root.configure(bg="#f0f8ff")

# Variável para armazenar a opção selecionada
valor = IntVar()
valor.set(3)  # Define a opção 3 como padrão

# Label de título
title = Label(root, text="Escolha uma Opção", font=("Helvetica", 14, "bold"), bg="#4682b4", fg="white")
title.pack(pady=10, fill="x")

# Frame para os botões de rádio
radio_frame = Frame(root, bg="#f0f8ff")
radio_frame.pack(pady=20)

# Função para mostrar a opção selecionada na tela
def ver_radio():
    selected_option.set(f"Você selecionou: Opção {valor.get()}")

# Criação dos botões de rádio dinamicamente
for i in range(1, 11):
    Radiobutton(radio_frame, text=f"Opção {i}", variable=valor, value=i,
                font=("Helvetica", 10), bg="#f0f8ff").pack(anchor="w")

# Botão para confirmar a seleção
selected_option = StringVar()
Button(root, text="Executar", command=ver_radio, font=("Helvetica", 12),
       bg="#4682b4", fg="white").pack(pady=10)

# Label para exibir a opção selecionada
selected_label = Label(root, textvariable=selected_option, font=("Helvetica", 12, "italic"),
                       bg="#f0f8ff", fg="#4682b4")
selected_label.pack(pady=10)

# Executa o loop principal da interface gráfica
root.mainloop()
