# -*- coding: utf-8 -*-

import re

# Diccionario para convertir dígitos a superíndices
superindice_map = {
    '0': '⁰',
    '1': '¹',
    '2': '²',
    '3': '³',
    '4': '⁴',
    '5': '⁵',
    '6': '⁶',
    '7': '⁷',
    '8': '⁸',
    '9': '⁹'
}

def convertir_a_superindice(numero):
    """Convierte una cadena de dígitos a su equivalente en superíndices."""
    return ''.join(superindice_map[d] for d in numero)

def procesar_archivo(entrada, salida):
    """Lee un archivo, convierte [n] a superíndices, y guarda el resultado en otro archivo."""
    with open(entrada, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Buscar patrones [n] y reemplazar con superíndices
    contenido_modificado = re.sub(r'\[(\d+)\]', lambda m: convertir_a_superindice(m.group(1)), contenido)

    with open(salida, 'w', encoding='utf-8') as f:
        f.write(contenido_modificado)

    print("El archivo ha sido procesado y guardado en '{}'.".format(salida))

# Ejemplo de uso
entrada = 'entrada.txt'  # Cambia por el nombre de tu archivo de entrada
salida = 'salida.txt'    # Cambia por el nombre del archivo de salida
procesar_archivo(entrada, salida)


# Usar
# python3 convertir_superindice.py
# python convertir_superindice.py

# Diccionario para convertir dígitos a superíndices