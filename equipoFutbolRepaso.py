
def esBuenJugador(jugador):
    goles = jugador[0]
    faltas = jugador[1]
    if goles >= 10 and faltas < 5:
        return True
    else:
        return False


def recorrerEquipo(equipo):
    for i in equipo:
        jugador = equipo[i]
        print(esBuenJugador(jugador))  


                   
equipo = {'jugador1':[10,2,3],'jugador2':[7,8,3],'jugador3':[1,2,1],'jugador4':[5,6,2],'jugador5':[9,0,4]}
recorrerEquipo(equipo)

'''
*Jugador sucio
*algún gol 
*jugaron más de 2 partidos
*cometieron alguna infracción,

def esSucio(jugador):
    goles = jugador[0]
    faltas = jugador[1]
    partidos = jgador[2]
    if goles >= 1 and faltas >= 1 and partidos > 2:
        return True
    else:
        return False 


def recorrerEquipo(equipo):
    for i in equipo:
        jugador = equipo[i]
        print(esSucio(jugador))     

'''