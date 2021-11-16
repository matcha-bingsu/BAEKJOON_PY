# 상수: 숫자를 뒤집어서 비교하는 문제

inp = input().split()
num = ''

for each in inp:
    num += ' '
    for i in range(len(each) - 1, -1, -1):
        num += each[i]
print(max(num.split()))

"""
num1, num2 = input().split()
num1 = int(num1[::-1]) 
"""
