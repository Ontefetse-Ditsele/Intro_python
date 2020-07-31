 #Ontefetse Ditsele
#
#23 June 2020

def create_grid(grid):
  """create a 4x4 array of zeroes within grid"""
  #row= [0,0,0,0]
  for rows in range(4):
    #grid.append(row)
    grid.append([0,0,0,0])
  return grid 

def print_grid(grid):
  """print out the a in 5-width columns within a box"""
  box = "{:5}{:5}{:5}{:5}"
  for row in range(4):
    print(box.format(grid[row][0],grid[row][1],grid[row][2],grid[row][3]))
    
def check_lost(grid):
  """return True if there are no 0 values and there are no adjacent values 
     that are equal; otherwise False"""
  #returns false if a 0 in the grid or if adjacent values are equal,
  #ptherwise it returns true
  
  for index in range(4):
    if 0 in grid[index]:
      return False
    if (grid[index][0] == grid[index][1]) or (grid[index][1]==grid[index][2]) or (grid[index][2]==grid[index][3]):
      return False
    if (grid[0][index] == grid[1][index]) or (grid[1][index]==grid[2][index]) or (grid[2][index]==grid[3][index]): 
      return False
  return True

def check_won(grid):
  """ returns True is a value>= 32 is found in the grid; otherwise False"""
  for row in grid:
    for value in row:
      if value >= 32:
        return True
  return False

def copy_grid(grid):
  """ returns a copy of the given grid"""
  clone = []
  for rows in grid:
    row = []
    for col in rows:
      row.append(col)
    clone.append(row)
  return clone

def grid_equal(grid1,grid2):
  """check if 2 grids are equal - return boolean value"""
  if (grid1[0] == grid2[0]) and (grid1[1] == grid2[1]) and (grid1[2] == grid2[2]) and (grid1[3] == grid2[3]): 
    return True
    
  return False
