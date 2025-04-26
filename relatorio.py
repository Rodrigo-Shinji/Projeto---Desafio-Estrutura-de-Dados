from cadastrar import alunos, orientadores

def listar_alunos_por_orientador(nome_orientador):
    if nome_orientador in orientadores:
        print("Alunos orientados por", nome_orientador)
        for nome in orientadores[nome_orientador]:
            print("-", nome)
    else:
        print("Orientador não encontrado.")

def listar_versoes_por_aluno(nome_aluno):
    for aluno in alunos:
        if aluno["nome"] == nome_aluno:
            print("Versões de", nome_aluno)
            for entrega in aluno["entregas"]:
                versao = entrega[0]
                data = entrega[1]
                nota = entrega[2]
                if nota is not None:
                    print(f"Versão {versao}, Data: {data}, Nota: {nota}")
                else:
                    print(f"Versão {versao}, Data: {data}, Nota: (pendente)")
            return
    print("Aluno não encontrado.")

def listar_pendencias_avaliacao():
    for aluno in alunos:
        tem_pendencia = False
        for entrega in aluno["entregas"]:
            if entrega[2] == None:
                tem_pendencia = True
                break
        if tem_pendencia:
            print(f"{aluno['nome']} (orientador: {aluno['orientador']}) tem entregas pendentes.")
            
        else:
            print("Não há entregas pendentes")

def gerar_relatorio_orientador(nome_orientador):
    if nome_orientador not in orientadores:
        print("Orientador não encontrado.")
        return

    total_notas = 0
    total_alunos_com_media = 0

    print(f"Relatório de {nome_orientador}:")
    for nome_aluno in orientadores[nome_orientador]:
        for aluno in alunos:
            if aluno["nome"] == nome_aluno:
                entregas_avaliadas = [entrega for entrega in aluno["entregas"] if entrega[2] is not None]

                if entregas_avaliadas:
                    print(f"- {nome_aluno}:")
                    soma_notas = 0
                    for entrega in entregas_avaliadas:
                        print(f"    Versão {entrega[0]}, Data: {entrega[1]}, Nota: {entrega[2]}")
                        soma_notas += entrega[2]
                    media = soma_notas / len(entregas_avaliadas)
                    print(f"    Média: {media:.2f}")
                    ultima_versao_avaliada = max(entregas_avaliadas, key=lambda e: e[0])
                    total_notas += ultima_versao_avaliada[2]
                    total_alunos_com_media += 1
                else:
                    print(f"- {nome_aluno}: nenhuma versão avaliada.")

    if total_alunos_com_media > 0:
        media_geral = total_notas / total_alunos_com_media
        print(f"\nMédia geral (considerando última versão avaliada de cada aluno): {media_geral:.2f}")
    else:
        print("Nenhuma versão avaliada para calcular média geral.")