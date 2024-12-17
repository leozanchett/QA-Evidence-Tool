import tkinter as tk
from tkinter import filedialog, messagebox

from controller.c_write_docx import WriteDocxController

def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory(
        title="Selecione uma pasta"
    )
    if pasta_selecionada:
        entrada_pasta.delete(0, tk.END)
        entrada_pasta.insert(0, pasta_selecionada)

janela = tk.Tk()
janela.title("Selecionar Pasta")

largura = 500
altura = 200

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)

janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
entrada_pasta = tk.Entry(janela, width=100)
entrada_pasta.pack(pady=5, padx=20)

botao_selecionar = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
botao_selecionar.pack(pady=20)

write_docx_controller = WriteDocxController()


def gerar_docx():
    pasta_selecionada = entrada_pasta.get()
    resultado = write_docx_controller.write_docx(pasta_selecionada)
    messagebox.showinfo("QA - Tool", resultado)

botao_gerar = tk.Button(janela, text="Gerar Docx", command=gerar_docx, width=10)
botao_gerar.pack(pady=3, padx=20)

janela.mainloop()