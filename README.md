# webservices-atividade-introducao
## _Web Services – Ativida de introdução_

Implemente um programa que utilize comunicação via rede e arquitetura cliente-servidor, utilizando duas
linguagens de programação diferentes (escolha livre), conforme a figura acima.

  No programa cliente, o usuário poderá criar turmas e adicionar alunos à mesma (apenas em memória, não é
necessário utilizar persistência). Após o cadastro, os dados serão enviados para o programa servidor, que, para
cada turma, exibirá a seguinte mensagem na tela:

> A turma nome_turma de ano_turma do curso nome_curso possui qtd_alunos_turma alunos, dos quais qtd_alunos_matriculados_turma estão devidamente matriculados.

Turma
* Id (inteiro)
* Ano (inteiro)
* Curso (string)
* alunos([] Aluno)

Aluno
* Id (inteiro)
* Nome (string)
* Matriculado (booleano)

## Como usar

1. Instale o Java (Preferencialmente o [Java SE 16](https://www.oracle.com/java/technologies/javase/jdk16-archive-downloads.html)) e o [Eclipse](https://www.eclipse.org/downloads/).
2. No _Eclipse_ importe o projeto contido na pasta _Server_ e o execute.
3. Instale o [Pyhton 3](https://www.python.org/) caso não tenha.
4. Altere o _SERVER_NAME_ no arquivo _client.py_ caso seja necessário.
6. Execute o _Client/client.py_: ```python Client/client.py```
