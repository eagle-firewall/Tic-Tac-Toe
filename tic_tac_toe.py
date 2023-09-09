struct = ['-' for i in range(9)]
def print_board(option, player,fn_name):
  if struct[option] != '-':
        print('This place is already filled, Enter correct option. ')
        fn_name()
  else:
    struct[option] = player
    if all(k in ('o','x') for k in struct) and not(validate_move(player)):
        print('match draw')
        exit()
    else:
     board = f'''|{struct[0]}| |{struct[1]}| |{struct[2]}|
|{struct[3]}| |{struct[4]}| |{struct[5]}|
|{struct[6]}| |{struct[7]}| |{struct[8]}|'''
     print(board)
def validate_move(player):
    winning_conditions = [struct[0:3], struct[3:6], struct[6:9],struct[0:9:3], struct[1:9:3],struct[2:9:3],struct[0:9:4], struct[2:7:2]]
    if any(all(one == player for one in condition) for condition in winning_conditions):
       return True
def playo():
        if (a:=input('player O: Enter your option: ')) in [str(d) for d in range(1,10)]:
         print_board(int(a)-1,symbol:='o',playo)
         if not (validate_move(symbol)):
          playx()
         else:
             print(f'{symbol} player won')
             exit()
        else:
            print('Wrong option enter option between 1 to 9')
            playo()
def playx():
    if (b:=input('player X: Enter your option: ')) in [str(d) for d in range(1,10)]:
     print_board(int(b)-1,symbol:='x',playx)
     if not (validate_move(symbol)):
        playo()
     else:
         print(f'{symbol} player won')
         exit()
    else:
        print('Wrong option enter option between 1 to 9')
        playx()
print('''|1| |2| |3|
|4| |5| |6|
|7| |8| |9|
player x start the game as first player''')
playx()
