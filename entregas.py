from cadastrar import alunos

def formatar_data(data_str):
    if len(data_str) != 8 or not data_str.isdigit():
        raise ValueError("A data deve ser uma string com 8 dígitos, no formato DDMMAAAA.")
    return f"{data_str[4:]}/{data_str[2:4]}/{data_str[:2]}"  # AAAA/MM/DD

def registrar_entrega(nome_aluno, numero_versao, data):
    try:
        data_formatada = formatar_data(data)
    except ValueError as e:
        print(f"Erro ao formatar a data: {e}")
        return

    for aluno in alunos:
        if aluno["nome"] == nome_aluno:
            # Verifica se já existe uma entrega com o mesmo número de versão
            for entrega in aluno["entregas"]:
                if entrega[0] == numero_versao:
                    print("Já existe uma entrega com esse número de versão.")
                    return
                if entrega[2] is None:
                    print("Ainda tem uma versão pendente para avaliar.")
                    return

            aluno["entregas"].append((numero_versao, data_formatada, None))
            print(f"Entrega registrada com sucesso. Data formatada: {data_formatada}")
            return

    print("Aluno não encontrado.")

def registrar_nota(nome_aluno, numero_versao, nota):
    for aluno in alunos:
        if aluno["nome"] == nome_aluno:
            print(f"\n[DEBUG] Entregas antes da nota: {aluno['entregas']}")
            for i, entrega in enumerate(aluno["entregas"]):
                print(f"[DEBUG] Verificando entrega {i}: {entrega}")
                if entrega[0] == numero_versao and entrega[2] is None:
                    nova_tupla = (entrega[0], entrega[1], nota)
                    aluno["entregas"][i] = nova_tupla
                    print(f"Nota registrada com sucesso.")
                    print(f"[DEBUG] Entregas depois da nota: {aluno['entregas']}")
                    return
            print("Versão não encontrada ou já foi avaliada.")
            return
    print("Aluno não encontrado.")