# 01
# num = int(input())

# is_multiplo = num % 5 == 0
# message = f'El numero {num} es multiplo de 5' if is_multiplo else f'El numero {num} no es multiplo de 5'

# print(message)

#02 
# note = float(input())
# approved = note >= 3.0
# message = f'Felicitaciones, con la calificacion {note} has aprobado el curso' if approved else f'Lo lamento, la calificacion {note} no te permite aprobar el curso'
# print(message)

#03
A = int(input())
B = int(input())

isMultiple = A % 117 == 0 or A % 127 == 0 or B % 117 == 0 or B % 127 == 0
message = f'Los numeros {A} y {B} tienen al planeta condenado, bien condenado' if isMultiple else f'Los numeros {A} y {B} han salvado al planeta'
print(message)