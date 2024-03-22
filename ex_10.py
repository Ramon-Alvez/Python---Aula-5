import os
os.system ("cls")

print("Cálculo da potência e a raiz de um número positivo.")

num = float(input("\nDigite um número positivo: "))

while num < 0:
    num = float(input("Digite um número positivo: "))


pot = num**2
raiz = num**0.5

print(f"\nPara o número: {num:.2f} teremos: \nPotência: {pot:.2f} \nRaiz: {raiz:.2f}.")