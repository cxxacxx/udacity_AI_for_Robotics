#!/usr/bin/env python
# coding: utf-8

# In[18]:


# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    g = 0
    take = [g,init[0],init[1]]
    open = []
    while True:
        expand[take[1]][take[2]]=take[0]
        print("take:",take)
        if take[1]==goal[0] and take[2]==goal[1]:
            print("success!")
            break
            
        for d in delta:
            x = take[1]+d[0]
            y = take[2]+d[1]
            if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y]==0 and expand[x][y]==-1:
                g+=1
                expand[x][y] = g
                open.append([g,x,y])
                print([g,x,y])
        if len(open)==0:
            break
        open.sort()
        take = open[0]
        open.pop(0)
    return expand

print(search(grid,init,goal,cost))


# In[6]:


##### Do Not Modify ######

import grader
from test import delta, delta_name

try:
    respons
    e = grader.run_grader(search)
    print(response)    
    
except Exception as err:
    print(str(err))


# In[ ]:




