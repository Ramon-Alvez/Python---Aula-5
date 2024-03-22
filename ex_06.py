import os
os.system("cls")

print("Cálculo da idade atual de uma pessoa, e sua idade em 2030")

ano_nascimento = int(input("\nDigite o seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento
idade_2030 = 2030 - ano_nascimento

print(f"A idade de uma pessoa que nasceu em {ano_nascimento} está por volta dos {idade} anos, e sua idade em 2030 será por volta dos {idade_2030} anos.")
