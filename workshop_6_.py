import os 
os.system('cls')

#01
# n = int(input())

# list_numbers = []

# for i in range(n):
#   n_add = int(input())
#   list_numbers.append(n_add)

# list_numbers.sort()
# print(list_numbers)

#02
# n = int(input())
# l = int(input())
# s = int(input())

# list_games = []
# for i in range(n): 
#   time = int(input())
  
#   if l <= time <= s: 
#     list_games.append(time)

# for i in range(l, s+1):
#   num_games = list_games.count(i)
#   print(f"{i}: {num_games}")

#03
# n = int(input())

# n_list1 = []
# n_list2 = []
# results = []

# for i in range(n):
#   n1 = float(input())
#   n_list1.append(n1)

# for i in range(n):
#   n2 = float(input())
#   n_list2.append(n2)

# for i in range(n):
#   n1 = n_list1[i]
#   n2 = n_list2[i]

#   if n1 > n2: 
#     results.append(1)
#   elif n1 < n2: 
#     results.append(2)
#   else: 
#     results.append(0)

# print(results)
# print(f'Gana 1: {results.count(1) / len(results) * 100}')
# print(f'Gana 2: {results.count(2) / len(results) * 100}')
# print(f'Igual: {results.count(0) / len(results) * 100}')

#04
# n = int(input())

# calificaciones = [float(input()) for _ in range(n)]

# promedio = sum(calificaciones) / n

# mayores = [nota for nota in calificaciones if nota > promedio]
# menores = [nota for nota in calificaciones if nota < promedio]

# print(' '.join(f"{nota:.1f}" for nota in mayores))
# print(' '.join(f"{nota:.1f}" for nota in menores))

#05
# Leer la cantidad de estudiantes que reprobaron Cálculo Integral
m = int(input())

# Leer la cantidad de estudiantes que reprobaron Álgebra Lineal
n = int(input())

# Leer los códigos de estudiantes que reprobaron Cálculo Integral
codigos_calculo = set(map(int, input().split()))

# Leer los códigos de estudiantes que reprobaron Álgebra Lineal
codigos_algebra = set(map(int, input().split()))

# Encontrar los estudiantes que reprobaron ambas materias
reprobaron_ambas = codigos_calculo & codigos_algebra  # intersección de conjuntos

# Ordenar los códigos para una salida más clara (opcional)
reprobaron_ambas = sorted(reprobaron_ambas)

# Imprimir el resultado
print("Los estudiantes que reprobaron ambas materias son:", ' '.join(map(str, reprobaron_ambas)))