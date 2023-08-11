from unittest import TestCase
import level1


class TesteLevel1(TestCase):
    def teste_recebendo_frase_retorna_numero_palavras(self):
        frase = "Realizando o primeiro teste"

        resultado_esperado = 4

        resultado_obtido = level1.contador_palavras(frase )

        self.assertEqual(resultado_esperado, resultado_obtido)

    def teste_recebendo_frase_com_caracter_especial_retorna_numero_palavras(self):
        frase = "Realizando_o_primeiro_teste"
        resultado_esperado = 4

        resultado_obtido = level1.contador_palavras(frase )

        self.assertEqual(resultado_esperado, resultado_obtido)
    
    def teste_recebendo_caracter_especial_inicio_final_frase_retorna_numero_palavras(self):
        frase = "_Realizando_o_primeiro_teste_"
        resultado_esperado = 4

        resultado_obtido = level1.contador_palavras(frase )

        self.assertEqual(resultado_esperado, resultado_obtido)
    
    def teste_recebendo_caracter_especial_repetido_retorna_numero_palavras(self):
        frase = "_Realizando_o__primeiro_teste_"
        resultado_esperado = 4

        resultado_obtido = level1.contador_palavras(frase )

        self.assertEqual(resultado_esperado, resultado_obtido)

    def teste_recebendo_multiplos_caracteres_especiais_retorna_numero_palavras(self):
        frase = "_Realizando$o#!primeiro,teste."
        resultado_esperado = 4

        resultado_obtido = level1.contador_palavras(frase )

        self.assertEqual(resultado_esperado, resultado_obtido)

    def teste_recebendo_apenas_multiplos_caracteres_especiais_retorna_numero_palavras(self):
        frase = "_$#!,."
        resultado_esperado = 0

        resultado_obtido = level1.contador_palavras(frase )

        self.assertEqual(resultado_esperado, resultado_obtido)
