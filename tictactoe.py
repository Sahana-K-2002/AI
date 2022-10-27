"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount=0
    ocount=0
    for i in range (len(board)):
      for j in range (len(board[0])):
        if board[i][j]==X:
          xcount=xcount+1
        elif board[i][j]==O:
          ocount=ocount+1
    return X if xcount==ocount else O 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions=set()
    for i in range (len(board)):
      for j in range (len(board[0])):
        if board[i][j]==EMPTY:
          actions.add((i,j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x,y)=action
    if x<0 or x>=len(board) or y<0 or y>=len(board):
      raise IndexError
   
    new=[row[:] for row in board]
    #new=copy.deepcopy(board)
    new[x][y]=player(board)
    return new

def row(board,player):
  for i in range(len(board)):
    count=0
    for j in range(len(board[0])):
      if board[i][j]==player:
        count=count+1
    if count==len(board[0]):
      return True
  return False
  
def col(board,player):
  for i in range(len(board)):
    count=0
    for j in range(len(board[0])):
      if board[j][i]==player:
        count=count+1
    if count==len(board[0]):
      return True
  return False

def mdiag(board,player):
  count=0
  for i in range(len(board)):
    for j in range(len(board[0])):
      if i==j and board[i][j]==player:
        count=count+1
  if count==len(board[0]):
    return True
  return False

def diag(board,player):
  count=0
  for i in range(len(board)):
    for j in range(len(board[0])):
      if i+j==2 and board[i][j]==player:
        count=count+1
  if count==len(board[0]):
    return True
  return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if row(board,X) or col(board,X) or mdiag(board,X) or diag(board,X):
      return X
    elif row(board,O) or col(board,O) or mdiag(board,O) or diag(board,O):
      return O
    else:
      return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
      return True
    #count=0
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j]==EMPTY:
          return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
      return 1
    elif winner(board)==O:
      return -1
    else:
      return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
      return None
    elif player(board)==X:
      v=float('-inf')
      selected=None
      for action in actions(board):
        minval=min_val(result(board,action))
        if minval>v:
          v=minval
          selected=action
    elif player(board)==O:
      v=float('inf')
      selected=None
      for action in actions(board):
        maxval=max_val(result(board,action))
        if maxval<v:
          v=maxval
          selected=action
    return selected
    
def max_val(board):
  if terminal(board):
    return utility(board)
  v=float('-inf')
  for action in actions(board):
    v=max(v,min_val(result(board,action)))
  return v
  
def min_val(board):
  if terminal(board):
    return utility(board)
  v=float('inf')
  for action in actions(board):
    v=min(v,max_val(result(board,action)))
  return v




