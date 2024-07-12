
def print_board (board):
    for row in board:
        print(row[0], row[1], row[2])

def build_new_board (): 
    board = [] 
    SIZE = 3
    for row in range(SIZE):
        board.append([])
        for _ in range(SIZE):
            board[row].append('.')
    return board

def get_player_input (board, player_name, turn):
    positions = [
        'tl', 'tc', 'tr',
        'cl', 'cc', 'cr',
        'bl', 'bc' ,'br'
    ]
    
    position_input = input(f'{player_name} ({turn}) - Choose your move (eg. tl, tc, tr, cl, cc, cr, bl, bc, br): ').lower()

    try:  
        position_index = positions.index(position_input)
        final_position = [0,position_index]
        if (position_index > 5):
            final_position = [2, position_index - 6]
        elif (position_index > 2):
            final_position = [1, position_index - 3]

        value_at_position = board[final_position[0]][final_position[1]]

        if value_at_position == 'o' or value_at_position == 'x':
            print('Position already taken, try again')
            return get_player_input(board, player_name, turn)
    
        return final_position
        
    except:
        print('Invalid position, try again')
        return get_player_input(board, player_name, turn)
    
def check_for_winner (board): 
    winning_lines = [
        [[0,0], [0,1], [0,2]],
        [[1,0], [1,1], [1,2]],
        [[2,0], [2,1], [2,2]],
        [[0,0], [1,0], [2,0]],
        [[0,1], [1,1], [2,1]],
        [[0,2], [1,2], [2,2]],
        [[0,0], [1,1], [2,2]],
        [[2,0], [1,1], [0,2]]
    ]

    for winning_line in winning_lines:
        matching_with = ''
        for position in winning_line:
            cell_value = board[position[0]][position[1]]
            if matching_with == '' and cell_value != '.':
                matching_with = cell_value
                
            if (cell_value != matching_with):
                matching_with = ''
                break
        
        if matching_with != '':
            return matching_with
        
def get_name_of_player_taking_turn (players, turn):
    for player in [players.get('player_one'), players.get('player_two')]:
        if player.get('piece') == turn:
            return player.get('name')
    raise Exception('Can not find player taking turn')

def increment_win_counter (players, winner):
    for player in [players.get('player_one'), players.get('player_two')]:
        if player.get('piece') == winner:
            player.update({ 'score': player.get('score') + 1 })
    return players

def print_leaderboard (players):
    print('\nLEADERBOARD')
    print('-----------')
    for player in [players.get('player_one'), players.get('player_two')]:
        print(f'{player.get("name")} - SCORE: {player.get("score")}')
        
def run_game(players):
    turn = 'o'
    gameboard = build_new_board()

    print_board(gameboard)

    while (True):
        player_name = get_name_of_player_taking_turn(players, turn)
        position = get_player_input(gameboard, player_name, turn)
        gameboard[position[0]][position[1]] = turn
        print_board(gameboard)

        winner = check_for_winner(gameboard)

        if winner:
            print(f'{winner} is the winner!')
            players = increment_win_counter(players, winner)
            print_leaderboard(players)
            return turn

        if turn == 'o':
            turn = 'x'
        else:
            turn = 'o'

def gather_player_info ():
    players = {
        'player_one': {
            'name': get_player_name('Player 1'),
            'piece': 'o',
            'score': 0
        },
        'player_two': {
            'name': get_player_name('Player 2'),
            'piece': 'x',
            'score': 0
        }
    }


    return players


def get_player_name (label): 
    name_input = input(f'Enter {label} name: ')
    if len(name_input) >= 3:
        return name_input
    
    print('Invalid name, name must be 3 or more characters in length')
    return get_player_name(label)

def invert_players_turn (players):
    player_one_piece = players.get('player_one').get('piece')
    player_two_piece = players.get('player_two').get('piece')

    players.get('player_one').update({ 
        'piece': player_two_piece
    })
    players.get('player_two').update({ 
        'piece': player_one_piece
    })
    return players




players = gather_player_info()
turn = 'player_one' 

while (True):
    run_game(players)
    players = invert_players_turn(players)
 


    








