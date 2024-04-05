print("당신이 제시한 숫자 3개 중 가장 큰 숫자를 찾을겁니다.")

first = int(input("첫번째 숫자를 입력하시오: "))
second = int(input("두번째 숫자를 입력하시오: "))
third = int(input("세번째 숫자를 입력하시오: "))

if first >= second and first >= third:
    print(f"가장 큰 숫자는 {first}입니다")

elif second >= first and second >= third:
    print(f"가장 큰 숫자는 {second}입니다")

elif third >= first and third >= second:
    print(f"가장 큰 숫자는 {third}입니다")
