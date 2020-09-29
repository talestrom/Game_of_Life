import numpy as np
import matplotlib

board = np.zeros((10,10))

#random initialization of the cells which are alive on the board           
for i in range(10):
  for j in range(10):
    board[i,j] = np.random.binomial(1,0.35)

#print(board)
matplotlib.pyplot.matshow(board)

# Computing the number of neighbors using convolution with a kernel:
kernel = np.array([[1, 1, 1],[1, 0, 1],[1, 1, 1]])

from scipy.ndimage import convolve

neighbors = convolve(board, kernel, mode='constant')
print(neighbors)

#Next cell contains the heart of Game of Life: computing then next step. As inputs it takes the board as well as the map of neighbors. 

def next_step(board, neighbors):
  board_next = np.zeros((10,10))
  for i in range(10):
   for j in range(10):
      if board[i,j]==1 and (neighbors[i,j]>3 or neighbors[i,j]<2):
        board_next[i,j] = 0
      if board[i,j]==1 and (neighbors[i,j] == 2 or neighbors[i,j]==3):
        board_next[i,j] = 1 
      if board[i,j]==0 and (neighbors[i,j]==3):
        board_next[i,j] = 1
      if board[i,j]==0 and (neighbors[i,j]!=3):
        board_next[i,j] = 0
  return board_next

#Next cell contains a function which prints out subsequent states of the 'Game of Life'. It has parameter sessions - number of steps we want and parameter - probability of a cell being alive in the state of inicialization. 

def print_lot(sessions, parameter,size):
  board = np.zeros((size,size))
  for i in range(size):
    for j in range(size):
      board[i,j] = np.random.binomial(1,parameter)
  for i in range(sessions):
    matplotlib.pyplot.matshow(board)
    neighbors = convolve(board, kernel, mode='constant')   
    board = next_step(board, neighbors)


print_lot(20,0.2,50)
