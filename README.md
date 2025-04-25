Membros do grupo :

Guilherme Dorce de Britto RA:1991866
Rodrigo Shinji Yamashita RA: 2001443
Thiago Tsuyoshi Okada Aoki RA:2002282

Sistema de Acompanhamento de TCC
Objetivo
Desenvolver um sistema para a coordenação de curso acompanhar a entrega e o andamento dos Trabalhos de Conclusão de Curso (TCC). O sistema gerenciará o registro das versões entregues pelos alunos, a atribuição de notas pelos orientadores, e permitirá a visualização de pendências e relatórios de desempenho.

Funcionalidades
O sistema deve permitir as seguintes funcionalidades:

Cadastro de alunos e orientadores.

Registro de versões do TCC entregues.

Atribuição de notas pelos orientadores.

Verificação de pendências de entregas por aluno.

Relatórios para o orientador.

Visões de Funcionalidade:
Listagem de alunos por orientador.

Versões entregues por aluno (número da versão e data).

Alunos com versões não avaliadas por orientador.

Relatórios:

Média das notas dadas por aluno.

Média geral (considerando somente a última versão avaliada de cada aluno).

Alunos com pendências (sem nota atribuída).

Estrutura de Dados
Estrutura de Aluno
Cada aluno será representado por um dicionário contendo as seguintes chaves obrigatórias:

nome: (string) Nome do aluno.

matricula: (string) Matrícula do aluno.

orientador: (string) Nome do orientador do aluno.

entregas: (lista de tuplas) Cada tupla representará uma versão do TCC, onde:

1º elemento: número da versão (string).

2º elemento: data da entrega (formato YYYY-MM-DD).

3º elemento: nota atribuída (float ou None, caso não tenha sido avaliada ainda).

Estrutura de Orientador
Os orientadores serão armazenados em um dicionário, onde:

Chave: nome do orientador (string).

Valor: lista de alunos sob sua orientação (lista de strings, com os nomes dos alunos).

Funcionalidades Detalhadas
Cadastrar Orientador
A função cadastrar_orientador será responsável por adicionar orientadores ao sistema. Cada orientador terá uma lista de alunos associados.

Cadastrar Aluno
A função cadastrar_aluno será responsável por adicionar alunos ao sistema. Para cada aluno, será registrado o nome, matrícula, orientador e entregas (inicialmente vazias).

Registrar Entrega
A função registrar_entrega permitirá que um aluno registre uma nova versão do TCC. A entrega só pode ser registrada se não houver versões pendentes de correção (onde a nota seja None).

Registrar Nota
A função registrar_nota permitirá que um orientador atribua uma nota a uma versão do TCC de um aluno.

Listar Alunos por Orientador
A função listar_alunos_orientador permitirá ao orientador ver todos os alunos sob sua orientação.

Listar Versões Entregues por Aluno
A função listar_entregas_aluno permitirá ao orientador ou à coordenação ver todas as versões entregues por um aluno específico, incluindo as datas de entrega.

Listar Pendências de Avaliação
A função listar_pendencias_avaliacao permitirá ao orientador ou à coordenação ver todos os alunos com versões de TCC não avaliadas.

Gerar Relatório do Orientador
A função gerar_relatorio_orientador permitirá ao orientador gerar um relatório com a média das notas de seus alunos e a média geral considerando a última versão avaliada de cada aluno.

Instruções de Uso
Menu Principal
Ao iniciar o sistema, o usuário será apresentado ao seguinte menu:

Cadastrar orientador

Cadastrar aluno

Realizar operações (onde o usuário poderá escolher uma das funcionalidades do sistema)

Menu de Operações
Dentro da opção "Realizar operações", o usuário poderá escolher entre as seguintes funcionalidades:

Registrar nova entrega

Registrar nota

Listar alunos por orientador

Listar versões entregues por aluno

Listar pendências de avaliação

Gerar relatório do orientador

Voltar ao menu principal

Se o usuário digitar a letra "q", o programa será encerrado.

Exemplo de Execução
Cadastrar Orientador: O orientador é adicionado ao sistema.

Cadastrar Aluno: O aluno é associado a um orientador e suas entregas podem ser registradas.

Registrar Entrega: O aluno registra uma nova versão do TCC.

Registrar Nota: O orientador atribui uma nota à versão registrada.

Gerar Relatório: O orientador gera um relatório com médias e pendências.

Considerações
As entregas só podem ser registradas se não houver nenhuma pendência de avaliação.

A média geral é calculada levando em consideração apenas a última versão avaliada de cada aluno.

O programa pode ser facilmente expandido e mantido por meio da criação de funções específicas para cada operação.

Este sistema foi desenvolvido para facilitar a gestão de TCCs e o acompanhamento do progresso dos alunos, oferecendo uma interface simples e intuitiva para coordenadores e orientadores.
