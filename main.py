from time import sleep
import random
import os

def clear():
    return os.system("clear")

user = input("이름을 입력해 주세요: ") #유저네임 저장

print(f"{user}님 안녕하세요!") #유저네임 프린트 (근데 구지 할 필요가 있나??)
print("게임 시작")
point = 0 #while 문 안쪽에다 하면 계속 리셋 되서 점수가 안올라감
while True:
    result = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    final_result = random.choice(result)
    sleep(1)
    print("point: ", point)
    print(final_result)
    ask = input(": ")
    if ask == final_result: #input 과 result의 랜덤이 같으면 정답 아니면 틀림
        point += 1
        print("correct")
        sleep(0.5)
        clear()
    elif ask == "log out": #로그 아웃을 치면 게임 종료
        break
    elif ask == "python the best":
        point += 1
        print("correct")
        sleep(0.5)
        clear()
    elif ask == "돼지":
        print("되지는 꿀꿀 데이지도.. 껙")
        sleep(3)
        clear
    else:
        point -= 1
        print("wrong")
        sleep(1)
        clear()

print("게임을 종료 합니다")