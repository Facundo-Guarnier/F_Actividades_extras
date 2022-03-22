import unittest
from parameterized import parameterized, parameterized_class
from tateti import (
    Tateti,
    TableroError,
    Ganador,
)

class TareiTestr(unittest.TestCase):

    @parameterized.expand([
        ("O", 2, 2, [[" ", " ", " "], [" ", " ", " "], [" ", " ", "O"]]),
        ("O", 1, 2, [[" ", " ", " "], [" ", " ", "O"], [" ", " ", " "]]),
        ("X", 0, 0, [["X", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
        ("X", 1, 0, [[" ", " ", " "], ["X", " ", " "], [" ", " ", " "]]),
        ("O", 2, 1, [[" ", " ", " "], [" ", " ", " "], [" ", "O", " "]]),

    ])
    def test_juego(self, jugador, fila, columna, tabla):
        juego = Tateti()
        juego.anotar(jugador, fila, columna)
        self.assertEqual(juego.tablero, tabla)


    def test_inicio(self):
        juego = Tateti()
        self.assertEqual(juego.tablero, [
                        [" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "],
                    ]
                )


    def test_anotar_bien(self):
        juego = Tateti()
        juego.anotar("X", 1, 1)     #jugador, fila, columna
        self.assertEqual(juego.tablero, [
                        [" ", " ", " "],
                        [" ", "X", " "],
                        [" ", " ", " "],
                    ]
                )

    @parameterized.expand([
        ("O", -1, 2, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
        ("O", 4, 2, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
        ("X", 0, 8, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
        ("X", 8, 0, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
        ("O", 3, 1, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
        ("X", 4, 9, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
    ])
    def test_anotar_mal_rango(self, jugador, fila, columna, tabla):
        juego = Tateti()
        with self.assertRaises(TableroError):
            juego.anotar(jugador, fila, columna)     #jugador, fila, columna
        self.assertEqual(juego.tablero, tabla)


    @parameterized.expand([
        ("O", -1, "s2", [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
        ("O", "s", 2, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
        ("X", "", 8, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
        ("X", "s", 0, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
        ("O", 3, "d", [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
        ("X", 4, "nueve", [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]),
    ])
    def test_anotar_mal_letras(self, jugador, fila, columna, tabla):
        juego = Tateti()
        with self.assertRaises(ValueError):
            juego.anotar(jugador, fila, columna)     #jugador, fila, columna
        self.assertEqual(juego.tablero, tabla)



    def test_anotar_mal2(self):
        juego = Tateti()
        juego.tablero = [
                [" ", " ", " "],
                [" ", "X", " "],
                [" ", " ", " "],
            ]

        with self.assertRaises(TableroError):
            juego.anotar("O", "1", "1")     #jugador, fila, columna
        self.assertEqual(juego.tablero, [
                        [" ", " ", " "],
                        [" ", "X", " "],
                        [" ", " ", " "],
                    ]
                )


    def test_anotar_mal3(self):
        juego = Tateti()
        with self.assertRaises(TableroError):
            juego.anotar("asdasd", 1, 2)     #jugador, fila, columna
        self.assertEqual(juego.tablero, [
                        [" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "],
                    ]
                )


    def test_ganador_vertical(self):
        juego = Tateti()
        juego.tablero = [
                [" ", "X", " "],
                [" ", "X", "O"],
                [" ", " ", "O"],
            ]
        
        with self.assertRaises(Ganador):
            juego.anotar("X", 2, 1)     #fila, columna


    def test_ganador_horizontal(self):
        juego = Tateti()
        juego.tablero = [
                [" ", "X", "X"],
                [" ", "X", "O"],
                [" ", "O", "O"],
            ]
        
        with self.assertRaises(Ganador):
            juego.anotar("X", 0, 0)     #jugador, fila, columna


    def test_ganador_cruzado(self):
        juego = Tateti()
        juego.tablero = [
                [" ", "X", "X"],
                [" ", "X", "O"],
                [" ", "O", "O"],
            ]
        
        with self.assertRaises(Ganador):
            juego.anotar("X", 2, 0)     #jugador, fila, columna




if __name__ == '__main__':
    unittest.main()