

import random as r
notexisting = False
gameend = False
tie = 0
user = 0
bot = 0
xvalue = 0
yvalue = 0
board = [['ㅁ','ㅁ','ㅁ'],
 ['ㅁ','ㅁ','ㅁ'],
 ['ㅁ','ㅁ','ㅁ']]
def checkwin(board):
  if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
    if checkplayer(0,0):
      return True
  if board[1][0] == board[1][1] and board[1][1] == board[1][2]:
    if checkplayer(1,0):
      return True
  if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
    if checkplayer(2,0):
      return True
  if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
    if checkplayer(0,0):
      return True
  if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
    if checkplayer(0,1):
      return True
  if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
    if checkplayer(0,2):
      return True
  if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    if checkplayer(0,0):
      return True
  if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
    if checkplayer(0,2):
      return True
  return False
def checkplayer(x,y):
  xvalue = x
  yvalue = y
  if board[x][y] == 'X':
    print("Player won")

    return True
  if board[x][y] == 'O':
    print("Bot won")

    return True
  return False
def checktie():
  count=9
  for x in range(9):
    if board[x//3][x%3] == 'ㅁ':
      count = count-1
  if count == 9:
    return True

  return False

for x in board:
  print(x)
while gameend == False:

  notexisting = False
  while notexisting == False:
    a = int(input())
    if a>-1 and a<9:
      if board[a//3][a%3] == 'O' or board[a//3][a%3] == 'X':
        notexisting = False
      else:
        board[a//3][a%3] = 'X'
        notexisting = True
        isWin = checkwin(board)
        isTie = checktie()


        if isWin or isTie:
          print("reached")
          gameend = True
          if isTie and not isWin:
            tie+=1
            print(tie)
          if isWin:
            user+=1

        else:
          gameend = False






  #gdgggbdbgbdg
  if (not gameend):
    notexisting = False
    while notexisting == False:
      x = r.randint(0,8)
      if board[x//3][x%3] == 'X' or board[x//3][x%3] == 'O':
        notexisting = False
      else:
        board[x//3][x%3] = 'O'
        notexisting = True
        isWin = checkwin(board)
        isTie = checktie()


        if isWin or isTie:
          print("reached")
          gameend = True
          if isTie and not isWin:
            tie+=1
            print(tie)
          if isWin:
            bot+=1

        else:
          gameend = False
        for x in board:
          print(x)

  if gameend == True:
    aa = input("Start New Game? (Yes/No)")
    if aa == "Yes" or aa == "yes":
      print("Player won:",user,"Bot won:",bot,"Tied:",tie)
      board = [['ㅁ','ㅁ','ㅁ'],
       ['ㅁ','ㅁ','ㅁ'],
       ['ㅁ','ㅁ','ㅁ']]
      for x in board:
        print(x)
      gameend = False
    if aa == "No" or aa == "no":
      gameend = True
      print("Player won:",user,"Bot won:",bot,"Tied:",tie)