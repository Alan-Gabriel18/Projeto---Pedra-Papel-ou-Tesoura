import random

def corrigir_texto(texto):
    return texto.lower().strip()

def arrumar_numeros(numeros):
    return numeros.strip()

def separador_arrumar():
    return "=" * 100

def opcao_valida(opcoes):
    escolha_jogador = corrigir_texto(input("Escolha e digite entre pedra, papel ou tesoura: "))

    while escolha_jogador not in opcoes:
        print("ERRO: Opção", escolha_jogador, "não é válida!")
        escolha_jogador = corrigir_texto(input("Escolha e digite entre pedra, papel ou tesoura: "))
    return escolha_jogador

def computador(pontos_computador):
    texto = "Computador venceu essa rodada!"
    pontos_computador += 1
    return texto, pontos_computador

def jogador(pontos_jogador):
    texto = "Jogador venceu essa rodada!"
    pontos_jogador += 1
    return texto, pontos_jogador

def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    opcoes_rodadas = [3, 5, 7]

    rodadas = int(arrumar_numeros(input("Digite a quantidade de rodadas (3 / 5 / 7): ")))

    while rodadas not in opcoes_rodadas:
        rodadas = int(arrumar_numeros(input("Digite um valor válido para a quantidade de rodadas (3 / 5 / 7): ")))

    print(separador_arrumar())

    pontos_computador = 0
    pontos_jogador = 0

    for rodadas in range(1, rodadas + 1):
        escolha_computador = random.choice(opcoes)
        escolha_jogador = opcao_valida(opcoes)

        print(f"Sua escolha foi: {escolha_jogador}")
        print(f"Escolha do computador foi: {escolha_computador}")

        while escolha_computador == "pedra" and escolha_jogador == "pedra" or escolha_computador == "papel" and escolha_jogador == "papel" or escolha_computador == "tesoura" and escolha_jogador == "tesoura":
            print("Empate.")
            print("Tente novamente até desempatar.")
            escolha_computador = random.choice(opcoes)
            escolha_jogador = opcao_valida(opcoes)

        if escolha_computador == "papel" and escolha_jogador == "pedra":
            texto, pontos_computador = computador(pontos_computador)
            print(texto)

        else:
            if escolha_computador == "pedra" and escolha_jogador == "tesoura":
                texto, pontos_computador = computador(pontos_computador)
                print(texto)

            else:
                if escolha_computador == "tesoura" and escolha_jogador == "papel":
                   texto, pontos_computador = computador(pontos_computador)
                   print(texto)

                else:
                    if escolha_jogador == "papel" and escolha_computador == "pedra":
                        texto, pontos_jogador = jogador(pontos_jogador)
                        print(texto)

                    else:
                        if escolha_jogador == "pedra" and escolha_computador == "papel":
                            texto, pontos_jogador = jogador(pontos_jogador)
                            print(texto)

                        else:
                            if escolha_jogador == "tesoura" and escolha_computador == "papel":
                                texto, pontos_jogador = jogador(pontos_jogador)
                                print(texto)

        if pontos_computador > pontos_jogador:
            print("Vitória do Computador!")
            print("Computador: ")




pedra_papel_tesoura()

print(pedra_papel_tesoura)