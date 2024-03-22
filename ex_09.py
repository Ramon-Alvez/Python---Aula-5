import os
os.system ("cls")

print("Cálculo do quanto de salário receber")

qtd_horas = float(input("\nDigite a quantidade de horas trabalhadas: "))
salario_minimo = float(input("Digite o valor do salário minimo: R$ "))

valor_hora = salario_minimo / 2
salario_bruto = qtd_horas * valor_hora
imposto = salario_bruto * 0.03
salario = salario_bruto - imposto

print(f"\nO valor do salário a ser recebido é: R$ {salario:.2f}.")
