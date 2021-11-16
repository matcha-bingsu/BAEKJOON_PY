# 알파벳 찾기: 한 단어에서 각 알파벳이 처음 등장하는 위치 찾는 문제

word = input()

for alpha in range(ord('a'),ord('z') + 1):
    print(word.find(chr(alpha)), end = ' ')

# abc = 'abcdefghijklmnopqrstuvwxyz'