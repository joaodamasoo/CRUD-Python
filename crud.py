import sqlite3


conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()


def criar_tabela():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()


def adicionar_produto():
    try:
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        cursor.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)", (nome, quantidade, preco))
        conn.commit()
        print("Produto adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: nome do produto já existe.")
    except ValueError:
        print("Erro: valores inválidos.")


def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    if produtos:
        for p in produtos:
            print(f"ID: {p[0]} | Nome: {p[1]} | Quantidade: {p[2]} | Preço: R${p[3]:.2f}")
    else:
        print("Nenhum produto cadastrado.")


def atualizar_produto():
    try:
        id_produto = int(input("ID do produto a atualizar: "))
        nova_quantidade = int(input("Nova quantidade: "))
        novo_preco = float(input("Novo preço: "))
        cursor.execute("UPDATE produtos SET quantidade = ?, preco = ? WHERE id = ?", (nova_quantidade, novo_preco, id_produto))
        if cursor.rowcount == 0:
            print("Produto não encontrado.")
        else:
            conn.commit()
            print("Produto atualizado com sucesso.")
    except ValueError:
        print("Erro: valores inválidos.")


def deletar_produto():
    try:
        id_produto = int(input("ID do produto a deletar: "))
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        if cursor.rowcount == 0:
            print("Produto não encontrado.")
        else:
            conn.commit()
            print("Produto deletado com sucesso.")
    except ValueError:
        print("Erro: ID inválido.")


def menu():
    criar_tabela()
    while True:
        print("\n--- MENU DE ESTOQUE ---")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            atualizar_produto()
        elif opcao == '4':
            deletar_produto()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    conn.close()


if __name__ == "__main__":
    menu()
