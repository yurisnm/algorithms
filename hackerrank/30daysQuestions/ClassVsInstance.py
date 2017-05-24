# def solution(A):
#     i = 1
#     print(A)
#     while i< len(A):
#         print("--------------")
#         print(A[0:i], sum(A[0:i]))
#         print(A[i::], sum(A[i::]))
#         if sum(A[0:i])==sum(A[i+1::]):
#             return i
#         i+=1
#     if sum(A)==0:
#         return 0
#     return -1

def solution(A):
    i = 1
    while i< len(A):
        if sum(A[0:i])==sum(A[i+1::]):
            return i
        i+=1
    if sum(A)==0:
        return 0
    return -1

print(solution([500,1,-2,-1,2] ))