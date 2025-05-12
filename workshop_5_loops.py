import os
import math
os.system('cls')


# 01
# n = int(input())

# for i in range(n):
#     print('Hola mundo') 
#     print('Estoy tomando contacto con el lenguaje de programacion')

#023
# m = int(input())
# n = int(input())

# for i in range(1, n + 1):
#     result = m * i
#     print(f'{m} x {i} = {result}')

#03

# n_bacteria = int(input())

# hours = 0

# while n_bacteria > 10:
#     n_bacteria = n_bacteria /2
#     hours += 1

# print(hours)

#04 
# n = int(input())
# area = 0
# l_sum = 0

# while n > 0 :
#     l = float(input())
#     l_sum = l_sum + l
#     area = area + l_sum**2
#     n -= 1


# print(f'Ramon, el area total de la estructura basica del universo es de {round(area, 2)} centimetros cuadrados')

#05
# maximum_load = float(input())
# n_sacks = int(input())
# weights = []

# for i in range(n_sacks):
#     weight_sack = float(input())
#     weights.append(weight_sack)

# acc = 0
# weight_sacks = 0
# for i in weights:
#     weight_sacks += i
#     if weight_sacks > maximum_load:
#         break
#     acc += 1

# print(f'Caben {acc} bultos de papa')

#06
# n = input()
# n_list = ''
# for i in n:
#    n_list = f'{i}{n_list}'

# print(int(n_list))

#07
# n = int(input())
# succession = 17

# for i in range(n):
#     print(succession)
#     succession = succession - 2 if i % 2 == 0 else succession + 3 

#08 
# n = int(input())
# acc = 0
# for i in range(n):
#     number = int(input())
#     is_not_prime = False
#     if number > 1:
#         for j in range(2, number):
#             if number % j == 0:
#                 is_not_prime = True
#                 break
#         acc = acc if is_not_prime else acc + 1 
    
# print(acc)

#09
# acc = 0
# count = 0
# n = int(input())
# for i in range(n): 
#     number = int(input())
#     is_compound = False
#     if number > 1:
#         for j in range(2, number):
#             if number % j == 0: 
#                 is_compound = True
#                 break

#     print(is_compound)
#     acc = acc + number if is_compound else acc
#     count = count + 1 if is_compound else count

# print(round(acc / count, 1) if acc > 0 and count > 0 else 0)

#10
# n = input()
# n_list = []
# for i in n:
#     n_list.append(int(i))

# n_list.sort(reverse=True)

# print(n_list[0] - n_list[-1])

#11
# char = '*'
# l = int(input())
# middle_list = math.ceil(l/2)

# for i in range(1, l + 1):
#     if i <= middle_list:
#         print(char * i)

# for j in range(middle_list -1, 0, -1):
#     print(char * j)

#12
rows = int(input())
columns = int(input())

for c in range(columns + 1):
    print(c if c > 0 else '', end='\t' if c < columns else '\n')

print('')

for row in range(1, rows + 1):
    print(row, end='\t')
    for column in range(1, columns + 1):
        print(row * column, end='\t' if column < columns else '\n')

print(0.2 + 0.1 == 0.3)