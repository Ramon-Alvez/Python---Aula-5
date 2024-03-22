import os
os.system("cls")

print("Cálculo de área (m²) e a potência necessária para a iluminação dos cômodos.")

l1 = float(input("\nDigite o tamanho lateral do cômodo(m): "))
l2 = float(input("Digite o tamanho frontal do cômodo(m): "))

area = l1 * l2
pot = area * 18

print(f"\nUm cômodo de {l1:.1f}x{l2:.1f}m terá uma área de {area:.1f}m² e será necessária uma potência de {pot:.1f}W para a iluminação.")