from models import Turma, Aluno
import json
import socket

SERVER_NAME = '127.0.0.1'
SERVER_PORT = 12000

# Transforma uma lista de turmas em uma string no formato json.
def turmas_to_json(turmas):
    turmas_dict = {}
    turmas_dict['turmas'] = [turma.to_dict() for turma in turmas]
    return json.dumps(turmas_dict)

# Envia a lista de turmas passada para o servidor.
def send_turmas(turmas):
    # Transformando a lista de turmas em uma string no formato json.
    msg = turmas_to_json(turmas)
    
    try:
        # Iniciando a conexão com o servidor.
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_NAME, SERVER_PORT))

        # Enviando a mensagem para o servidor.
        client_socket.sendall(msg.encode('utf-8'))

        client_socket.close()

    except:
        print("\nErro na comunicação com o servidor!\n")

# Lê uma string não vazia.
def ler_string(msg="Digite o valor do campo: ", msg_vazio="O campo não pode ser vazio!"):
    while True:
        entrada = input(msg)
        if(entrada and not entrada.isspace()):
            return entrada
        print(msg_vazio)

# Lê um número inteiro.
def ler_inteiro(msg="Digite um valor inteiro: ", msg_nao_inteiro="Você deve digitar um valor inteiro!"):
    while True:
        entrada = ler_string(msg)
        if entrada.isdigit():
            return int(entrada)
        print(msg_nao_inteiro)

# Lê um ano.
def ler_ano(msg="Digite o ano: ", msg_ano_invalido="Ano inválido! Você deve digitar um valor inteiro positivo!"):
    while True:
        entrada = ler_inteiro(msg, msg_ano_invalido)
        if entrada > 0:
            return entrada
        print(msg_ano_invalido)

# Exibe um menu com as opções passadas e retorna o número da opção escolhida.
def menu_opcoes(opcoes, msg_erro = "Opção inválida!"):
    while True:
        try:
            menu = ""
            for i, opcao in enumerate(opcoes):
                menu += "{} - {}\n".format(i + 1, opcao)

            opcao = int(input(menu + "\nOpção escolhida: "))
            print()

            if(opcao > 0 and opcao <= len(opcoes)):
                return opcao
                
        except ValueError:
            pass

        print(msg_erro)

# Lê os dados de uma turma.
def ler_turma():
    turma = Turma()
    turma.id = ler_inteiro("Digite o id da turma: ")
    turma.nome = ler_string("Digite o nome da turma: ")
    turma.ano = ler_ano("Digite o ano da turma: ")
    turma.curso = ler_string("Digite o curso da turma: ")
    
    turma.alunos = []
    print("\nAlunos da turma: \n")
    while True:
        turma.alunos.append(ler_aluno())
        
        print()

        if(menu_opcoes(["Adicionar outro aluno", "Finalizar cadastro da turma"]) == 2):
            break
    return turma

# Lê os dados de um aluno.
def ler_aluno():
    aluno = Aluno()
    aluno.id = ler_inteiro("Digite o id do aluno: ")
    aluno.nome = ler_string("Digite o nome do aluno: ")
    print("\nO aluno está matriculado?")
    aluno.matriculado = True if menu_opcoes(["Sim", "Não"]) == 1 else False

    return aluno

def main():
    try:
        turmas = []
        print()
        while True:
            turmas.append(ler_turma())

            if(menu_opcoes(["Cadastrar outra turma", "Finalizar cadastro"]) == 2):
                break
            
        send_turmas(turmas)
    except KeyboardInterrupt:
        pass 

if __name__ == "__main__":
    main()