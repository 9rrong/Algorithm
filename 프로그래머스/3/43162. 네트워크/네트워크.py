from collections import deque

def solution(n, computers):
    cnt = 0
    visited = [False] * n
    
    def bfs(v):
        
        q = deque()
        q.append(v)
        visited[v] = True
        
        while q:
            s = q.popleft()
            visited[s] = True
            
            for i in range(n):
                if computers[s][i] == 1 and not visited[i]:
                    q.append(i)
        
                    
    for j in range(n):
        if not visited[j]:
            bfs(j)
            cnt+=1
    
    return cnt