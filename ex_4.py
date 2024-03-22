import os
os.system("cls")

print("Cálculo de reajuste de salário de 15%")

salario = float(input("\nDigite o valor do seu salário: R$ "))

salario_reajustado = salario * 1.15

print(f"\nUm de salário de R$ {salario:.2f} com reajuste de 15% é: R$ {salario_reajustado:.2f}.")