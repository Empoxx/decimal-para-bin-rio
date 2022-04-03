#colocar e definir as variaveis
numero_da_potencia = 0
numero_multiplicado = 0
numero_lista = []
numero_somado = []
numero_binario = []
lista_binario = []

numero_para_decimal = []

numero_ou_binario = str(input())

if numero_ou_binario == "b":
    
    print("Escolha um número binario")
    numero_binario = int(input())

    
    while numero_binario < 0:
        print(f"O número {numero_binario} é inválido.")
        numero_binario = int(input())

    
    binario_separado = [int(numero) for numero in str(numero_binario)]
    #print(binario_separado)

    
    binario_separado.reverse()
    

    
    for array_binario in binario_separado:
            if array_binario == 0 and array_binario < 2:
                numero_para_decimal.append(0)
                numero_da_potencia = numero_da_potencia + 1

            if array_binario == 1 and array_binario < 2:
                numero_para_decimal.append(2 ** numero_da_potencia)
                numero_da_potencia = numero_da_potencia + 1

    
    print("O numero binario escolhido foi:", numero_binario)
    print("O numero decimal desse binário é:", sum(numero_para_decimal))

        

        
if numero_ou_binario == "n":
    #inserir qql número inteiro
    print("Escolha um número inteiro")
    numero_decimal = int(input())

    
    while numero_decimal < 0:
        print(f"O número {numero_decimal} é inválido.")
        numero_decimal = int(input())

    
    while numero_multiplicado * 2 <= numero_decimal:
        numero_multiplicado = 2 ** numero_da_potencia
        numero_lista.append(numero_multiplicado)
        numero_da_potencia = numero_da_potencia + 1

    
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
    #print("a lista de potência é:", numero_somado) // ver os numeros na potencia
    print(f"O número em binário é:", ''.join(lista_binario),".")
