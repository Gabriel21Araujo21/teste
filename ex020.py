from random import randint
print("=====" * 10)
print("JOGO DE PEDRA, PAPEL E TESOURA COM A MAQUINA")
print("=====" * 10)
lista = ("pedra", "papel", "tesoura")

#print(f"{lista[maquina]} e {maquina}")
while True:
    maquina = randint(0, 2)
    while True:
        while True:
            try:
                jogador = int(input("""[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Escolha seu numero: """))
                print("=====" * 10)
                if jogador in [0, 1, 2]:
                    break
                else:
                    print("tente novamente")
            except ValueError:
                print("para de digitar errado, e coloque numeros, apenas entre 0 e 2")
                printprint("=====" * 10)

        if maquina == 0:
            if jogador == 0:
                print(f"maquina escolheu{lista[maquina]} e voce escolheu {lista[jogador]}")
                print("EMPATE")
                break
            elif jogador == 1:
                print(f"a maquina escolheu {lista[maquina]} e voce escolheu {lista[jogador]}")
                print("VOCE GANHOU")
                break
            elif jogador == 2:
                print(f"a maquina escolheu {lista[maquina]} e voce escolheu {lista[jogador]}")
                print("VOCE PERDEU")
                break
        elif maquina == 1:
            if jogador == 0:
                print(f"a maquina escolheu {lista[maquina]} e voce escolheu {lista[jogador]}")
                print("VOCE PERDEU")
                break
            elif jogador == 1:
                print(f"a maquina escolheu {lista[maquina]} e voce escolheu {lista[jogador]}")
                print("EMPATE")
                break
            elif jogador == 2:
                print(f"a maquina escolheu {lista[maquina]} e voce escolheu {lista[jogador]}")
                print("VOCE GANHOU")
                break
        elif maquina == 2:
            if jogador == 0:
                print(f"a maquina escolheu {lista[maquina]} e voce escolheu {lista[jogador]}")
                print("VOCE GANHOU")
                break
            elif jogador == 1:
                print(f"a maquina escolheu {lista[maquina]} e voce escolheu {lista[jogador]}")
                print("VOCE PERDEU")
                break
            elif jogador == 2:
                print(f"a maquina escolheu {lista[maquina]} e voce escolheu {lista[jogador]}")
                print("EMPATE")
                break

            else:
                print("tente novamente apenas 0, 1 ou 2...")
    again = int(input("""Deseja jogar novamente?: 
SIM [ 1 ]
NAO [ 2 ]
DIGITE AQUI: """))
    if again == 1:
        print("=====" * 10)
    else:
        print("=====" * 10)
        print("tchau")
