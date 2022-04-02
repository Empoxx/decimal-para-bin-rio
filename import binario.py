#colocar e definir as variaveis
numero_da_potencia = 0
numero_multiplicado = 0
numero_lista = []
numero_somado = []
lista_binario = []

#inserir qql número
numero_decimal = int(input())

#se for colocado negativo, nao permite que seja executado o código até ser escolhido um positivo
while numero_decimal < 0:
    print(f"O número {numero_decimal} é inválido.")
    numero_decimal = int(input())

#criar uma lista de números base 2 em funçao do numero escolhido
while numero_multiplicado * 2 <= numero_decimal:
    numero_multiplicado = 2 ** numero_da_potencia
    numero_lista.append(numero_multiplicado)
    numero_da_potencia = numero_da_potencia + 1

#inverter a ordem da lista 
numero_lista.reverse()

#pegar os números da lista e ver se cabe no numero escolhido
for numeros in numero_lista:
    if sum(numero_somado) + numeros <= numero_decimal:
        lista_binario.append("1")
        numero_somado.append(numeros)
    else:
        lista_binario.append("0")
    #print(numero_lista)

#mostrar os números
#print(f"O resultado do número decimal {numero_decimal} é:", sum(numero_somado)) //ver se o resultado da lista tá dando certo 
print(f"O número decimal escolhido foi: {numero_decimal}")
print("a lista de potência é:", numero_somado)
print(f"O número em binário é:", ''.join(lista_binario),".")
