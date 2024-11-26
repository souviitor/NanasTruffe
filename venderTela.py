import customtkinter as ctk
from datetime import datetime
from backend import realizar_venda

def tela_vender():
    def vender():
        sabor = combobox_sabor.get()
        quantidade = int(entry_quantidade.get())
        comprador = entry_comprador.get()
        data_venda = datetime.now().strftime('%Y-%m-%d')

        realizar_venda(sabor, quantidade, comprador, data_venda)
        label_status.configure(text="Venda realizada com sucesso!")

    # Configuração principal da janela
    janela = ctk.CTk()
    janela.geometry("400x400")
    janela.title("Nana's Truffes - Vender")

    # Título
    titulo = ctk.CTkLabel(janela, text="Venda de Trufas", font=("Arial", 16, "bold"))
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

    # Campo para nome do comprador
    label_comprador = ctk.CTkLabel(janela, text="Comprador:")
    label_comprador.pack(pady=5)
    entry_comprador = ctk.CTkEntry(janela)
    entry_comprador.pack(pady=5)

    # Botão para registrar venda
    botao_vender = ctk.CTkButton(janela, text="Vender", command=vender)
    botao_vender.pack(pady=20)

    # Status
    label_status = ctk.CTkLabel(janela, text="")
    label_status.pack(pady=10)

    janela.mainloop()
