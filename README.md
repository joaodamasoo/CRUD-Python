# 🧾 Sistema de Gerenciamento de Estoque com SQLite

Este projeto é um sistema simples de gerenciamento de estoque, desenvolvido em Python com uso de banco de dados SQLite. Ele permite realizar operações CRUD (Criar, Listar, Atualizar e Deletar produtos), com um menu interativo via terminal.

## 📦 Funcionalidades

O programa permite ao usuário:

- Criar automaticamente o banco de dados e a tabela `produtos`
- Adicionar novos produtos ao estoque
- Listar todos os produtos registrados
- Atualizar a quantidade e o preço de produtos existentes
- Deletar produtos pelo ID
- Realizar várias operações através de um menu interativo até decidir sair

---

## 🛠 Estrutura do Banco de Dados

A tabela `produtos` possui os seguintes campos:

| Campo      | Tipo     | Detalhes                                      |
|------------|----------|-----------------------------------------------|
| `id`       | INTEGER  | Chave primária com auto incremento            |
| `nome`     | TEXT     | Nome do produto, obrigatório e único          |
| `quantidade` | INTEGER | Quantidade disponível, obrigatório            |
| `preco`    | REAL     | Preço do produto, obrigatório                 |

---

## 🧩 Funções do Código

### `criar_tabela()`
- Cria a tabela `produtos` no banco de dados caso ela ainda não exista.
- Garante que o sistema esteja pronto para uso mesmo em primeira execução.

---

### `adicionar_produto()`
- Solicita ao usuário o nome, a quantidade e o preço do produto.
- Insere um novo registro no banco de dados.
- Trata erros de nome duplicado (campo `nome` é único).
- Trata valores inválidos (quantidade e preço).

---

### `listar_produtos()`
- Consulta todos os produtos cadastrados no banco.
- Exibe os dados formatados: ID, Nome, Quantidade e Preço.

---

### `atualizar_produto()`
- Solicita o ID do produto a ser alterado.
- Pede os novos valores de quantidade e preço.
- Atualiza os campos indicados no banco de dados.
- Exibe mensagem caso o ID não exista.
- Trata erros de entrada (ex: letras no lugar de números).

---

### `deletar_produto()`
- Solicita o ID do produto a ser deletado.
- Remove o produto da tabela.
- Exibe mensagem caso o ID informado não exista.
- Trata erros de entrada (valores inválidos).

---

### `menu()`
- Exibe um menu com as opções disponíveis:
  - 1: Adicionar produto
  - 2: Listar produtos
  - 3: Atualizar produto
  - 4: Deletar produto
  - 5: Sair
- Permite ao usuário realizar múltiplas operações até optar por sair.
- Chama as funções correspondentes de acordo com a escolha.

---

## 💻 Como Executar

1. Certifique-se de ter o Python instalado (versão 3.6 ou superior).
2. Execute o programa com o seguinte comando:

```bash
python estoque.py
O banco de dados estoque.db será criado automaticamente no mesmo diretório do script.
```
## 🧪 Exemplos de Testes Realizados
Teste	Resultado Esperado
  - Adicionar novo produto	Produto adicionado com sucesso
  - Adicionar produto com nome repetido	Erro tratado (nome já existe)
  - Listar produtos	Mostra todos os produtos do banco
  - Atualizar produto com ID válido	Quantidade e preço atualizados
  - Atualizar produto com ID inválido	Mensagem de produto não encontrado
  - Deletar produto com ID válido	Produto removido com sucesso
  - Deletar produto com ID inexistente	Mensagem de produto não encontrado

📌 Observações
  O sistema foi desenvolvido com foco em simplicidade e aprendizado de banco de dados com SQLite.
 
  Todos os dados são armazenados localmente no arquivo estoque.db.

👨‍💻 Desenvolvido por: 
- Ana Julia
- João Vitor Passos
- Vinicius Martin
  
Curso: Ciência da Computação

Disciplina: Linguagem e Técnicas de Programação II

Professor: FABIO SILVA RAMOS

Data: 11/04/2025
