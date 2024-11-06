from conexao import Conexao
from contato import Contato

while(True):

        print("\n# Menu com funções")
        print("1. Inserir")
        print("2. Atualizar")
        print("3. Excluir")
        print("4. Listar")

        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            conn = Conexao().conexao()
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            endereco = input("Digite o endereco do contato: ")
            contato = Contato(nome,telefone,endereco)
            if conn:
                Conexao.insert_contato(conn, contato)
                conn.close()
            input()