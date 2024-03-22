import os
os.system ("cls")

print("Cálculo da variação do peso de uma pessoa se ela engordar em 15% e emagrecer 20% do seu peso original.")

peso = float(input("\nDigite o peso: "))

peso_engordado = peso * 1.15
peso_emagrecido = peso - (peso * 0.20)

print(f"\nUma pessoa de peso {peso:.1f}Kg terá: \n{peso_engordado:.1f}Kg se houver engordado em 15%; \n{peso_emagrecido:.1f}Kg se tiver emagrecido em 20%.")