#숫자퀴즈
#랜덤 숫자를 맞춰보세요.

#hint: random.randint를 통해 1이상 100이하의 랜덤수를 만듭니다.

#유저에게 10회의 기회를 줍니다. for, range사용 
#그 숫자를 맞췄다면 몇 번 만에 맞췄는지 숫자를 출력하고 
#입력한 숫자가 랜덤수보다 작다면 "더 큰수를 입력해주세요" 라고 출력
#입력한 숫자가 랜덤수보다 크다면, "더 작은수를 입력해주세요"라고 출력
#횟수를 초과했다면, "다음 기회에..."라고 출력

import random
ran_number = random.randint(1, 100)

for i in range(1, 10):
    press_num = input("숫자를 입력해주세요.")
    press_num = int(press_num)
    if press_num == ran_number:
        print(f"정답입니다.")
        break    
    elif press_num += ran_number:
        print(f"오답입니다.")
    
    elif 100 >= press_num > ran_number:
        count += 1
        if count == 11:
            break
        else:
            print("랜덤수보다 작은 수를 입력해주세요")
    elif 1 <= press_num < ran_number:
        count += 1
        if count == 11:
            break
        else:
            print("랜덤수보다 큰 수를 입력해주세요")

