import os
os.system ("cls")

print("Conversor de segundos para minutos e segundos")

segundos = int(input("\nDigite os segundos para a conversão: "))

min = segundos // 60
seg = segundos % 60

print(f"\nA conversão de {segundos} segundos para minutos são: {min} minutos e {seg} segundos.")
