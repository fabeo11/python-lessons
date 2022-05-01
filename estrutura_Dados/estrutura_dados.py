lista= [12,	-2,	4,	8,	29,	45,	78,	36,	-17, 2,	12,	12,	3,	3,	-52]

maiorNumero =0
menorNumero =0
pares = []
primeiroElementoOcorrencia = 0
somaNegativos =0

media = 0




for index in range(0,len(lista)):

    if(lista[index] > maiorNumero):
        maiorNumero = lista[index]

    if(lista[index] < menorNumero):
        menorNumero = lista[index]

    if(lista[index] % 2 == 0):
        pares.append(lista[index])

    if(lista[0] == lista[index]):
        primeiroElementoOcorrencia += 1

    if(lista[index] < 0):
        somaNegativos = somaNegativos + lista[index]
    media += lista[index]


media = media / len(lista)


print("Maior Numero: {}".format(maiorNumero))
print("Menor Numero: {}".format(menorNumero))
print("Pares: {}".format(pares))
print("Ocorrencia do primeiro elemento: {}".format(primeiroElementoOcorrencia))
print("media: {}".format(media))
print("soma negativos: {}".format(somaNegativos))

