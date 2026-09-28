import string
import secrets

"""
string.ascii_letters --> Letras maiúsculas e minúsculas
string.digits --> Números
string.punctuation --> Caracteres especiais
"""

characters = string.ascii_letters + string.digits + string.punctuation

only_letters = string.ascii_letters
only_numbers = string.digits
only_especial_characters = string.punctuation

no_letters = string.digits + string.punctuation
no_numbers = string.ascii_letters + string.punctuation
no_especial_characters = string.ascii_letters + string.digits


senha = ""

qtd_characters = int(input("Digite a quantidade de caracteres que a sua senha terá: "))


print("\n--- MENU ---")
print("1 - SEM LETRAS")
print("2 - SEM NÚMEROS")
print("3 - SEM CARACTERES ESPECIAIS")
print("4 - SOMENTE LETRAS")
print("5 - SOMENTE NÚMEROS")
print("6 - SOMENTE CARACTERES ESPECIAIS")
print("7 - TODOS")

vlr_escolha = int(input("Escolha a maneira da qual deseja criar sua senha: "))

match vlr_escolha:

    case 1:
        for i in range(qtd_characters):
            senha += secrets.choice(no_letters)

    case 2:
        for i in range(qtd_characters):
            senha += secrets.choice(no_numbers)

    case 3:
        for i in range(qtd_characters):
            senha += secrets.choice(no_especial_characters)

    case 4:
        for i in range(qtd_characters):
            senha += secrets.choice(only_letters)

    case 5:
        for i in range(qtd_characters):
            senha += secrets.choice(only_numbers)

    case 6:
        for i in range(qtd_characters):
            senha += secrets.choice(only_especial_characters)

    case 7:
        for i in range(qtd_characters):
            senha += secrets.choice(characters)

print("\nSenha gerada:", senha)


