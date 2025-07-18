import os
import sys

if os.name == 'nt':
    import msvcrt
else:
    import termios
    import tty

def get_key():
    """Devuelve 'up', 'down', 'enter', o el carácter presionado"""
    if os.name == 'nt':
        key = msvcrt.getch()
        if key == b'\xe0':  # Tecla especial (como flechas)
            key = msvcrt.getch()
            if key == b'H':
                return 'up'
            elif key == b'P':
                return 'down'
        elif key == b'\r':
            return 'enter'
        else:
            return key.decode()
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            key = sys.stdin.read(1)
            if key == '\x1b':  # Puede ser una tecla especial
                next1 = sys.stdin.read(1)
                if next1 == '[':
                    next2 = sys.stdin.read(1)
                    if next2 == 'A':
                        return 'up'
                    elif next2 == 'B':
                        return 'down'
            elif key == '\n':
                return 'enter'
            else:
                return key
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def menu(titulo, opciones):
    seleccionado = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(titulo + "\n")

        for i, opcion in enumerate(opciones):
            if i == seleccionado:
                print(f"> {opcion} <")
            else:
                print(f"  {opcion}")

        key = get_key()
        if key == 'up':
            seleccionado = (seleccionado - 1) % len(opciones)
        elif key == 'down':
            seleccionado = (seleccionado + 1) % len(opciones)
        elif key == 'enter':
            return opciones[seleccionado]

# Ejemplo de uso
if __name__ == "__main__":
    jugadores = {
        "Jhonatan": {"name": "Jhonatan", "score": 10, "token": "X"},
        "Maria": {"name": "Maria", "score": 15, "token": "O"}
    }

    opciones = list(jugadores.keys()) + ["Nuevo jugador"]

    seleccion = menu("Selecciona un jugador:", opciones)
    print(f"\nElegiste: {seleccion}")
