print('******************************************')
print('***Bem	vindo	ao	jogo	da	Forca!***')
print('******************************************')

palavra_secreta	= 'banana'
letras_encontradas = ['_', '_','_', '_','_', '_']

print('Fim	do	jogo')

acertou = False
enforcou = False
erros = 0


while(not acertou and not enforcou):
    chute = input("Chute uma letra:")
    if(chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_encontradas[posicao] = chute
            posicao = posicao + 1
    else:
        print("essa letra não existe na palavra secreta.")
        erros += 1

    enforcou = erros == 6
    acertou = "_" not in letras_encontradas

    print(letras_encontradas)

if(acertou):
    print("voce ganhou!")
else:
    ("voce perdeu :(")
print("fim de jogo")



