import random
from datetime import datetime

ROWS = 6
COLUMNS = 7
EMPTY_CELL = '.'
X_TOKEN = 'x'
O_TOKEN = 'o'
DIRECTIONS = ['top', 'top_left', 'top_right', 'bottom', 'bottom_left', 'bottom_right', 'left', 'right']
WIN_TOKENS = 4

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
    
class Score:
    dic_players = dict()
    historical_score = []

    def add_players(self, players):
        for p in players:
            if p.name not in self.dic_players:
                self.dic_players[p.name] = p
                self.dic_players[p.name].date = datetime.now()
            else:
                self.dic_players[p.name].score = self.dic_players[p.name].score + p.score
                self.dic_players[p.name].date = datetime.now()

    def save_score_in_hist(self, hist):
        self.historical_score.append(hist)

    def print_score(self):
        sorted_score = sorted(self.dic_players.values(), key=lambda p: p.score, reverse=True)
        crr_score = []
        for i, player in enumerate(sorted_score):
            message = f'{i+1}. {player.name} {player.score} puntos acumulados. Última partida en {player.date.date()} a las {player.date.time().strftime("%H:%M %p")}' 
            print(message)
            crr_score.append(message)
        self.save_score_in_hist(crr_score)

    def export_hist(self):
        with open('historical_score.txt', 'w', encoding='utf-8') as hist:
            print('*** TABLA DE POSICIONES ***', file=hist)
            for h in self.historical_score:
                for hi in h:
                    print(hi, file=hist)
                print('', file=hist)
  
def init():
    player_1 = Player()
    player_2 = Player()
    player_1.set_name('1')
    player_1.set_token()
    player_2.set_name('2')
    player_2.set_token(player_1)
    table = create_table(ROWS, COLUMNS)

    return player_1, player_2, table

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

#region win
def count_right(row, column, table, player):
    columns = len(table[0])
    count = 0
    for i in range(column, columns):
        if count == WIN_TOKENS:
            return count
        if table[row][i] == player.token:
            count += 1
        else:
            count = 0
    return count

def count_left(row, column, table, player): 
    count = 0
    for i in range(column, -1, -1):
        if count == WIN_TOKENS:
            return count
        if table[row][i] == player.token:
            count += 1
        else:
            count: 0
    return count

def count_top(row, column, table, player):
    count = 0    
    for i in range(row, -1, -1):
        if count == WIN_TOKENS:
            return count
        if table[i][column] == player.token:
            count += 1
        else:
            count = 0
    return count

def count_top_right(row, column, table, player):
    count = 0
    irow = row
    icolumn = column
    while irow >= 0 and icolumn < len(table[0]):
        if count == WIN_TOKENS:
            return count
        if table[irow][icolumn] == player.token:
            count += 1
        else:
            count = 0
        irow -= 1
        icolumn += 1
    return 0

def count_top_left(row, column, table, player):
    count = 0
    irow = row
    icolumn = column
    while irow >= 0 and icolumn >= 0:
        if count == WIN_TOKENS:
            return count
        if table[irow][icolumn] == player.token:
            count += 1
        else:
            count = 0
        irow -= 1
        icolumn -= 1
    return 0

def count_bottom(row, column, table, player):
    count = 0
    rows = len(table)
    for i in range(row, rows):
        if count == WIN_TOKENS:
            return count
        if table[i][column] == player.token:
            count += 1
        else:
            count = 0
    return count

def count_bottom_right(row, column, table, player):
    count = 0
    irow = row
    icolumn = column
    while irow < len(table) and icolumn < len(table[0]):
        if count == WIN_TOKENS:
            return count
        if table[irow][icolumn] == player.token:
            count += 1
        else:
            count = 0
        irow += 1
        icolumn += 1
    return count

def count_bottom_left(row, column, table, player):
    count = 0
    irow = row
    icolumn = column
    while irow < len(table) and icolumn >= 0:
        if count == WIN_TOKENS:
            return count
        if table[irow][icolumn] == player.token:
            count += 1
        else:
            count = 0
        irow += 1
        icolumn -= 1
    return count

def get_count(row, column, table, player):
    for direction in DIRECTIONS:
        count_function = globals()[f'count_{direction}']
        count = count_function(row, column, table, player)
        if count >= WIN_TOKENS:
            return count
    return 0

def is_win(table, player):
    for i, row in enumerate(table):
        for j, column in enumerate(row):
            count_tokens = get_count(i, j, table, player)
            if count_tokens >= WIN_TOKENS: 
                return True
    return False 

def win_game(player):
    print(f'¡Felicitaciones, {player.name}, has ganado la partida!')
    print('Has sumado 3 puntos en esta partida')
    player.set_score(3)        
#endregion

#region draw    
def is_draw(table):
    for column in range(len(table[0])):
        if valid_row(table, column) != -1:
            return False
    return True

def draw(player1, player2):
    print('la partida ha quedado en empate, ambos tienen 1 punto')
    player1.set_score(1)
    player2.set_score(1)
#endregion

def replay():
    while True:
        choice = input('¿Desean volver a tomar la partida Si [S] No [N]:')
        if choice.lower() == 's':
            return True
        elif choice.lower() == 'n':
            return False

def game(table, player_1, player_2, score):
    current_player = choose_random_player(player_1, player_2)
    while True:
        render_table(table)
        column = print_request_column(current_player, table)
        token = place_token(table, current_player, column)
        if not token:
            print('No se puede colocar en esta columna')
        win = is_win(table, current_player)
        if win:
            render_table(table)
            win_game(current_player)
            score.add_players([player_1, player_2])
            score.print_score()
            break
        if is_draw(table):
            render_table(table)
            draw(player_1, player_2)
            score.print_score()
            break
        current_player = player_1 if current_player == player_2 else player_2
    

def runGame():
    print('*** CUATRO SEGUIDAS***')
    score = Score()
    while True :    
        player_1, player_2, table = init()
        game(table, player_1, player_2, score)
        if not replay():
            print('¡Gracias por jugar!')
            score.export_hist()
            break

# Launch the game
runGame()