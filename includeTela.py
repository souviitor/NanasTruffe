import customtkinter as ctk
import sqlite3
from backend import incluir_sabor, atualizar_estoque

def abrir_tela_incluir():
    def incluir_no_banco():
        sabor = combobox_sabor.get()
        quantidade = int(entry_quantidade.get())
        preco = float(entry_preco.get())

        incluir_sabor(sabor)
        atualizar_estoque(sabor, quantidade, preco)
        label_status.configure(text="Sabor e estoque incluídos com sucesso!")

    # Configuração principal da janela
    janela = ctk.CTk()
    janela.geometry("400x400")
    janela.title("Nana's Truffes - Incluir")

    # Título
    titulo = ctk.CTkLabel(janela, text="Incluir Trufas", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    # Combobox para selecionar o sabor
    label_sabor = ctk.CTkLabel(janela, text="Sabor:")
    label_sabor.pack(pady=5)
    combobox_sabor = ctk.CTkComboBox(
        janela, values=["Chocolate+Brigadeiro", "Chocolate+Morango",
                        "Chocolate+Maracujá", "Chocolate+Ninho", "Chocolate+Limão",
                        "Branco+Brigadeiro", "Branco+Morango", "Branco+Maracujá",
                        "Branco+Ninho", "Branco+Limão"])
    combobox_sabor.pack(pady=5)

    # Campo para quantidade
    label_quantidade = ctk.CTkLabel(janela, text="Quantidade:")
    label_quantidade.pack(pady=5)
    entry_quantidade = ctk.CTkEntry(janela)
    entry_quantidade.pack(pady=5)

    # Campo para preço unitário
    label_preco = ctk.CTkLabel(janela, text="Preço por unidade:")
    label_preco.pack(pady=5)
    entry_preco = ctk.CTkEntry(janela)
    entry_preco.pack(pady=5)

    # Botão para incluir no banco de dados
    botao_incluir = ctk.CTkButton(janela, text="Incluir", command=incluir_no_banco)
    botao_incluir.pack(pady=20)

    # Status
    label_status = ctk.CTkLabel(janela, text="")
    label_status.pack(pady=10)

    janela.mainloop()
