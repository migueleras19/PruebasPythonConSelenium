import random

game = ["Piedra", "Papel", "Tijera"]
comp = random.choice(game)

jugador = False
marcador = 0
marcador_jugador = 0

while True:
    jugador = input("Piedra, Papel o tijera?").capitalize()
    
    if jugador == comp:
        print('Unir!!')
        
    elif jugador == "Piedra":
        
        if marcador == "Papel":
            print("Perdiste!", marcador, "Partida", jugador)
            marcador+=1
        else :
            print("Ganaste", jugador, "Partida", comp)
            marcador+=1
            
    elif jugador == "Papel":
        
        if comp == "Tijera":
            print("Perdiste!!", comp, "parar", jugador)
            marcador+=1
        else:
            print("You win!", jugador, "covers", comp)
            marcador_jugador+=1
    elif jugador == "Scissors":
        if comp == "Rock":
            print("You lose...", comp, "smashes", jugador)
            marcador+=1
        else:
            print("You win!", jugador, "cut", comp)
            marcador_jugador+=1
    elif jugador=='End':
        print("Final Scores:")
        print(f"CPU:{marcador}")
        print(f"Plaer:{marcador_jugador}")
        break
                        
            
            
            
        