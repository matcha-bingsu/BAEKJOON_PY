# X보다 직은 수 

N, X = map(int,input().split())

A = list(map(int,input().split())) #빈 리스트에 인덱스로 접근 금지

for i in range(N):
    if A[i] < X: 
        print(A[i], end = ' ')