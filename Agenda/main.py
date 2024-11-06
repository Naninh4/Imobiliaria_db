from conexao import Conexao
from contato import Contato

while(True):

        print("\n# Menu com funções")
        print("1. Inserir")
        print("2. Atualizar")
        print("3. Excluir")
        print("4. Listar")
        print("5. Sair")

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

        elif opcao == 2:
            conn = Conexao().conexao()
            Conexao.listar_contatos(conn)
            id = int(input("\nDigite o id do contato que quer alterar: "))
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            endereco = input("Digite o endereco do contato: ")
            contato = Contato(id,nome,telefone,endereco)

            if conn:
                Conexao.alterar_contato(conn, contato)
                Conexao.select_contato_by_id(conn, id)
                conn.close()

            input()

        elif opcao == 3:
            conn = Conexao().conexao()
            Conexao.listar_contatos(conn)
            id = int(input("\nDigite o id do contato: "))
            if conn:
                Conexao.remover_contato(conn, id)
                conn.close()
            input()

        elif opcao == 4:
            conn = Conexao().conexao()
            if conn:
                Conexao.listar_contatos(conn)
                conn.close()
            input()
            
        elif opcao == 5:
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")