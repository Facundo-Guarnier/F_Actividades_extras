import re


class TableroError(Exception):
    pass

class Ganador(Exception):
    pass




def ganador(tabla):
    for i in range(3):
        #Horizontal
        if tabla[i][0] == tabla[i][1] == tabla[i][2] != " ":
            raise Ganador("Ganaste horizontal")
        # vertical
        elif tabla[0][i] == tabla[1][i] == tabla[2][i] != " ":
            raise Ganador("Ganaste vertical")
    
    # Cruzado
    if tabla[0][0] == tabla[1][1] == tabla[2][2] != " " or tabla[0][2] == tabla[1][1] == tabla[2][0] != " ":
        raise Ganador("Ganaste Cruzado")

    # Lleno
    if " " not in tabla[0] and " " not in tabla[1] and " " not in tabla[2]:
        return False

    return True


class Tateti:
    def __init__(self):
        self.tablero = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        self.esta_jugando = True
        self.jugador = "X"

    @property
    def estado_tablero(self):
        tablero_limpio = ""


        # n = 0
        # for i in range(len(self.tablero)): 
        #     for k in self.tablero[i]: # Fila completa
        #         m = n % 3
        #         tablero_limpio[m] += "|{:<15}|".format(k) +"\n"
        #         n += 1
        # return tablero_limpio


        for i in self.tablero:
            tablero_limpio += str(i) + "\n"
        return tablero_limpio




    def siguiente_jugada(self, fila, columna):
        try:
            if self.jugador == "X":
                self.anotar(self.jugador, fila, columna)
                self.jugador = "O"

            elif self.jugador == "O":
                self.anotar(self.jugador, fila, columna)
                self.jugador = "X"


        except Ganador as e:
            self.esta_jugando = False
            return e
        except TableroError as e:
            return e
        except ValueError:
            return ("No es un valor valido")


    def anotar(self, jugador, fila, columna):
        fila = int(fila)
        columna = int(columna)
        if not(jugador in ["X", "O"]):
            raise TableroError("Mal el jugador")

        elif not(fila in [0, 1, 2]):
            raise TableroError("Mal las coordenadas") 

        elif not(columna in [0, 1, 2]):
            raise TableroError("Mal las coordenadas") 

        elif self.tablero[fila] [columna] != " ":
            raise TableroError("Está anotado")
        self.tablero[fila] [columna] = jugador
        self.esta_jugando = ganador(self.tablero)


def main():
    juego = Tateti()
    while juego.esta_jugando:
        print(juego.estado_tablero)
        # print(juego.tablero)
        fila = (input("Fila: "))
        columna = (input("Columna: "))
        print(juego.siguiente_jugada(fila, columna))

if __name__ == '__main__':
    main()

