#!/usr/bin/python
import numpy as np

connected = []

def canmove(row, col, nrows, ncols, visited, mat):
    return (row >= 0 and row < nrows and col >= 0 and col < ncols and mat[row][col] == 1 and visited[row][col] == False)

def dfs(r, c, visited, input):
    global connected
    
    rmove = [0, 1,  0, -1] # right, down, left, up 
    cmove = [1, 0, -1,  0]
    
    connected.append((r, c))           
    visited[r][c] = True
    
    nrows = input.shape[0]
    ncols = input.shape[1]
    
    for n in xrange(4):
        next_r = r + rmove[n]
        next_c = c + cmove[n]
        if (canmove(next_r, next_c, nrows, ncols, visited, input)):
            dfs(next_r, next_c, visited, input)
    
def segment(input):
    global connected
   
    nrows = input.shape[0]
    ncols = input.shape[1]
    
    visited = [[False for c in xrange(ncols)] for r in xrange(nrows)] 
    result = []
   
    for r in xrange(nrows):
        for c in xrange(ncols):
            if (visited[r][c] == False and input[r][c] == 1):
                dfs(r, c, visited, input)
                result.append(connected)
                connected = []
    return result

if __name__== "__main__":
    test_img = np.array([[1,0,1,0,1,1,0],
                         [1,0,0,0,0,0,0],
                         [1,1,0,0,1,0,1],
                         [1,0,1,0,1,1,1],
                         [0,0,1,1,1,1,0]])
    print ""
    print "Original image:"
    print test_img
    print ""
    print "Segmentation image:"
    print segment(test_img)
