def soma(valor_um, valor_dois):
    resultado = valor_um + valor_dois
    return resultado

def subtracao(valor_um, valor_dois):
    resultado = valor_um - valor_dois
    return resultado

def multiplicacao(valor_um, valor_dois):
    resultado = valor_um * valor_dois
    return resultado

def divisao(valor_um, valor_dois):
    resultado = valor_um / valor_dois
    return resultado

def calculadora(valor_um, valor_dois):
    resultado_soma = soma(valor_um, valor_dois)
    resultado_subtracao = subtracao(valor_um, valor_dois)
    resultado_multiplicacao = multiplicacao(valor_um, valor_dois)
    resultado_divisao = divisao(valor_um, valor_dois)
    return resultado_soma , resultado_subtracao , resultado_multiplicacao , resultado_divisao


#retorna uma tuple:
print(type(calculadora(100,20)))
print(calculadora(100,20))


def velocidade_media(distancia, tempo):
    velocidade = divisao(distancia,tempo)
    return velocidade

print("O resultado da velocidade média é: {} m/s".format(velocidade_media(100,20)))


