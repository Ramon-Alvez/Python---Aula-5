import os
os.system ("cls")

print("Cálculo de sobra de ração após 5 dias")

peso = float(input("\nDigite o peso do saco (Kg): "))
qtd_racao = int(input("Digite a quantidade de ração (g) servida para os gatos por dia: "))

resto = (peso*1000)/((qtd_racao*2)*5)

print(f"\nO resto de ração no saco de {peso:.1f}Kg após 5 dias será de {resto:.1f}Kg.")