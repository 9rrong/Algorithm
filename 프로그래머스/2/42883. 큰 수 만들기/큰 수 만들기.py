from collections import deque

def solution(number, k):
    answer = []
    
    for num in number:
        while answer and num > answer[-1] and k > 0:
            answer.pop()
            k-=1
        answer.append(num)
    
    return ''.join(answer[:len(answer) - k])