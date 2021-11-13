# 나머지: 위와 비슷한 문제

dele = []
lis = []
for i in range(10):
    num = int(input())%42
    if num not in lis:
        lis.append(num)
print(len(lis))
