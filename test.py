import os
import sys

if os.name == 'nt':
    import msvcrt
else:
    import termios
    import tty

def get_key():
    if os.name == 'nt':
        key = msvcrt.getch()
        if key == b'\xe0':  # flechas
            key = msvcrt.getch()
            return key
        return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(3)
            if key == '\x1b[A':
                return b'H'  # flecha arriba
            elif key == '\x1b[B':
                return b'P'  # flecha abajo
            else:
                return key.encode()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def menu(titulo, opciones):
    seleccionado = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(titulo)
        for i, opcion in enumerate(opciones):
            if i == seleccionado:
                print(f"> {opcion} <")
            else:
                print(f"  {opcion}")

        key = get_key()
        if key == b'H':  # flecha arriba
            seleccionado = (seleccionado - 1) % len(opciones)
        elif key == b'P':  # flecha abajo
            seleccionado = (seleccionado + 1) % len(opciones)
        elif key == b'\r':  # Enter
            return opciones[seleccionado]

# Uso del menú
opcion = menu("Selecciona una opción:", ["Ver datos", "Agregar entrada", "Eliminar entrada", "Salir"])
print(f"Elegiste: {opcion}")
