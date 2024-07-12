# Temos que fazer com que os numeros digitados sejam ordenados sem usar o sort()
# Definimos a lista "vazia"
lista_ordenada=[]
# colocamos um contador para parar a repetição do while
cont=0
# Abrimos a repetição do while
while cont < 5:
    n=int(input('Digite um número:'))
    lista_ordenada.append(n)
    cont+=1
    # fazemos a ordenação com "FOR" ordenando cada valor recebido
    for i in range(1,len(lista_ordenada)):
        for j in range(1,len(lista_ordenada)):
            if lista_ordenada[j] < lista_ordenada[j-1]:
                aux = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[j-1]
                lista_ordenada[j-1] = aux
# exibimos o resultado
print(f'Está é a lista ordenada sem usar "sort()" {lista_ordenada}')
    
