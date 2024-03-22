import os
os.system ("cls")

print("Cálculo de média ponderada. Pesos 2, 3 e 5 respectivamente.")

n1 = float(input("\nDigite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = ((n1*2)+(n2*3)+(n3*5))/(2+3+5)

print(f"\nO aluno que obteve as notas: \n{n1:.1f}; \n{n2:.1f}; \n{n3:.1f}; \nTerá a média ponderada de {media:.1f}.")