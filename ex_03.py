import os
os.system("cls")

print("Cálculo do consumo médio de um veículo.")

distancia = int(input("\nDigite a distância total percorrida pelo veículo (m): "))
volume = float(input("Digite o volume de gasolina consumida no trajeto: "))

consumo = (distancia / 1000)/volume

print(f"\nO consumo médio de um veículo que percorreu {distancia:.1f}km e consumiu {volume:.1f} litros, é de: {consumo:.1f}km/l.")
