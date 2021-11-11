# 별 찍기 - 2

num = int(input())

for i in range(num):
    for j in range(num):
        if j < num - i - 1:
            print(' ',end='')
        else:
            print('*',end='')
    print()
