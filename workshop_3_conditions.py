import os
os.system('cls')
# 01
num = int(input())

is_multiplo = num % 5 == 0
message = f'El numero {num} es multiplo de 5' if is_multiplo else f'El numero {num} no es multiplo de 5'

print(message)

#02 
note = float(input())
approved = note >= 3.0
message = f'Felicitaciones, con la calificacion {note} has aprobado el curso' if approved else f'Lo lamento, la calificacion {note} no te permite aprobar el curso'
print(message)

#03
A = int(input())
B = int(input())

isMultiple = A % 117 == 0 or A % 127 == 0 or B % 117 == 0 or B % 127 == 0
message = f'Los numeros {A} y {B} tienen al planeta condenado, bien condenado' if isMultiple else f'Los numeros {A} y {B} han salvado al planeta'
print(message)

#04
Y = int(input())
X = int(input())

equation_straight_line = 3 * X + 5
belong_straight_line = Y == equation_straight_line
message = f'El punto ({X}, {Y}) pertenece a la recta Y = 3X + 5' if belong_straight_line else f'El punto ({X}, {Y}) no pertenece a la recta Y = 3X + 5'
print(message)

#05
unit_value = int(input())
apples = int(input())
message = 'El total a pagar por el cliente es'
net_worth = unit_value * apples

if(0 < apples <= 2):
    print(f'{message} ${net_worth}')
elif(3 <= apples <= 5):
    discount = net_worth * 0.1
    total_value = int(net_worth - discount)
    print(f'{message} ${total_value}')
elif(6 <= apples <= 10):
    discount = net_worth * 0.15
    total_value = int(net_worth - discount)
    print(f'{message} ${total_value}')
elif(apples >= 11):
    discount = net_worth * 0.2
    total_value = int(net_worth - discount)
    print(f'{message} ${total_value}')

#06
number = int(input())
if(number > 0):
    print('Bicicleta')
elif(number < 0):
    print('Ancheta')
else:
    print('Licuadora')

#07
amount = int(input())
desk_value = 1200000
net_worth = desk_value * amount
message = 'El valor a pagar por el cliente es'

if(0 < amount < 5):
    discount = net_worth * 0.1
    total_value = round(net_worth - discount, 1)
    print(f'{message} ${total_value}')
elif(5 <= amount < 10):
    discount = net_worth * 0.2
    total_value = round(net_worth - discount, 1)
    print(f'{message} ${total_value}')
else: 
    discount = net_worth * 0.4
    total_value = round(net_worth - discount, 1)
    print(f'{message} ${total_value}')

#08
A = int(input())
B = int(input())
C = int(input())

if(A + B == C):
    D = B + C
    print(f'Los numeros {A}, {B} y {C} podrian ser parte de la secuencia de Fibonnacci y el cuarto termino seria {D}')
else:
    print(f'Los numeros no podrian ser parte de la secuencia de Fibonacci')

# def fibonacci(num):
#     fib = []
#     for n in range(num):
#         if n < 2:
#             fib.append(int(n))
#         else:
#             Y = ((1 + math.sqrt(5)) / 2)
#             j = ((Y**n - (1 - Y)) / (math.sqrt(5)))

#             if (C<2):
#                 fib.append(int(j))
#             elif(int(j) <= C):
#               fib.append(int(j))
#             else:
#                 fib.append(fib[-1] + fib[-2])
#                 break
#     return fib

#09
P = int(input())

def message(degree, letter, isInvalid = False):
    print(f'El grado numerico {degree} corresponde al grado en letra {letter}') if not isInvalid else print(f'El valor {P} no es un grado numerico valido')

if(0 <= P < 40):
    message(P, 'F')
elif(40 <= P < 60):
    message(P, 'E')
elif(60 <= P < 70):
    message(P, 'D')
elif(70 <= P < 80):
    message(P, 'C')
elif(80 <= P < 90):
    message(P, 'B')
elif(90 <= P <= 100):
    message(P, 'A')
else:
    message(P, '', True)

#10
text = '''Vivir sin distinguir
ni Cid, ni gris visir;
dirimir si, viril,
mi gris lid incivil;
inquirir, dimitir
y sin dril inscribir:
"Vini, Vidi, Vivi"'''

l = input()

def changeLetter(letter):
    is_not_vowel = letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u'
    is_not_allowed_number = letter != '4' and letter != '3' and letter != '1' and letter != '0'
    if(is_not_vowel and is_not_allowed_number):
        print('La entrada no es correcta')
    else:
        new_text = ''''''
        for l in text:
            new_text = new_text + letter if l == 'i' else new_text + l
        
        print(new_text)
            
changeLetter(l)