 
#hint: random.randint를 통해 1이상 100이하의 랜덤수를 만듭니다.

#유저에게 10회의 기회를 줍니다. for, range사용 
#그 숫자를 맞췄다면 몇 번 만에 맞췄는지 숫자를 출력하고 
#입력한 숫자가 랜덤수보다 작다면 "더 큰수를 입력해주세요" 라고 출력
#입력한 숫자가 랜덤수보다 크다면, "더 작은수를 입력해주세요"라고 출력
#횟수를 초과했다면, "다음 기회에..."라고 출력

import random
ran_number = random.randint(1, 100)
count = 1
for i in range(10):
    press_num = input("1~100 사이 숫자를 입력하세요 ")
    press_num = int(press_num)
    if ran_number == press_num:
        print(f"{count}번만에 맞췄습니다")
        break
    #####
    elif 100 >= press_num > ran_number:
        count += 1
        if count == 11:
            break
        else:
            print("더 작은 수를 입력해주세요")

    #####
    elif 1 <= press_num < ran_number:
        count += 1
        if count == 11:
            break
        else:
            print("더 큰 수를 입력해주세요")

    #####
    elif press_num < 1 or press_num > 100:
        count += 1
        if count == 11:
            break
        else:
            print("범위에 맞지 않는 수를 입력하였습니다")
if count == 11:
    print("다음 기회에..")