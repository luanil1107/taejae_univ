# 1. 숫자를 입력한다. 2. 숫자*총숫자를 한다(곱셈이니 처음은 1) 3. 숫자-1을 한 뒤 2로 이동 4. 숫자가 1보다 작거나 같으면 정지. 5. 총 값을 출력
num = int(input("팩토리얼 계산기입니다. 원하는 숫자를 입력하십시오: "))

total = 1

for i in range(num):
    total = total * num
    num -= 1

    if num <= 1:
        break

print(total)