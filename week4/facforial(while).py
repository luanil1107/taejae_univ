# 1. 숫자를 입력한다. 2. 1부터 곱하기 시작한다. 3. 입력받은 숫자가 되면 멈춘다.
num = int(input("팩토리얼 계산기입니다. 원하는 숫자를 입력하십시오: "))

i = 1
total = 1

while i <= num:
    total = total * i
    i = i + 1

print(total)

