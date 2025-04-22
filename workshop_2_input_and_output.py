# import os
import math

# os.system('clear')

# 01
print('Hola mundo')
print('Estoy tomando contacto con el lenguaje de programacion')

# 02 
num = int(input())
print(num + 1)

# 03
string = input()
integer = int(input())
nfloat = float(input())

print(f'Mi cadena: {string}')
print(f'Mi entero: {integer}')
print(f'Mi float: {nfloat}')

# 04
degrees_fahrenheit = float(input())
def from_fahrenheit_to_celsius(degrees):
    celsius = 5 / 9 * (degrees - 32)
    return round(celsius, 2)

print(f'{degrees_fahrenheit} grados fahrenheit son {from_fahrenheit_to_celsius(degrees_fahrenheit)} grados centigrados')

# 05
base = float(input())
b = float(input())
h = float(input())

def area(base_major, b, h):
    area_result = (base_major + b) * h / 2
    return round(area_result, 3)

print(f'La figura tiene {area(base, b, h)} centimetros cuadrados')

06
age = int(input())
name = input()
weight = float(input())

print(f'Tengo {age}, me llamo {name} y peso {weight}kg')

#07

# 08
radio = float(input())
A = math.pi * radio**2
P = 2 * math.pi * radio
V = (4/3)* math.pi * radio**3

print(f'Perimetro: {P}')
print(f'Area: {A}')
print(f'Volumen: {V}')

#09
L = float(input())
D = float(input())

def pythagorean_theorem(cA, cO, h):
    if(h == None):
        hi = math.sqrt(cA**2 + cO**2)
        return hi
    elif(cA == None):
        a = math.sqrt(h**2 - cO**2)
        return a
    elif(cO == None):
        b = math.sqrt(h**2 - cA**2)
        return b

A = round(pythagorean_theorem(None, L, D) * L, 2)
    
print(A)

#10
num = input()

result = 0
str = ''
for i in range(len(num)):
    result = result + int(num[i])
    str = str + f'{num[i]} {'+ ' if i < len(num) - 1 else '=' }'

print(f'{str} {result}')

# 11
user_seconds = int(input())
seconds = user_seconds % 60
user_seconds = user_seconds - seconds

days = user_seconds // 86400
hours = (user_seconds % 86400) // 3600
mins = (user_seconds % 3600) // 60
user_seconds = user_seconds - hours * 3600

print(f'{days}:{hours:02d}:{mins:02d}:{seconds:02d}')

#12
p = float(input())
r = float(input())
t = int(input())

A = p * (1 + (r/ 12))**(12*t)
result = round(A)

print(f'El valor del capital al final del periodo es de: {result}')

#13
H = int(input())
C = int(input())

X = (H + C) % 24

print(f'La alarma sonara a las {X} horas')

#14
a = float(input())
b = float(input())
c = float(input())

sqrt = math.sqrt(b**2 - 4*a*c)
dnt = 2 * a 

x1 = (-b + sqrt) / dnt 
x2 = (-b - sqrt) / dnt

print(f'x1 = {round(x1, 3)}')
print(f'x2 = {round(x2, 3)}')