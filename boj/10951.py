# solution1 : sys.readlines()
import sys

input = sys.stdin.readlines()

for line in input:
    A, B = map(int, line.split())
    print(A+B)


# solution2 : 예외 처리로 EOF를 판단하기
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break