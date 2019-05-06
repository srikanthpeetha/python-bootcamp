grid = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
global status_flag
status_flag = True

def print_board(symbol,position):
  if(position == None):
    print("+---+---+---+\n| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |\n+---+---+---+\n")
    return
  if(1 <= position <=9):
    if(grid[position-1]==' '):
      grid[position-1] = symbol
      print("+---+---+---+\n| {} | {} | {} |\n+---+---+---+\n| {} | {} | {} |\n+---+---+---+\n| {} | {} | {} |\n+---+---+---+\n".format(grid[0],grid[1],grid[2],grid[3],grid[4],grid[5],grid[6],grid[7],grid[8]))
      return True
    else:
      print("Box already used. Enter unused box number")
      return False
  else:
    print("Please Enter correct box number. Number should be betweeen 1 nad 9")
    status_flag = False
    return False

def stop_game():
  if(grid[0] == grid[1] == grid[2] == 'X'):
    return True
  elif(grid[3] == grid[4] == grid[5] == 'X'):
    return True
  elif(grid[6] == grid[7] == grid[8] == 'X'):
    return True
  elif(grid[0] == grid[3] == grid[6] == 'X'):
    return True
  elif(grid[1] == grid[4] == grid[7] == 'X'):
    return True
  elif(grid[2] == grid[5] == grid[8] == 'X'):
    return True
  elif(grid[0] == grid[4] == grid[8] == 'X'):
    return True
  elif(grid[2] == grid[4] == grid[6] == 'X'):
    return True
  if(grid[0] == grid[1] == grid[2] == 'O'):
    return True
  elif(grid[3] == grid[4] == grid[5] == 'O'):
    return True
  elif(grid[6] == grid[7] == grid[8] == 'O'):
    return True
  elif(grid[0] == grid[3] == grid[6] == 'O'):
    return True
  elif(grid[1] == grid[4] == grid[7] == 'O'):
    return True
  elif(grid[2] == grid[5] == grid[8] == 'O'):
    return True
  elif(grid[0] == grid[4] == grid[8] == 'O'):
    return True
  elif(grid[2] == grid[4] == grid[6] == 'O'):
    return True
  else:
    return False

def start_game():
  print_board(None,None)
  print("Enter box number to mark player symbol in TicTacToe grid.\nPlayer One symbol ==> 'X'\nPlayer Two symbol ==> 'O'")
  turn = 1
  while(status_flag):
    if(turn%2 != 0):
      position = int(input("Player One turn: "))
      if(print_board('X',position)):
        if(stop_game()):
          print("Player one wins")
          break
        turn += 1
    else:
      position = int(input("Player Two turn: "))
      if(print_board('O',position)):
        if(stop_game()):
          print("Player wins wins")
          break
        turn += 1


def test_board():
  print_board('x',6)
  print(grid)
  print_board('o',5)
  print(grid)
  print_board('x',6)
  print(grid)
  print_board('x',11)
  print(grid)

start_game()