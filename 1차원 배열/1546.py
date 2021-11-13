# 평균: 평균을 조작하는 문제

num =int(input())
scores = list(map(int, input().split()))
M = max(scores)

for i in range(len(scores)):
    scores[i] = scores[i] / M * 100
print(sum(scores) / num)
