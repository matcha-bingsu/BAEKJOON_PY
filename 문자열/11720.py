# 숫자의 합: 문자열로 입력받는 문제. 파이썬처럼 정수 크기에 제한이 없다면 상관없으나 예제 3번은 일반적인 정수 자료형에 담기에 너무 크다는 점에 주목합니다.

case = int(input())
inp = input()

result = [int(i) for i in inp]
print(sum(result))

#print(sum(map(int, input())))
