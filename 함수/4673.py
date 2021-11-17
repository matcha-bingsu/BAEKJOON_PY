# 셀프 넘버: 함수 d를 정의하여 문제를 해결해 봅시다.

def d():
    ans = list(range(1,10001))
    d = []
    for i in range(1, 10001):   #리스트 표현식으로 할 수 있음 좋을 텐데
        for num in str(i):
            i += int(num)
        d.append(i)
    d= list(set(d))
    for num in d:
        if num < 10001:
            ans.remove(num)
    for num in ans:
        print(num)

d()