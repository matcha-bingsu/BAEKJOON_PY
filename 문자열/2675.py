# 문자열 반복: 각 문제를 반복하여 출력하는 문제

case = int(input())

for i in range(case):
    times, letters = input().split()
    for letter in letters:
        print(letter * int(times), end='')
    print()
        
"""
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i   <-문자열이니까 그냥 더해주넹 ㅇㅅㅇ 
    print(text)
"""