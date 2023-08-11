import re

def contador_palavras(frase):
    frase_tratada = re.sub(r"[^A-Za-z]+", ' ', frase)
    resultado = len(frase_tratada.split())
    return resultado
