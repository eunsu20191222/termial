from time import sleep
import random

user = input("이름을 입력해 주세요: ") #유저네임 저장

print(f"{user}님 안녕하세요!")
print("게임 시작")

while True:
    result = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    final_result = random.choice(result)
    sleep(1)
    print(final_result)
    