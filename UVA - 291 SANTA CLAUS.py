"""
Created on Tue Oct 30 11:03:34 2018

@author: Gabriel
"""
import numpy as np
map = [[0,1,1,0,1],
    [1,0,1,0,1],
    [1,1,0,1,1],
    [0,0,1,0,1],
    [1,1,1,1,0]] 

ans = np.zeros(9)
len(ans)

def dfs(idx, now):
    ans[idx] = now
    if(idx == 8):
        for i in range(9):
            print(int(ans[i]+1), end='')
        print("",flush=True)
        return 0
    
    
    
    for j in range(5):
        if(map[now][j] == 1):
            map[now][j] = map[j][now] = 0
            dfs(idx+1, j)
            map[now][j] = map[j][now] = 1
        
    

dfs(0,0)
