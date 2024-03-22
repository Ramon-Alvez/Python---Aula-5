import os
os.system ("cls")

print("Cálculo do restante do salário após pagar duas contas atrasadas (com multa de 2% sobre cada).")

salario = float(input("\nDigite o valor do seu salário: R$ "))
conta_1 = float(input("Digite o valor da primeira conta: R$ "))
conta_2 = float(input("Digite o valor da segunda conta: R$ "))

restante = salario - ((conta_1*1.02)+(conta_2*1.02))

print(f"\nApós pagar as duas contas, o salário restante será de R$ {restante:.2f}.")