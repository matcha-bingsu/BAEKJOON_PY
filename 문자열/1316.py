# 그룹 단어 체커: 조건에 맞는 문자열을 찾는 문제

cnt = 0
case = int(input())

for i in range(case):
    word = input()
    exist = ''
    for j in range(len(word)):
        if word[j] in exist:
            if word[j - 1] != word[j]:
                break
        exist += word[j]
        if j == len(word) - 1:
            cnt += 1 
print(cnt)

"""
for i in range(N):
    word = input()
    for j in range(len(word)):
        if j != len(word) - 1:
            if word[j] == word[j + 1]:
                pass
            elif word[j] in word[j + 1:]: ←이후 나머지에서 확인가능한지
                break
        else:
            cnt +=1
"""