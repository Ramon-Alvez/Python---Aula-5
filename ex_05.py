import os
os.system("cls")

print("Cálculo de aumento de salário")

salario = float(input("\nDigite o valor do seu salário: R$ "))
percentual = float(input("Digite o percentual de aumento: % "))

salario_reajustado = salario + (salario * (percentual/100))

print(f"\nO salário de R$ {salario:.2f} com um aumento de {percentual:.1f}% fica R$ {salario_reajustado:.2f}.")
