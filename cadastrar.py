alunos = {}
orientadores = {}

def cadastrar_orientador(nome):
    if nome not in orientadores:
        orientadores[nome] = []
        print(f"Orientador '{nome}' cadastrado com sucesso!")
    else:
        print("Este orientador já foi cadastrado.")

def cadastrar_aluno(nome, matricula, orientador):
    if orientador not in orientadores:
        print("O orientador informado não está cadastrado.")
        return
    
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "orientador": orientador,
        "entregas": []
    }
    
    alunos.append(aluno)
    orientadores[orientador].append(nome)
    print(f"Aluno '{nome}' cadastrado com o orientador '{orientador}'.")
alunos = []
orientadores = {}

def cadastrar_orientador(nome):
    if nome not in orientadores:
        orientadores[nome] = []
        print(f"Orientador '{nome}' cadastrado com sucesso!")
    else:
        print("Este orientador já foi cadastrado.")

def cadastrar_aluno(nome, matricula, orientador):
    if orientador not in orientadores:
        print("O orientador informado não está cadastrado.")
        return
    
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "orientador": orientador,
        "entregas": []
    }
    
    alunos.append(aluno)
    orientadores[orientador].append(nome)
    print(f"Aluno '{nome}' cadastrado com o orientador '{orientador}'.")
