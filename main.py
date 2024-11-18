import os
import defs
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Dicionário para armazenar os estudantes
estudantes = {}

def limpa_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal

def menu_principal():
    cadastrar_RA = False  # Inicializa como False, para ser atualizado após o cadastro

    while True:
        limpa_terminal()  # Limpa o terminal antes de mostrar o menu
        print(Fore.MAGENTA + "-" * 20 + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + " ╱▔▔▔▔╲" + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + " ╱  ╭┈  ╲╮" + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + " ▏       ▔▔╲" + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + "╱╳╲   ▍ ▍   ╲" + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + "▏╳╳▏     ╭━╮▕" + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + "▏╳╳▏ ▏   ╰━╯▕" + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + "╲▂╱╲ ╲      ╱" + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + "   ▕▃▃▔▔▔▔▔▔" + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + "   ╱  ╲_" + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + " ╭┓▏▏ ▕" + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + " ┃╰▏▏ ▕" + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + " ╰╭ ▏ Snoopy khan" + Style.RESET_ALL)
        print(Fore.MAGENTA + "-" * 20 + Style.RESET_ALL)
        print(Fore.YELLOW + "░▐█▀█░▐█░▐█░▐█▀▀─░▄█▀▄─▒█▀█▀█     ▒▐█▒▐▀░▐█░▐█─░▄█▀▄─▒██▄░▒█▌" + Style.RESET_ALL)
        print(Fore.YELLOW + "░▐█──░▐████░▐█▀▀░▐█▄▄▐█░░▒█░░     ▒▐██▌░░▐████░▐█▄▄▐█▒▐█▒█▒█░" + Style.RESET_ALL)
        print(Fore.YELLOW + "░▐█▄█░▐█░▐█░▐█▄▄░▐█─░▐█░▒▄█▄░     ▒▐█▒▐▄░▐█░▐█░▐█─░▐█▒██░▒██▌" + Style.RESET_ALL)
        print()
    
        # Exibe o menu principal
        defs.exibir_menu()

        # Solicita a entrada do usuário
        opcao = input(Fore.MAGENTA + "Insira a opção: " + Style.RESET_ALL)

        if opcao == "1":
            defs.cadastrar_RA(estudantes)  # Chama a função de cadastrar RA
            cadastrar_RA = True  # Após cadastrar, muda o estado para True
        elif opcao == "2":
            defs.mostrar_RA(estudantes)  # Mostra os RAs cadastrados
        elif opcao == "3":
            if cadastrar_RA:  # Verifica se o usuário foi cadastrado
                defs.khan_attack(estudantes, cadastrar_RA)  # Chama a função khan_attack
            else:
                print(Fore.RED + "Você precisa se cadastrar primeiro!" + Style.RESET_ALL)
        elif opcao == "0":
            print(Fore.GREEN + "Saindo do sistema. Cheat concluído com sucesso!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opção inválida! Tente novamente." + Style.RESET_ALL)

        # Aguarda o usuário antes de retornar ao menu
        input(Fore.YELLOW + "Pressione Enter para continuar..." + Style.RESET_ALL)

# Executa o menu principal
menu_principal()
