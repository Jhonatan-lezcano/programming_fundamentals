import os
os.system('cls')
#01
fee = int(input())
hours = int(input())

price = 0
for i in range(1, hours + 1):
    if i <= 5: 
        discount = fee * 0.6
        price += fee - discount
    else:
        surplus = fee / 2
        price += fee + surplus

print(f'${round(price)}')

#02
letter_1 = input()
n1 = float(input())
letter_2 = input()
n2 = float(input())

dis = n1 if letter_1 == 'D' else n2 if letter_2 == 'D' else 0.0
t = n1 if letter_1 == 'T' else n2 if letter_2 == 'T' else 0.0 
v = n1 if letter_1 == 'V' else n2 if letter_2 == 'V' else 0.0

if (letter_1 == 'D' or letter_2 == 'D') and (letter_1 == 'T' or letter_2 == 'T'): 
    print(f'V = {dis/t}')
elif (letter_1 == 'T' or letter_2 == 'T') and (letter_1 == 'V' or letter_2 == 'V'): 
    print(f'D = {t * v}')
elif (letter_1 == 'V' or letter_2 == 'V') and (letter_1 == 'D' or letter_2 == 'D'):
    print(f'T = {dis / v}')

#03
balance = int(input())
expenses = int(input())

calculation = balance + expenses

print('Si llegas a fin de mes' if calculation >= 0 else 'No llegas a fin de mes')

#04
row = int(input())
column = int(input())

sum = row + column

print('NEGRO' if sum % 2 == 0 else 'BLANCO')

#05
a = float(input())
b = float(input())
c = float(input())

is_triangle = a + b > c and a + c > b and b + c > a

triangle = 'Los lados ingresados conforman un triangulo'
not_triangle = 'Los lados ingresados no conforman un triangulo'

print(triangle if is_triangle else not_triangle)

#06
a = float(input())
b = float(input())
c = float(input())

is_triangle = a + b > c and a + c > b and b + c > a

is_equilateral = is_triangle and a == b == c
is_isosceles = is_triangle and (a == b != c or a == c != b or b == c != a)
is_scalene = is_triangle and a != b != c

if is_equilateral: 
    print('Los lados ingresados conforman un triangulo equilatero')
elif is_isosceles:
    print('Los lados ingresados conforman un triangulo isosceles')
elif is_scalene:
    print('Los lados ingresados conforman un triangulo escaleno')
else: 
    print('Los lados ingresados no conforman un triangulo')
  
#07
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
month = input()
day = int(input())

index = months.index(month)
is_spring = (index >= 2 and index <=5) and not (index == 5 and day >= 21)
is_summer = (index >= 5 and index <= 8) and not (index == 8 and day >= 22)
is_autumn = (index >= 8 and index <= 11) and not (index == 11 and day >= 21)

if(is_spring):
    print('Primavera')
elif(is_summer):
    print('Verano')
elif(is_autumn):
    print('Otono')
else:
    print('Invierno')

#08
andrea = float(input())
sandra = float(input())
milena = float(input())
values = [andrea, sandra, milena]
min = min(range(len(values)), key=values.__getitem__)
max = max(range(len(values)), key=values.__getitem__)
if (min + max == 1):
    print("Gana Milena")
elif (min + max == 2):
    print("Gana Sandra")
elif (min + max == 3):
    print("Gana Andrea")

#09
a = int(input())
b = int(input())
total = 0
if ( a <= 40):
    total = a * b
    print(f'El empleado recibira un salario de ${total}')
if ( a > 40 and a < 48):
    total = (40 * b) + ((a - 40) *(2*b))
    print(f'El empleado recibira un salario de ${total}')
if ( a > 48):
    total = (40 * b) + (8 *(2*b)) + ((a - 48) *(3*b))
    print(f'El empleado recibira un salario de ${total}')

#10
import math
a = float(input())
b = float(input())
c = float(input())
discri = b**2 - 4*a*c
if (discri >= 0):
    x = round(( -b + math.sqrt(b**2 - 4*a*c) ) / (2*a), 1)
    z = round(( -b - math.sqrt(b**2 - 4*a*c) ) / (2*a), 1)
if (discri == 0):
    print(f"La ecuacion tiene una solucion real, ella es X = {x}")
elif(discri > 0):
    print(f"La ecuacion tiene dos soluciones reales, ellas son X1 = {x} y X2 = {z}")
else:
    print("La ecuacion no tiene solucion en los reales")

#11
cash = int(input())
money = [50000, 20000, 10000, 5000, 2000, 1000]
number_cash = [0, 0, 0, 0, 0, 0]
loop = True
queue = 0
while loop:
    if cash >= money[queue]:
        number_cash[queue] += 1
        cash -= money[queue]
    elif (cash == 0):
      loop = False
    else:
      queue = queue + 1
for x, n in enumerate(number_cash):
    if n > 0:
        print(f'{n} de ${money[x]}')
