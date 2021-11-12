#더하기 사이클 

num = int(input())
old = num
count = 0

while True:
    a = num // 10 
    b = num % 10
    c = (a + b) % 10 
    num = (b * 10) + c

    count += 1
    if num == old:
        break 
print(count) 

# 숫자로도 인덱스처럼 더하는 방법이 있다 by usung //, %
