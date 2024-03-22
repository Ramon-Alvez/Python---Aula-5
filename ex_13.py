import os
os.system ("cls")

print("Cálculo da quantidade de ingressos mínimos para abater o custo.")

custo = float(input("\nDigite o valor total do custo do espetáculo: R$ "))
preço_convite = float(input("Digite o valor do ingresso: R$ "))

qtd_min = custo / preço_convite

print(f"\nA quantidade mínima de ingressos de R$ {preço_convite:.2f} para cobrir um espetáculo de R$ {custo:.2f} é de {qtd_min:.0f} ingressos.")