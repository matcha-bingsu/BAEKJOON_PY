# 한수: X가 한수인지 판별하는 함수를 정의하여 문제를 해결해 봅시다

def is_hansu(inp):
    cnt = 0 
    for i in range(1, inp + 1):
        i = str(i)
        if len(i) > 2:
            left = set()
            for j in range(0,len(i) - 1):
                num = int(i[j]) - int(i[j + 1])
                left.add(num)
            if len(set(left)) == 1:
                cnt += 1
        else:
            cnt += 1                
    return cnt

print(is_hansu(int(input())))

"""
def hansu(num) :
    hansu_cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i))) 
        print(num_list)
        if i < 100:
            hansu_cnt += 1 
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            hansu_cnt += 1  
    return hansu_cnt

num = int(input())
print(hansu(num))
"""