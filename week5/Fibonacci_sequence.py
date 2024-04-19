# 피보니치 수열 연산
# 바로 앞 두 수를 더한 수가 다음 수에 오는 수열
# ex) 0 1 1 2 3 5 8 13 21 34....
# n번째 파보니치 수를 구하는 코드를 작성해야 함
# 수열을 0부터 시작하게 할것
# n = (n-1)+(n-2)
# n-1 = (n-2)+(n-3)

def fibonacci(n):

    if n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        return output

while True:

    try:
        n = int(input("구하고자 하는 n번째 파보니치 수를 입력하라: "))

        print(f"{n}번째 파보니치 수: " + str(fibonacci(n)))

    except:
        print("숫자만 입력하시오.")



