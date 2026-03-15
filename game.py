import random

def guess_number_game():
    print("🎮 숫자 맞추기 게임에 오신 것을 환영합니다!")
    print("1부터 100 사이의 숫자를 생각했습니다. 맞춰보세요!")

    # 컴퓨터가 무작위 숫자 생성
    target_number = random.randint(1, 100)
    attempts = 0  # 시도 횟수

    while True:
        try:
            # 사용자로부터 입력 받기
            user_guess = int(input("숫자를 입력하세요: "))
            attempts += 1

            if user_guess < target_number:
                print("UP! 더 큰 숫자입니다. 📈")
            elif user_guess > target_number:
                print("DOWN! 더 작은 숫자입니다. 📉")
            else:
                print(f"🎉 정답입니다! {attempts}번 만에 맞추셨네요!")
                break
        except ValueError:
            print("❌ 숫자를 입력해야 합니다. 다시 시도하세요.")

if __name__ == "__main__":
    guess_number_game()