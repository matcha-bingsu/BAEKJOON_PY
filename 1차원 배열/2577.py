#숫자의 개수

A = int(input())
B = int(input())
C = int(input())
all = A * B * C
for i in range(10):
    print(str(all).count(str(i)))