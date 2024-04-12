num = int(input("소수를 판별하겠습니다. 원하는 숫자를 입력하십시오: "))
if num == 1:
    print("1은 소수가 아닙니다")
elif num == 2:
    print(f"2는 소수입니다")
elif num == 3:
    print(f"3은 소수입니다")

root = int(num ** 0.5)

for i in range(2, root+1):

    if num % i == 0:
        print(f"{num}은 소수가 아닙니다.")
        break

    else:
        print(f"{num}은 소수입니다")
        break














