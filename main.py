from cadastrar import cadastrar_orientador, cadastrar_aluno, orientadores, alunos
from entregas import registrar_entrega, registrar_nota
from relatorio import listar_alunos_por_orientador, listar_versoes_por_aluno, listar_pendencias_avaliacao, gerar_relatorio_orientador

def submenu():
    while True:
        print("\nOperações:")
        print("1 - Registrar nova entrega")
        print("2 - Registrar nota")
        print("3 - Listar alunos por orientador")
        print("4 - Listar versões entregues por aluno")
        print("5 - Listar pendências de avaliação")
        print("6 - Gerar relatório do orientador")
        print("q - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if not alunos:
                print("Nenhum aluno cadastrado.")
                continue

            print("\nEscolha um aluno para registrar a entrega:")
            nomes_alunos = [aluno["nome"] for aluno in alunos]
            for i, nome in enumerate(nomes_alunos, start=1):
                print(f"{i} - {nome}")
            escolha = input("Digite o número do aluno: ")

            if escolha.isdigit():
                indice = int(escolha) - 1
                if 0 <= indice < len(nomes_alunos):
                    nome_escolhido = nomes_alunos[indice]
                    versao = input("Número da versão: ")
                    data = input("Data (DD-MM-YYYY): ")
                    registrar_entrega(nome_escolhido, versao, data)
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida.")

        elif opcao == "2":
            if not alunos:
                print("Nenhum aluno cadastrado.")
                continue

            print("\nAlunos cadastrados:")
            for i, aluno in enumerate(alunos, start=1):
                print(f"{i} - {aluno['nome']}")

            escolha = input("Digite o número do aluno: ")
            if escolha.isdigit():
                indice = int(escolha) - 1
                if 0 <= indice < len(alunos):
                    aluno_escolhido = alunos[indice]
                    nome = aluno_escolhido["nome"]

                    if not aluno_escolhido["entregas"]:
                        print("Esse aluno ainda não tem nenhuma entrega registrada.")
                        continue

                    print("\nVersões entregues:")
                    for j, entrega in enumerate(aluno_escolhido["entregas"], start=1):
                        versao, data, nota = entrega
                        status = "pendente" if nota is None else f"nota: {nota}"
                        print(f"{j} - Versão {versao}, Data: {data}, {status}")

                    versao_escolhida = input("Digite o número da versão que deseja avaliar: ")
                    nota = float(input("Digite a nota: "))
                    registrar_nota(nome, versao_escolhida, nota)
                else:
                    print("Número de aluno inválido.")
            else:
                print("Entrada inválida.")

        elif opcao == "3":
            if not orientadores:
                print("Nenhum orientador cadastrado.")
                continue

            print("\nEscolha um orientador:")
            nomes_orientadores = list(orientadores.keys())
            for i, nome in enumerate(nomes_orientadores, start=1):
                print(f"{i} - {nome}")
            escolha = input("Digite o número do orientador: ")

            if escolha.isdigit():
                indice = int(escolha) - 1
                if 0 <= indice < len(nomes_orientadores):
                    nome_escolhido = nomes_orientadores[indice]
                    listar_alunos_por_orientador(nome_escolhido)
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida.")

        elif opcao == "4":
            if not alunos:
                print("Nenhum aluno cadastrado.")
                continue

            print("\nEscolha um aluno:")
            nomes_alunos = [aluno["nome"] for aluno in alunos]
            for i, nome in enumerate(nomes_alunos, start=1):
                print(f"{i} - {nome}")
            escolha = input("Digite o número do aluno: ")

            if escolha.isdigit():
                indice = int(escolha) - 1
                if 0 <= indice < len(nomes_alunos):
                    nome_escolhido = nomes_alunos[indice]
                    listar_versoes_por_aluno(nome_escolhido)
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida.")

        elif opcao == "5":
            listar_pendencias_avaliacao()

        elif opcao == "6":
            if not orientadores:
                print("Nenhum orientador cadastrado.")
                continue

            print("\nEscolha um orientador para gerar o relatório:")
            nomes_orientadores = list(orientadores.keys())
            for i, nome in enumerate(nomes_orientadores, start=1):
                print(f"{i} - {nome}")
            escolha = input("Digite o número do orientador: ")

            if escolha.isdigit():
                indice = int(escolha) - 1
                if 0 <= indice < len(nomes_orientadores):
                    nome_escolhido = nomes_orientadores[indice]
                    gerar_relatorio_orientador(nome_escolhido)
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida.")

        elif opcao.lower() == "q":
            break
        else:
            print("Opção inválida.")

def menu():
    while True:
        print("\nMenu Principal:")
        print("1 - Cadastrar Orientador")
        print("2 - Cadastrar Aluno")
        print("3 - Operações")
        print("q - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do orientador: ")
            cadastrar_orientador(nome)

        elif opcao == "2":
            nome = input("Nome do aluno: ")
            matricula = input("Matrícula do aluno: ")

            if not orientadores:
                print("Nenhum orientador cadastrado. Cadastre um orientador primeiro.")
                return

            print("\nEscolha um orientador da lista abaixo:")
            nomes_orientadores = list(orientadores.keys())
            for i, nome_orientador in enumerate(nomes_orientadores, start=1):
                print(f"{i} - {nome_orientador}")

            while True:
                escolha = input("Digite o número do orientador: ")
                if escolha.isdigit():
                    indice = int(escolha) - 1
                    if 0 <= indice < len(nomes_orientadores):
                        orientador_escolhido = nomes_orientadores[indice]
                        break
                    else:
                        print("Número inválido. Tente novamente.")
                else:
                    print("Entrada inválida. Por favor, digite um número.")

            cadastrar_aluno(nome, matricula, orientador_escolhido)

        elif opcao == "3":
            submenu()

        elif opcao.lower() == "q":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
