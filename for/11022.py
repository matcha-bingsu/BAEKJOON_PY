#A + B - 8

case = int(input())
for i in range(case):
    a,b=map(int,input().split())
    print("Case #%s: %s + %s = %s" %(i + 1, a, b, a + b))