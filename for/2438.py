# 별 찍기 - 1

num = int(input())

for i in range(num):
    for j in range(num):
        if j <= i:
            print('*',end='')
    print()


"""

inp = int(input())
for i in range(1, inp+1):
    print('*' * i)

"""