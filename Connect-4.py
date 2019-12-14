import random as rn

class Board:
    
    def __init__(self):
        self.game = [[' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ']]
        
        self.turn = 'X'
        
    def __str__(self):
        self.show = ''
        a = '\n'
        for i in range(6):
            self.show += f"{' ---'*7}{a}|"
            for j in range(7):
                self.show += f"{self.game[j][i]:^3}|"
            self.show += a
        self.show += f"{' ---'*7}"
        return self.show
        
    def next_move(self):
        if self.turn == 'X':
            self.turn = 'O'
        else: self.turn = 'X'

my_board = Board()


class Player:
    
    def __init__(self, game):
        self.game = game
    
    def do_move(self, column, turn):
        self.turn = turn
        for i in range(-1, -7, -1):
            if self.game[column-1][i] == ' ':
                self.game[column-1][i] = self.turn
                break

my_player = Player(my_board.game)


class Game:
    
    def __init__(self, game, p1, p2):
        self.playerX = p1
        self.playerO = p2
        self.game = game
        
    def check_win(self):
        
        #-----COLUMN-CHECK-----
        for i in range(7):
            for j in range(-1, -4, -1):
                lst = []
                for k in range(4):
                    lst.append(self.game[i][j-k])
                lst_s = list(set(lst))
                if len(lst_s) == 1 and lst_s[0] == self.playerX:
                    return [True , self.playerX]
                elif len(lst_s) == 1 and lst_s[0] == self.playerO:
                    return [True , self.playerO]
        
        #-----ROW-CHECK-----
        for i in range(6):
            for j in range(-1, -5, -1):
                lst = []
                for k in range(4):
                    lst.append(self.game[j-k][i])
                lst_s = list(set(lst))
                if len(lst_s) == 1 and lst_s[0] == self.playerX:
                    return [True , self.playerX]
                elif len(lst_s) == 1 and lst_s[0] == self.playerO:
                    return [True , self.playerO]
        
        #-----DIAGONAL-UP-RIGHT-CHECK-----
        for i in range(-1, -5, -1):
            for j in range(-1, -4, -1):
                lst = []
                for k in range(4):
                    lst.append(self.game[i-k][j-k])
                lst_s = list(set(lst))
                if len(lst_s) == 1 and lst_s[0] == self.playerX:
                    return [True , self.playerX]
                elif len(lst_s) == 1 and lst_s[0] == self.playerO:
                    return [True , self.playerO]
        
        #-----DIAGONAL-UP-LEFT-CHECK-----
        for i in range(4):
            for j in range(-1, -4, -1):
                lst = []
                for k in range(4):
                    lst.append(self.game[i+k][j-k])
                lst_s = list(set(lst))
                if len(lst_s) == 1 and lst_s[0] == self.playerX:
                    return [True , self.playerX]
                elif len(lst_s) == 1 and lst_s[0] == self.playerO:
                    return [True , self.playerO]
                
        return False, 'Draw'

my_game = Game(my_board.game, 'X', 'O')
def entry_not_valid(c):
    if c in range(1,8):
        return False
    else:
        return True

def start_game():
    mode = input('1. Single Player\n2. Multi Player\n')
    if mode == '1':
        com = False
        print("\nYou are player 'X'")
        while True:
            if com:
                col = rn.randint(1,7)
            else:
                col = int(input(f"\nChoose a column: "))
                if entry_not_valid(col):
                    print('Not Valid')
                    continue
            my_player.do_move(col, my_board.turn)
            my_board.next_move()
            print(my_board)
            my_game = Game(my_board.game, 'X', 'O')
            winner = my_game.check_win()
            if winner[0]:
                if winner[1] == 'X':
                    print(f"\nYou WON! :)")
                else:
                    print(f"\nYou Lost! :(")
                break
            com = not com
            
    elif mode == '2':
        while True:
            col = int(input(f"\nPlayer '{my_board.turn}' choose a column: "))
            if entry_not_valid(col):
                    print('Not Valid')
                    continue
            my_player.do_move(col, my_board.turn)
            my_board.next_move()
            print(my_board)
            my_game = Game(my_board.game, 'X', 'O')
            winner = my_game.check_win()
            if winner[0]:
                print(f"\nPlayer '{winner[1]}' WON!")
                break
                
    else:
        print("Please enter either '1' or '2'!")
        start_game()

start_game()       