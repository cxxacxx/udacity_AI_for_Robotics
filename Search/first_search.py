#!/usr/bin/env python
# coding: utf-8

# In[19]:


# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    take = [0,init[0],init[1]]
    print("take:", take)
    open = []
    path = "fail"
    
    g = 0
    while True:
        if take[1]== goal[0] and take[2] == goal[1]:
            print("success!")
            path = take
            break
        for d in delta:
            g = take[0] + cost
            x = take[1] + d[0]
            y = take[2] + d[1]
            cell = [g,x,y]
            if x>=0 and x< len(grid) and y>=0 and y<len(grid[0]) and grid[x][y]==0:
                open.append(cell)
        grid[take[1]][take[2]]=2;
        if len(open) == 0:
            break
        open.sort()
        print("open:", open)
        take = open[0]
        print("take:", take)
        open.pop(0)
        
    return path
        
    
    
    
    
    
    
    
    
    
print(search(grid,init,goal,cost))


# In[ ]:


##### Do Not Modify ######

import grader

try:
    response = grader.run_grader(search)
    print(response)    
    
except Exception as err:
    print(str(err))


# In[ ]:




