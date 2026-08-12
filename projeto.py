import random

def corrigir_texto(texto):
    return texto.lower().strip()

def arrumar_numeros(numeros):
    return numeros.strip()

def separador_barra():
    return "=" * 130

def separador_vazio():
    return " " * 130

def opcao_valida(opcoes):
    print(separador_vazio())
    escolha_jogador = corrigir_texto(input("Escolha e digite entre pedra, papel ou tesoura: "))
    
    while escolha_jogador not in opcoes:
        print(separador_vazio())
        print(separador_barra())
        print(separador_vazio())
        print(f"ERRO: Opção ({escolha_jogador}) não é válido!")
        escolha_jogador = corrigir_texto(input("Escolha e digite entre pedra, papel ou tesoura: "))

    print(separador_vazio())
    print(separador_barra())
    
    return escolha_jogador

def mostrar_escolha(escolha_computador, escolha_jogador):
    print(f"| Sua escolha foi: ({escolha_jogador})")
    print(f"| Escolha do computador foi: ({escolha_computador})")
    
def computador(pontos_computador):
    texto = "- Computador venceu essa rodada!"
    pontos_computador += 1
    return texto, pontos_computador
    
def jogador(pontos_jogador):
    texto = "- Jogador venceu essa rodada!"
    pontos_jogador += 1
    return texto, pontos_jogador

def pedra_papel_tesoura():
    opcoes_rodadas = [3, 5, 7]
    opcoes = ["pedra", "papel", "tesoura"]
    sim_ou_nao = ["ss", "nn"]

    rodadas = int(arrumar_numeros(input("Digite a quantidade de rodadas (3 / 5 / 7): ")))
    
    while rodadas not in opcoes_rodadas:
        print(separador_vazio())
        print(separador_barra())
        print(separador_vazio())
        print(f"ERRO: Quantidade de rodadas ({rodadas}) não é válido!")
        rodadas = int(arrumar_numeros(input("Digite um valor válido para a quantidade de rodadas (3 / 5 / 7): ")))
    print(separador_vazio())
    print(separador_barra())
    
    pontos_computador = 0
    pontos_jogador = 0

    for rodadas in range(1, rodadas + 1):
        escolha_computador = random.choice(opcoes)
        escolha_jogador = opcao_valida(opcoes)

        while escolha_computador == escolha_jogador:
            print(separador_vazio())
            mostrar_escolha(escolha_computador, escolha_jogador)
            print("- Empate.")
            print("Tente novamente até desempatar.")
            print(separador_vazio())
            print(separador_barra())
            escolha_computador = random.choice(opcoes)
            escolha_jogador = opcao_valida(opcoes)
            
        if escolha_computador == "papel" and escolha_jogador == "pedra":
            print(separador_vazio())
            mostrar_escolha(escolha_computador, escolha_jogador)
            texto, pontos_computador = computador(pontos_computador)
            print(texto)
            print(separador_vazio())
            print(separador_barra())
            
        else:
            if escolha_computador == "pedra" and escolha_jogador == "tesoura":
                print(separador_vazio())
                mostrar_escolha(escolha_computador, escolha_jogador)
                texto, pontos_computador = computador(pontos_computador)
                print(texto)
                print(separador_vazio())
                print(separador_barra())
                
            else:
                if escolha_computador == "tesoura" and escolha_jogador == "papel":
                   print(separador_vazio())
                   mostrar_escolha(escolha_computador, escolha_jogador)
                   texto, pontos_computador = computador(pontos_computador)
                   print(texto)
                   print(separador_vazio())
                   print(separador_barra())
                   
                else:
                    print(separador_vazio())
                    mostrar_escolha(escolha_computador, escolha_jogador)
                    texto, pontos_jogador = jogador(pontos_jogador)
                    print(texto)
                    print(separador_vazio())
                    print(separador_barra())

    print(separador_vazio())
    
    if pontos_computador > pontos_jogador:
       print("      Vitória do Computador!")
       print(separador_vazio())
       print("|------- PLACAR FINAL -------|")
       print(f"| Computador: {pontos_computador} x {pontos_jogador} :Jogador |")
       print("|", "-" * 27, "|")
       
    else:
        print("      Vitória do Jogador!")
        print(separador_vazio())
        print("|------- PLACAR FINAL -------|")
        print(f"| Jogador: {pontos_jogador} x {pontos_computador} :Computador |")
        print("|", "-" * 27, "|")

    print(separador_vazio())
    print(separador_barra())
    print(separador_vazio())

    print("ATENÇÃO: Digite (ss) para (sim) e (nn) para (não)!")
    jogar_novamente = corrigir_texto(input("- Deseja jogar novamente?: "))

    while jogar_novamente not in sim_ou_nao:
        print(separador_vazio())
        print(separador_barra())
        print(separador_vazio())
        print(f"ERRO: Opção digitada ({jogar_novamente}) não válida!")
        jogar_novamente = corrigir_texto(input("- Digite novamente: "))
    print(separador_vazio())

    if jogar_novamente == "ss":
        print(separador_barra())
        print(separador_vazio())
        print(pedra_papel_tesoura())

    else:
        print(separador_barra())
        print(separador_vazio())
        print("- Obrigado por jogar.")
        print(separador_vazio())
    
pedra_papel_tesoura()