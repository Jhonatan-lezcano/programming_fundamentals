# Import the random package
import random
import os

ROWS = 6
COLUMNS = 7
EMPTY_CELL = '.'
X_TOKEN = 'x'
O_TOKEN = 'o'


class Player:
    name = ''
    token = ''
    score = 0

    def __input_token(self, message):
        while True:
            try:
                token = input(message)
                if token.lower() != X_TOKEN and token.lower() != O_TOKEN:
                    print('Elige un ficha entre [X] o [O]')
                else:
                    return token.upper()
            except ValueError:
                continue

    def set_name(self, num_player):
        name = input(f'Por favor indique nombre de participante #{num_player}: ')
        self.name = name

    def set_token(self, player = None):
        if not player: 
            token = self.__input_token(f'{self.name}, por favor indica con qué ficha deseas jugar [X] o [O]: ')
            self.token = token
        else:
            previous_player_token = player.get_token()
            self.token = O_TOKEN.upper() if previous_player_token.lower() == X_TOKEN else X_TOKEN.upper()
            print(f'{self.name}, te tocará jugar con la siguente ficha: {self.token}')

    def set_score(self, points):
        self.score += points
        
    
    def get_token(self):
        return self.token
    
    def get_name(self):
        return self.name



def init():
    player_1 = Player()
    player_2 = Player()
    player_1.set_name('1')
    player_1.set_token()
    player_2.set_name('2')
    player_2.set_token(player_1)

    return player_1, player_2

def create_table(rows, columns): 
    table = []
    for row in range(rows):
        table.append([])
        for column in range(columns):
            table[row].append(EMPTY_CELL)
    return table

def render_separator(table):
    print('+', end='')
    for s in range(1, len(table[0]) + 1):
        print('-', end='')
    print('+', end='')
    print('')

def render_table(table):
    # print(' ', end='')
    for i in range(1,len(table[0]) + 1):
        print(i, end='')
    print('')
    render_separator(table)
    for row in table:
        print('|', end='')
        for value in row:
            print(value, end='')
        print('|', end='')
        print('')
    render_separator(table)

def choose_random_player(player_1, player_2):
    print('Lanzando una moneda al aire para determinar quien inicia la partida...')
    random_player = random.choice([player_1, player_2])
    print(f'La partida la inicia {random_player.name}')
    return  random_player

def valid_int(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            continue


def print_request_column(player, table): 
    while True:
        column = valid_int(f'{player.name}, indica un número de columna o pulsa [S] para tentar a la suerte: ')
        if 0 <=column > len(table[0]):
            print(f'numero de columna no permitido, ingrese un numero entre 1 y {COLUMNS}')
        elif table[0][column - 1] != EMPTY_CELL:
            print('La columna seleccionada ya está llena')
        else:
            return column - 1

def valid_row(table, column):
    index = len(table) - 1
    while index >= 0:
        if table[index][column] == EMPTY_CELL:
            return index
        index -= 1
    return -1

def place_token(table, player, column):
    row = valid_row(table, column)
    if row == -1:
        return False
    
    table[row][column] = player.token
    return True
    
def is_draw(table):
    for column in range(len(table[0])):
        if valid_row(table, column) != -1:
            return False
    return True

def draw(player1, player2):
    print('la partida ha quedado en empate, ambos tienen 1 punto')
    player1.set_score(1)
    player2.set_score(1)

def score():
    print('''
*** TABLA DE POSICIONES ***
1. Andrea 110 puntos acumulados. Última partida en 2022-08-16 a las 13:50
2. Camilo 80 puntos acumulados. Última partida en 2021-02-25 a las 10:15
3. Tatiana 75 puntos cumulados. Última partida en 2022-08-16 a las 13:50
4. Juana 70 puntos acumulados. Última partida en 2022-05-10 a las 14:00
5. Johana 60 puntos acumulados. Última partida en 2022-05-11 a las 14:00
''')

def replay():
    while True:
        choice = input('¿Desean volver a tomar la partida Si [S] No [N]:')
        if choice.lower() == 's':
            return True
        elif choice.lower() == 'n':
            return False

def game(table, player_1, player_2):
    current_player = choose_random_player(player_1, player_2)
    while True:
        render_table(table)
        column = print_request_column(current_player, table)
        place_token(table, current_player, column)
        if is_draw(table):
            render_table(table)
            draw(player_1, player_2)
            score()
            break
        current_player = player_1 if current_player == player_2 else player_2
    

def runGame():
    print('*** CUATRO SEGUIDAS***')
    player_1, player_2 = init()
    while True :    
        table = create_table(ROWS, COLUMNS)
        game(table, player_1, player_2)
        if not replay():
            print('¡Gracias por jugar!')
            break


# Launch the game
runGame()