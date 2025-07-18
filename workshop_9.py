import os
os.system('cls')

#01
# n = int(input())
# print(len('a'))
# origin = dict(Galo='ix', Romano='us', Godo='ic', Griego='as', Normando='af', Bretone='is-ax', Hispano='ez', Indio='a')

# for i in range(n):
#     name = input()
#     last_letters = name[-2:] 
#     if last_letters[-1:] == 'a':
#         print('Indio')
#     elif last_letters == 'ix':
#         print('Galo')
#     elif last_letters == 'us':
#         print('Romano')
#     elif last_letters == 'ic':
#         print('Godo')
#     elif last_letters == 'as':
#         print('Griego')
#     elif last_letters == 'af':
#         print('Normando')
#     elif last_letters == 'is' or last_letters == 'ax':
#         print('Breton')
#     elif last_letters == 'ez':
#         print('Hispano')
#     else:
#         print('Desconocido')

#02
# n = int(input())
# print('A' > 'B')

# for i in range(n):
#     placas = input()
#     list_placas = placas.split(' ')
#     message = ''
#     for _, plate in enumerate(list_placas[1:]):
#         for i, letter in enumerate(plate):
#             if list_placas[1][i] > letter:
#                 message = 'Estoy viajando en el vehiculo mas modeludo del camino'
#             else:
#                 message = 'Parece que hay otro vehiculo mas modeludo en el camino'
#     print(message)     

#03    
# def es_panvocalica(palabra):
#     vocales = set("aeiou")
#     return vocales.issubset(set(palabra))

# # Leer número de palabras
# N = int(input())

# # Procesar cada palabra
# for _ in range(N):
#     palabra = input().strip()
#     if es_panvocalica(palabra):
#         print("Panvocalica")
#     else:
#         print("No panvocalica")

#04
# def verificar_circulo(cables):
#     total_macho = 0
#     total_hembra = 0

#     for cable in cables:
#         total_macho += cable.count('M')
#         total_hembra += cable.count('F')

#     if total_macho == total_hembra:
#         return "Circulo de cables"
#     else:
#         return "Circulo imposible"

# N = int(input())

# for _ in range(N):
#     linea = input().strip().split()
#     resultado = verificar_circulo(linea)
#     print(resultado)

#05
# def snake_a_camel(nombre_snake):
#     partes = nombre_snake.split('_')
#     return partes[0] + ''.join(p.capitalize() for p in partes[1:])

# N = int(input())

# for _ in range(N):
#     nombre_snake = input().strip()
#     print(snake_a_camel(nombre_snake))

#06
# with open("mensaje.txt", "r", encoding="utf-8") as archivo:
#     lineas = archivo.readlines()

# for linea in lineas:
#     linea = linea.rstrip('\n')  
#     if linea.strip(): 
#         print(linea[::-1])  

#07
# def es_cadena_completa(palabras):
#     for i in range(len(palabras) - 1):
#         palabra_actual = palabras[i]
#         siguiente = palabras[i + 1]

#         parte_final = {palabra_actual[-2:], palabra_actual[-3:]}
#         parte_inicial = {siguiente[:2], siguiente[:3]}

#         if parte_final.isdisjoint(parte_inicial): 
#             return False
#     return True

# with open("palabras.txt", "r", encoding="utf-8") as archivo:
#     lineas = archivo.readlines()

# for linea in lineas:
#     linea = linea.strip()
#     if not linea:
#         continue  

#     palabras = linea.split()
#     if es_cadena_completa(palabras):
#         print("Cadena completa")
#     else:
#         print("Cadena rota")

#08
# def es_trifelio(palabra1, palabra2):
#     n = len(palabra1)
#     for i in range(1, n):
#         parte1 = palabra1[:i]
#         parte2 = palabra1[i:]
#         fusion = parte2 + parte1
#         if fusion == palabra2:
#             return True
#     return False

# with open("trifelios.txt", "r", encoding="utf-8") as archivo:
#     lineas = archivo.readlines()

# for linea in lineas:
#     linea = linea.strip()
#     if not linea:
#         continue
#     palabra1, palabra2 = linea.split('-')
#     if es_trifelio(palabra1, palabra2):
#         print("Es trifelio")
#     else:
#         print("No es trifelio")

#09
# import re

# opositivas = [
#     "por otro lado", "a pesar de", "en cambio",
#     "mientras que", "no solo", "sin embargo"
# ]

# causativas = [
#     "hacer que", "obligar a", "convencer a",
#     "inducir a", "permitir que"
# ]

# def limpiar_texto(texto):
#     return re.sub(r'[.,;:!?]+', '', texto.lower())

# with open("discursos.txt", "r", encoding="utf-8") as archivo:
#     lineas = archivo.readlines()

# for linea in lineas:
#     linea_limpia = limpiar_texto(linea.strip())
#     op_count = sum(linea_limpia.count(expresion) for expresion in opositivas)
#     cau_count = sum(linea_limpia.count(expresion) for expresion in causativas)
#     print(f"Opositivos {op_count} Causativos {cau_count}")

#10
# binario = input().strip()

# digitos = [int(c) for c in binario]

# n = len(digitos)
# valores = [digitos[i] * (2 ** (n - 1 - i)) for i in range(n)]

# decimal = sum(valores)

# print(f"Digitos en binario: {digitos}")
# print(f"Digito x Valor Posicional: {valores}")
# print(f"Valor en decimal: {decimal}")

# def patron_letras_asteriscos(N):
#     for i in range(N):
#         asteriscos = '*' * (N - i - 1)
#         letras = ''.join(chr(65 + j) for j in range(i, -1, -1))  
#         print(asteriscos + letras)

# N = int(input())
# patron_letras_asteriscos(N)
