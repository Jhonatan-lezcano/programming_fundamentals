# Import the random package
import random
import os

ROWS = 6
COLUMNS = 7
EMPTY_CELL = '.'



class Player:
    name = ''
    token = ''
    score = 0

    def __input_token(self, message):
        while True:
            try:
                token = input(message)
                if token.lower() != 'x' and token.lower() != 'o':
                    print('Elige un ficha entre [X] o [O]', token.lower(), token.lower() != 'x', token.lower() != 'o')
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
            self.token = 'O' if previous_player_token.lower() == 'x' else 'X' 
            print(f'{self.name}, te tocará jugar con la siguente ficha: {self.token}')

    
    def get_token(self):
        return self.token
    
    def get_name(self):
        return self.name



def init():
    """
    Initialize game
    """
    player_1 = Player()
    player_2 = Player()
    player_1.set_name('1')
    player_1.set_token()
    player_2.set_name('2')
    player_2.set_token(player_1)
    game_status = None

    return player_1, player_2, game_status

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
    print(' ', end='')
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
            print('Columna no valida')
        elif table[0][column - 1] != '.':
            print('La columna seleccionada ya está llena')
        else:
            return column - 1

def valid_row(table, column):
    index = len(table) - 1
    while index >= 0:
        if table[index][column] == '.':
            return index
        index -= 1
    return -1

def place_token(table, player, column):
    row = valid_row(table, column)
    if row == -1:
        return False
    
    table[row][column] = player.token
    return True
    



def game(table, player_1, player_2):
    current_player = choose_random_player(player_1, player_2)
    while True:

        render_table(table)
        column = print_request_column(current_player, table)
        current_place_token = place_token(table, current_player, column)
        current_player = player_1 if current_player == player_2 else player_2
    

def runGame():
    print('*** CUATRO SEGUIDAS***')
    player_1, player_2, game_status = init()
    while game_status != 'win' and game_status != 'end' :    
        table = create_table(ROWS, COLUMNS)
        game(table, player_1, player_2)


        
        # while gameStatus != "win" and gameStatus != "end":
        #     playerNumber = processInput()
        #     gameStatus, magicNumber = update(gameStatus,magicNumber,playerNumber)
        #     render(gameStatus,magicNumber)


# Launch the game
runGame()