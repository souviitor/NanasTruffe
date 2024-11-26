import sqlite3

# Criar conexão e cursor
conn = sqlite3.connect('nanas_truffes.db')
cursor = conn.cursor()

# Tabela de sabores
cursor.execute("""
CREATE TABLE IF NOT EXISTS sabores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
)
""")

# Tabela de estoque
cursor.execute("""
CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sabor_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario REAL NOT NULL,
    FOREIGN KEY (sabor_id) REFERENCES sabores (id)
)
""")

# Tabela de vendas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sabor_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_total REAL NOT NULL,
    comprador TEXT NOT NULL,
    data_venda DATE NOT NULL,
    FOREIGN KEY (sabor_id) REFERENCES sabores (id)
)
""")

# Salvar alterações e fechar conexão
conn.commit()
conn.close()

def incluir_sabor(nome_sabor):
    conn = sqlite3.connect('nanas_truffes.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO sabores (nome) VALUES (?)", (nome_sabor,))
        conn.commit()
        print(f"Sabor '{nome_sabor}' incluído com sucesso.")
    except sqlite3.IntegrityError:
        print(f"Sabor '{nome_sabor}' já existe.")
    finally:
        conn.close()

def atualizar_estoque(sabor, quantidade, preco_unitario):
    conn = sqlite3.connect('nanas_truffes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM sabores WHERE nome = ?", (sabor,))
    sabor_id = cursor.fetchone()
    if sabor_id:
        cursor.execute("""
            INSERT INTO estoque (sabor_id, quantidade, preco_unitario)
            VALUES (?, ?, ?)
            """, (sabor_id[0], quantidade, preco_unitario))
        conn.commit()
        print(f"{quantidade} unidades de {sabor} adicionadas ao estoque.")
    else:
        print(f"Sabor '{sabor}' não encontrado.")
    conn.close()

def realizar_venda(sabor, quantidade, comprador, data_venda):
    conn = sqlite3.connect('nanas_truffes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, quantidade, preco_unitario FROM estoque WHERE sabor_id = (SELECT id FROM sabores WHERE nome = ?)", (sabor,))
    estoque = cursor.fetchone()
    if estoque and estoque[1] >= quantidade:
        preco_total = quantidade * estoque[2]
        cursor.execute("""
            INSERT INTO vendas (sabor_id, quantidade, preco_total, comprador, data_venda)
            VALUES (?, ?, ?, ?, ?)
        """, (estoque[0], quantidade, preco_total, comprador, data_venda))
        cursor.execute("""
            UPDATE estoque SET quantidade = quantidade - ? WHERE id = ?
        """, (quantidade, estoque[0]))
        conn.commit()
        print(f"Venda de {quantidade} unidades de {sabor} realizada com sucesso.")
    else:
        print(f"Estoque insuficiente para o sabor '{sabor}'.")
    conn.close()

def consultar_estoque():
    conn = sqlite3.connect("nanas_truffes.db")
    cursor = conn.cursor()

    # Consulta com JOIN para obter o nome do sabor
    cursor.execute("""
        SELECT sabores.nome, estoque.quantidade, estoque.preco_unitario 
        FROM estoque
        INNER JOIN sabores ON estoque.sabor_id = sabores.id
    """)
    dados = cursor.fetchall()
    conn.close()

    # Formata os dados em uma lista de dicionários
    return [{"sabor": linha[0], "quantidade": linha[1], "preco": linha[2]} for linha in dados]

def consultar_vendas(dias=15):
    from datetime import datetime, timedelta
    conn = sqlite3.connect("nanas_truffes.db")
    cursor = conn.cursor()

    # Filtra vendas dos últimos X dias
    data_limite = (datetime.now() - timedelta(days=dias)).strftime('%Y-%m-%d')

    # Consulta com JOIN para obter detalhes da venda
    cursor.execute("""
        SELECT sabores.nome, vendas.quantidade, vendas.preco_total, vendas.comprador, vendas.data_venda
        FROM vendas
        INNER JOIN sabores ON vendas.sabor_id = sabores.id
        WHERE vendas.data_venda >= ?
        ORDER BY vendas.data_venda DESC
    """, (data_limite,))
    dados = cursor.fetchall()

    # Cálculo do valor total vendido
    cursor.execute("""
        SELECT SUM(preco_total)
        FROM vendas
        WHERE data_venda >= ?
    """, (data_limite,))
    valor_total = cursor.fetchone()[0] or 0  # Se não houver vendas, retorna 0

    conn.close()

    # Formata os dados em uma lista de dicionários
    vendas = [{"sabor": linha[0], "quantidade": linha[1], "preco_total": linha[2], "comprador": linha[3], "data": linha[4]} for linha in dados]
    return vendas, valor_total
