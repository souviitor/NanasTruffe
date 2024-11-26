import customtkinter as ctk
from backend import consultar_estoque, consultar_vendas

def tela_estoque():
    def atualizar_estoque():
        # Limpa a área de texto
        texto_relatorio.delete(1.0, "end")

        # Consulta e insere os dados do estoque formatados
        estoque = consultar_estoque()
        if estoque:
            texto_relatorio.insert("end", f"{'Sabor':<30}{'Quantidade':<15}{'Preço (R$)':<10}\n")
            texto_relatorio.insert("end", "-" * 55 + "\n")
            for item in estoque:
                texto_relatorio.insert("end", f"{item['sabor']:<30}{item['quantidade']:<15}{item['preco']:<10.2f}\n")
        else:
            texto_relatorio.insert("end", "Estoque vazio.\n")

    def consultar_vendas_periodo():
        # Limpa a área de texto
        texto_relatorio.delete(1.0, "end")

        # Consulta os dados das vendas e o valor total vendido
        vendas, valor_total = consultar_vendas(15)
        if vendas:
            texto_relatorio.insert("end", f"{'Sabor':<30}{'Quantidade':<15}{'Comprador':<20}{'Data':<15}\n")
            texto_relatorio.insert("end", "-" * 80 + "\n")
            for venda in vendas:
                texto_relatorio.insert(
                    "end", 
                    f"{venda['sabor']:<30}{venda['quantidade']:<15}{venda['comprador']:<20}{venda['data']:<15}\n"
                )
            texto_relatorio.insert("end", "-" * 80 + "\n")
            texto_relatorio.insert("end", f"Total vendido nos últimos 15 dias: R$ {valor_total:.2f}\n")
        else:
            texto_relatorio.insert("end", "Nenhuma venda nos últimos 15 dias.\n")

    # Configuração da janela
    janela = ctk.CTk()
    janela.geometry("600x600")
    janela.title("Nana's Truffes - Estoque e Relatórios")

    # Título
    titulo = ctk.CTkLabel(janela, text="Estoque e Relatórios", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    # Botões
    botao_estoque = ctk.CTkButton(janela, text="Mostrar Estoque", command=atualizar_estoque)
    botao_estoque.pack(pady=10)

    botao_vendas = ctk.CTkButton(janela, text="Vendas dos Últimos 15 Dias", command=consultar_vendas_periodo)
    botao_vendas.pack(pady=10)

    # Área de texto para exibir os relatórios
    texto_relatorio = ctk.CTkTextbox(janela, width=550, height=400, wrap="none")
    texto_relatorio.pack(pady=10)

    janela.mainloop()

# Chamando a tela
tela_estoque()
