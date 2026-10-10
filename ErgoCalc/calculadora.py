import math


def validar_medidas(altura_poplitea, altura_cotovelo, altura_joelho, sapato, altura_cadeira):
    if altura_poplitea <= 0 or altura_cotovelo <= 0 or altura_joelho <= 0 or sapato < 0 or altura_cadeira <= 0:
        return False
    else:
        return True


def calcular(altura_poplitea, altura_cotovelo, altura_joelho, sapato, altura_cadeira):

    if validar_medidas(altura_poplitea, altura_cotovelo, altura_joelho, sapato, altura_cadeira) == True:
        print("Medidas válidas.")
        print(f"Altura poplítea: {altura_poplitea} cm")
        print(f"Altura do cotovelo: {altura_cotovelo} cm")
        print(f"Altura do joelho: {altura_joelho} cm")

        altura_minima = (altura_poplitea + sapato) * math.cos(math.radians(30))
        altura_maxima = (altura_poplitea + sapato) * math.cos(math.radians(5))
        altura_media = (altura_minima + altura_maxima) / 2

        print(f"Altura mínima: {altura_minima:.2f} cm")
        print(f"Altura máxima: {altura_maxima:.2f} cm")
        print(f"Altura média da faixa: {altura_media:.2f} cm")

        if altura_cadeira < altura_minima:
            diferenca = altura_minima - altura_cadeira
            avaliacao = f"A cadeira está baixa demais em {diferenca:.2f} cm."

        elif altura_cadeira > altura_maxima:
            diferenca = altura_cadeira - altura_maxima
            avaliacao = f"A cadeira está alta demais em {diferenca:.2f} cm."

        else:
            avaliacao = "A altura da cadeira está dentro da faixa calculada."

        return avaliacao

    else:
        return "Medidas inválidas."