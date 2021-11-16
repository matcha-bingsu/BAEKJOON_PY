# 다이얼: 규칙에 따라 문자에 대응하는 수를 출력하는 문제

inp = input()
i = 0
t = 0

while (i < len(inp)):
    if ord(inp[i]) >= 65 and ord(inp[i]) <= 67:
        t += 3
    elif ord(inp[i]) >= 68 and ord(inp[i]) <= 70:
        t += 4
    elif ord(inp[i]) >= 71 and ord(inp[i]) <= 73:
        t += 5
    elif ord(inp[i]) >= 74 and ord(inp[i]) <= 76:
        t += 6
    elif ord(inp[i]) >= 77 and ord(inp[i]) <= 79:        
        t += 7
    elif ord(inp[i]) >= 80 and ord(inp[i]) <= 83:
        t += 8
    elif ord(inp[i]) >= 84 and ord(inp[i]) <= 86:
        t += 9
    elif ord(inp[i]) >= 87 and ord(inp[i]) <= 90:
        t += 10
    i += 1
print(t)    

"""
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)): <-단어 순서대로
    for i in dial: <-알파벳에 있는지 돌아
        if a[j] in i:
            ret += dial.index(i) + 3 <-인덱스 + 3
"""