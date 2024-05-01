import random

def roll_dice():
    return random.randint(1, 6)

def play_dice_game():# 주사위 게임 통으로 묶어버리기

    num = int(input("플레이어 수를 입력하라: ")) # 1. 사용자로부터 플레이어의 수를 입력 받습니다.
    players = []

    for i in range(num):
        name = input(f"{i+1}번째 플레이어의 이름을 입력하라") # 2. 각 플레이어의 이름을 입력 받습니다.
        players.append({"name":name, "score":0}) #딕셔너리로 만듬

    for person in players: # 3. 각 플레이어는 주사위를 굴려 나온 숫자를 기록합니다.
        input(f"플레이어 {person["name"]}, 주사위를 굴리고자 한다면 enter를 입력하라")
        person["score"] = roll_dice()
        print(f"플레이어{person["name"]}의 점수는 {person["score"]}점이다")

    print("모든 플레이어가 주사위를 굴렸다. 결과를 발표하겠다")# 4. 모든 플레이어가 주사위를 한 번씩 굴린 후, 각 플레이어의 점수를 출력합니다.
    for i in players:
        print(f"{i["name"]}: {i["score"]}점")

    # 5. 가장 높은 점수를 획득한 플레이어와 점수를 출력합니다.
    max_score = 0
    winner = None

    for i in players:
        if i['score'] > max_score:
            max_score = i['score']
            winner = i
    print(f"\n우승자는 플레이어 {winner['name']}, 점수는 {winner['score']}점이다.")


while True:
    play_dice_game()#주사위 게임 실행

    again = input("게임을 다시 한 번 하시겠는가?(y/n): ") # 6. 게임의 종료여부를 묻습니다. y를 입력할 시 재시작, n을 입력할 시 프로그램을 종료합니다.
    if again.lower() != "y":
        break




