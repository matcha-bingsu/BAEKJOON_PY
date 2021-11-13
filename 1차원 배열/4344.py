# 평균은 넘겠지

case = int(input())

for i in range(case):
    case1 = list(map(int, input().split()))
    sum = 0
    cnt = 0
    for j in range(1, len(case1)):
        sum += case1[j]
    avg = sum / case1[0]
    for j in range(1, len(case1)):
        if case1[j] > avg:
            cnt += 1
    print('%.3f' %(cnt / case1[0] * 100), '%', sep = '')

"""
for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/num[0]  #인덱스 활용
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1
    rate = cnt / nums[0] * 100
    print(f.'{rate : .3f}%')

"""