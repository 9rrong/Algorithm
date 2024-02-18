res = set()

def solution(numbers):
    for i in range(len(numbers)):
        s = []
        visited = [False] * len(numbers)
        dfs(i, s, list(numbers), visited)
    return check_prime(res)

def check_prime(nums):
    cnt = 0
    
    for num in nums:
        number = int(num)
        is_divided = False
        
        for i in range(2, int(number**(1/2)+1)):
            if number % i == 0:
                is_divided = True
                
        if not is_divided:
            cnt += 1
            
    return cnt

def dfs(start, s, n, visited):
    s.append(n[start])
    visited[start] = True
    
    if s and s[0] != '0':
        num = ''.join(map(str, s))
        if num != '1':
            res.add(num)

    for i in range(len(n)):
        if not visited[i]:
            dfs(i, s, n, visited)
            s.pop()
            visited[i] = False

