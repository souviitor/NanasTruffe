import customtkinter as ctk # Biblioteca de custom
from includeTela import abrir_tela_incluir #import da tela de incluir
from venderTela import tela_vender #import da tela de vender
from estoque import tela_estoque #import de estoque

# Criacao da janela do programa
menu = ctk.CTk()
menu.geometry('300x300')
menu.title("Nana's Truffes")

# H1 da tela do programa
texto = ctk.CTkLabel(menu, text="Nana's Truffes".upper())
texto.pack(padx=10, pady=10)

# Botoes da tela do programa
menuIncluir = ctk.CTkButton(menu, text='incluir'.upper(), command=abrir_tela_incluir)
menuIncluir.pack(padx=10, pady=20)
menuVender = ctk.CTkButton(menu, text='vender'.upper(), command=tela_vender)
menuVender.pack(padx=10, pady=20)
menuEstoque = ctk.CTkButton(menu, text='Estoque'.upper(), command=tela_estoque)
menuEstoque.pack(padx=10, pady=20)

# footer da tela do programa
footer = ctk.CTkLabel(menu, text='© VBA CO.')
footer.pack(padx=10, pady=10)

# Finalizacao da janela do programa
menu.mainloop()