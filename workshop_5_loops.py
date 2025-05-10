import os
os.system('clear')

# 01
# n = int(input())

# for i in range(n):
#     print('Hola mundo') 
#     print('Estoy tomando contacto con el lenguaje de programacion')

#02
# m = int(input())
# n = int(input())

# for i in range(1, n + 1):
#     result = m * i
#     print(f'{m} x {i} = {result}')

n_bacteria = int(input())

hours = 0

while n_bacteria > 10:
    n_bacteria = n_bacteria /2
    hours += 1

print(hours)