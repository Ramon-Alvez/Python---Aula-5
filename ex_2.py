import os
os.system("cls")

print("Cálculo de tempo de download")

bits = float(input("\nInsira o tamanho do arquivo (bits): "))
bits_seg = float(input("Insira a velocidade da internet (bits/segundo): "))

tempo = bits/bits_seg

print(f"\nTempo que levará para fazer o download de {bits} de tamanho com uma velocidade de {bits_seg:.2f} bits/s é de: {tempo:.2f}s")