# 크로아티아 알파벳: 크로아티아 알파벳의 개수를 세는 문제

inp = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for each in croatia:
   inp = inp.replace(each,"*")
print(len(inp))