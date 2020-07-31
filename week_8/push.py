#Ontefetse Ditsele
#
#24 June 2020


import util

def push_up(grid):
  """merge grid values upwards"""
  grid[:] = list(map(list,zip(*grid)))
  for index in range(4):
        nrow = []
        
        row = grid[index]
        row = [val for val in row if val != 0]
         
        for element in range(len(row)):
          value = row[element]
                
          if len(nrow) != 0:
            if nrow[-1] == value:
                nrow[-1] = value*2
                value = 0
          nrow.append(value)
        

        nrow = [val2 for val2 in nrow if val2 != 0]
        nrow.extend([0] * 4)
        grid[index][:] = nrow[:4]
  
  grid[:] = list(map(list,zip(*grid)))

 
def push_down(grid):
  """merge grid values upwards"""
  grid[:] = list(map(list,zip(*grid)))
  
  for index in range(4):
        nrow = []
        
        row = grid[index][::-1]
        row = [val for val in row if val != 0]
         
        for element in range(len(row)):
          value = row[element]
                
          if len(nrow) != 0:
            if nrow[-1] == value:
                nrow[-1] = value*2
                value = 0
          nrow.append(value)
        

        nrow = [val2 for val2 in nrow if val2 != 0]
        nrow.extend([0] * 4)
        grid[index][:] = nrow[:4][::-1]
  
  grid[:] = list(map(list,zip(*grid)))
   
def push_left(grid):
  """merge grid values towards the left"""
  
  for index in range(4):
        nrow = []
        
        row = grid[index]
        row = [val for val in row if val != 0]
         
        for element in range(len(row)):
          value = row[element]
                
          if len(nrow) != 0:
            if nrow[-1] == value:
                nrow[-1] = value*2
                value = 0
          nrow.append(value)
        

        nrow = [val2 for val2 in nrow if val2 != 0]
        nrow.extend([0] * 4)
        grid[index][:] = nrow[:4]
  

def push_right(grid):
  """merge grid values towards the right"""
  for index in range(4):
      nrow = []
        
      row = grid[index][::-1]
      row = [val for val in row if val != 0]
         
      for element in range(len(row)):
        value = row[element]
                
      
        if len(nrow) != 0:
          if nrow[-1] == value:
            nrow[-1] = value*2
            value = 0
        nrow.append(value)
        
      nrow = [val2 for val2 in nrow if val2 != 0]
      nrow.extend([0] * 4)
      grid[index][:] = nrow[:4][::-1]
