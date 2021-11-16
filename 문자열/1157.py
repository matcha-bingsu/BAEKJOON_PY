# 단어 공부: 주어진 단어에서 가장 많이 사용된 알파벳을 출력하는 문제

inp = input()

abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
save = []
i = 0

for letter in abc:
    save.append(inp.count(letter))
for letter in ABC:
    save[i] += inp.count(letter)
    i += 1
if save.count(max(save)) != 1:
    print('?')
else:
    print(ABC[save.index(max(save))])


"""
words = input().upper() <-소문자와 대문자를 구분하지 않기 때문에
unique_words = list(set(words)) <-입력받은 문자열에서 중복값 제거

cnt_list = []
for x in unique_words:
    cnt = words.count(x)
    cnt_list.append(cnt)

"""