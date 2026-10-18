
from colorama import Fore, Style, init

init(autoreset=True)

# Lista com as situações do reservatório
situacoes = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função para verificar o nível da água
def verificar_nivel(nivel):

    # Verifica se o nível é válido
    if nivel < 1 or nivel > 5:
        print("Nível inválido!")
        return

    # Define a cor de acordo com o nível
    if nivel == 1:
        cor = Fore.RED
    elif nivel == 2:
        cor = Fore.YELLOW
    elif nivel == 3:
        cor = Fore.GREEN
    elif nivel == 4:
        cor = Fore.CYAN
    else:
        cor = Fore.BLUE

    # Pega a mensagem correspondente ao nível
    mensagem = situacoes[nivel - 1]

    # Mostra as informações no terminal
    print(cor + f"Nível atual: {nivel}")
    print(cor + f"Situação: {mensagem}")

    # Volta para a cor padrão
    print(Style.RESET_ALL, end="")



# Entrada do nível do reservatório
nivel_atual = int(input("Digite o nível do reservatório (1 a 5): "))

# Verifica o nível informado
verificar_nivel(nivel_atual)
