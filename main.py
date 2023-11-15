import os

with open("hosts.txt") as file:
    file_r = file.read()
    file_r = file_r.splitlines()

program_commands = {"-h": "Exibir comandos", "-p": "Executar ping",
                    "-s": "Encerrar o programa", "-r": "Ler os hosts do documento",
                    "-o": "Abrir hosts.txt"}
user_input = "a"


def help_command():
    keys = (program_commands.keys())
    for key in keys:
        print(f"{key}: {program_commands.get(key)}")
    input("Pressione qualquer botão para retornar")


def run_command():
    print("\n" * 100)
    for ip in file_r:
        print("*" * 100)
        os.system(f"ping -c 4 -q {ip}")
    print("*" * 100)
    input("Pressione qualquer botão para retornar")


def print_command():
    print("\n" * 100)
    print("/" * 100)
    print(os.system("cat hosts.txt"))
    print("/" * 100)
    input("Pressione qualquer botão para retornar")


def open_command():
    os.system("open hosts.txt")


def prg_run(command):
    if command in program_commands.keys():
        if command == "-h":
            help_command()
        elif command == "-r":
            print_command()
        elif command == "-o":
            open_command()
        elif command == "-p":
            run_command()
    else:
        print("Comando não encontrado. "
              "Pressione qualquer botão para retornar.")
        input()
        print("\n" * 100)


while user_input != "-s":
    print("\n" * 100)
    print("*" * 100)
    user_input = input("Pronto para execução. "
                       "Digite -h para obter lista de comandos.\n")
    prg_run(user_input)
