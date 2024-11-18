import os
import time
from colorama import Fore, Style


def exibir_menu():
    print("===" + Fore.CYAN + " <<< Invadir sistema >>> " + Style.RESET_ALL + "===")
    print(Fore.YELLOW + "[1]" + Style.RESET_ALL + "Entre utilizando seu RA")
    print(Fore.YELLOW + "[2]" + Style.RESET_ALL + "Informações de login")
    print(Fore.YELLOW + "[3]" + Style.RESET_ALL + "Fazer atividades")
    print(Fore.YELLOW + "[0]" + Style.RESET_ALL + "Sair")
    print(Fore.CYAN + "-" * 31 + Style.RESET_ALL)


def barra_de_carregamento(mensagens, duracao=3):
    etapas = len(mensagens)  # Número de mensagens
    tempo_por_etapa = duracao / etapas  # Tempo para cada etapa

    for mensagem in mensagens:
        print(Fore.BLUE + mensagem + Style.RESET_ALL, end='', flush=True)
        for _ in range(10):  # Cada mensagem tem sua barra de 10 partes
            time.sleep(tempo_por_etapa / 10)
            print(Fore.GREEN + "|" + Style.RESET_ALL, end='', flush=True)
        print()  # Linha nova após cada etapa


def cadastrar_RA(estudantes):
    while True:
        ra = input(Fore.GREEN + "Digite o seu RA (deve conter apenas números e terminar com 'sp'): " + Style.RESET_ALL)
        
        # Verifica se é composto por números e termina com 'sp'
        if ra[:-2].isdigit() and ra.endswith("sp"):
            break
        else:
            print(Fore.RED + "Usuário não encontrado. O RA deve conter apenas números e terminar com 'sp'. Tente novamente." + Style.RESET_ALL)
    
    senha = input(Fore.GREEN + "Digite a sua senha: " + Style.RESET_ALL)
    nome = input(Fore.GREEN + "Digite o seu nome: " + Style.RESET_ALL)
    
    mensagens = [
        "Pegando informações...",
        "Validando dados...",
        "Logando na conta..."
    ]
    barra_de_carregamento(mensagens, duracao=6)
    
    estudantes[ra] = {'nome': nome, 'senha': senha}
    print(Fore.BLUE + f"Conta logada com sucesso, {nome}!\n" + Style.RESET_ALL)

def mostrar_RA(estudantes):
    if not estudantes:
        print(Fore.RED + "Você não se cadastrou ainda.\n" + Style.RESET_ALL)
    else:
        print(Fore.CYAN + "INFO:" + Style.RESET_ALL)
        for ra, dados in estudantes.items():
            email = f"0000{ra}@al.educacao.sp.gov.br"  # Gerando o e-mail
            email2 = f"0000{ra}@aluno.educacao.sp.gov.br"  # Gerando o e-mail
            print(Fore.YELLOW + f"RA: {ra}" + Style.RESET_ALL + f" - Nome: {dados['nome']} - Senha: {dados['senha']}")
            print(Fore.MAGENTA + f"Email: {email}" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"Email 2: {email2}" + Style.RESET_ALL)
        print()



def khan_attack(estudantes, cadastrar_RA):
    if cadastrar_RA:
        print(Fore.CYAN + "<<< Atividades >>>" + Style.RESET_ALL)
        print(Fore.YELLOW + "[1]" + Style.RESET_ALL + Fore.GREEN + " Fazer Khan Academy" + Style.RESET_ALL)
        print(Fore.YELLOW + "[2]" + Style.RESET_ALL + Fore.GREEN + " Fazer CMPS" + Style.RESET_ALL)
        print(Fore.YELLOW + "[3]" + Style.RESET_ALL + Fore.GREEN + " Fazer Speak" + Style.RESET_ALL)
        print(Fore.CYAN + "-" * 30 + Style.RESET_ALL)

        opcao = input(Fore.MAGENTA + "Escolha uma atividade para realizar: " + Style.RESET_ALL)

        if opcao == "1":
            mensagens = [
                "Entrando no khan academy...",
                "Iniciando atividades no Khan Academy...",
                "Realizando cálculos...",
                "Finalizando atividades..."
            ]
            barra_de_carregamento(mensagens, duracao=60)
            print(Fore.GREEN + "Atividade concluída no Khan Academy!" + Style.RESET_ALL)

        elif opcao == "2":
            print(Fore.CYAN + "<<< CMPS >>>" + Style.RESET_ALL)
            print(Fore.YELLOW + "[1]" + Style.RESET_ALL + Fore.GREEN + " Fazer atividades pendentes" + Style.RESET_ALL)
            print(Fore.YELLOW + "[2]" + Style.RESET_ALL + Fore.GREEN + " Fazer atividades expiradas" + Style.RESET_ALL)
            print(Fore.CYAN + "-" * 30 + Style.RESET_ALL)

            sub_opcao = input(Fore.MAGENTA + "Escolha uma opção: " + Style.RESET_ALL)

            if sub_opcao == "1":
                mensagens = [
                    "Calculando atividades pendentes...",
                    "Realizando atividades pendentes...",
                    "Finalizando tarefas..."
                ]
                barra_de_carregamento(mensagens, duracao=30)
                print(Fore.GREEN + "Atividade pendente concluída no CMPS!" + Style.RESET_ALL)
            elif sub_opcao == "2":
                mensagens = [
                    "Calculando atividades expiradas...",
                    "Realizando atividades expiradas...",
                    "Finalizando tarefas..."
                ]
                barra_de_carregamento(mensagens, duracao=30)
                print(Fore.GREEN + "Atividade expirada concluída no CMPS!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Opção inválida!" + Style.RESET_ALL)

        elif opcao == "3":
            print(Fore.CYAN + "<<< Speak >>>" + Style.RESET_ALL)
            print(Fore.YELLOW + "[1]" + Style.RESET_ALL + Fore.GREEN + " Fazer atividades" + Style.RESET_ALL)
            print(Fore.YELLOW + "[2]" + Style.RESET_ALL + Fore.GREEN + " Assistir vídeos" + Style.RESET_ALL)
            print(Fore.CYAN + "-" * 30 + Style.RESET_ALL)

            sub_opcao = input(Fore.MAGENTA + "Escolha uma opção: " + Style.RESET_ALL)

            if sub_opcao == "1":
                mensagens = [
                    "Entrando no speak...",
                    "Realizando exercícios...",
                    "Finalizando atividades..."
                ]
                barra_de_carregamento(mensagens, duracao=30)
                print(Fore.GREEN + "Atividade concluída no Speak!" + Style.RESET_ALL)
            elif sub_opcao == "2":
                mensagens = [
                    "Carregando vídeos no Speak...",
                    "Assistindo conteúdo...",
                    "Finalizando visualização..."
                ]
                barra_de_carregamento(mensagens, duracao=30)
                print(Fore.GREEN + "Vídeos concluídos no Speak!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Opção inválida!" + Style.RESET_ALL)

        else:
            print(Fore.RED + "Opção inválida! Tente novamente." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Você precisa se cadastrar primeiro." + Style.RESET_ALL)


