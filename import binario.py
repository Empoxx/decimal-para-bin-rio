numero_decimal = int(input())
numero_da_potencia = 0
numero_multiplicado = 0
numero_lista = []
numero_somado = []
lista_binario = []


while numero_multiplicado * 2 <= numero_decimal:
    numero_multiplicado = 2 ** numero_da_potencia
    numero_lista.append(numero_multiplicado)
    numero_da_potencia = numero_da_potencia + 1

numero_lista.reverse()

#print(numero_lista)
print(f"O número decimal escolhido foi {numero_decimal}")
for numeros in numero_lista:
    if sum(numero_somado) + numeros <= numero_decimal:
        lista_binario.append("1")
        numero_somado.append(numeros)
    else:
        lista_binario.append("0")

print(f"O resultado do número decimal {numero_decimal} é:", sum(numero_somado))
print(numero_somado)
print(''.join(lista_binario))
