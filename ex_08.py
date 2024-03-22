import os
os.system ("cls")

print("Cálculo da hipotenusa")

a = float(input("\nDigite o valor do primeiro cateto: "))
b = float(input("Digite o valor do segundo cateto: "))

hip = ((a**2)+(b**2))**0.5

print(f"\nUm triângulo retângulo de lados: \na = {a:.2f} \nb = {b:.2f} \nO valor da hipotenusa é {hip:.2f}.")
