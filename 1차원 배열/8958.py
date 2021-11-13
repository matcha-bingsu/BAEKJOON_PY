# OX퀴즈: OX퀴즈의 결과를 일차원 배열로 입력받아 점수를 계산하는 문제
lis = []

num = int(input())

for i in range(num):
    lis.append(input())

for i in range(num):
    cnt = 0
    ans = []
    for j in range(len(lis[i])):
        if lis[i][j] == 'O':
            cnt += 1
            ans.append(cnt)
        else:
            cnt = 0
    print(sum(ans))

"""
N = int(input())

for i in rage(N):
    a = input()
    score = 0
    sumScore = 0
    for j in a:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)
"""

            

