import random
import time

animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
]

input("준비되셨으면, 엔터키를 입력해주세요.")

begin_time = time.time()
ok_counter = 0

for i in animal_names:
    length = len(i) 
    

for count in range(5):
    
    random_name = random.choice(animal_names)
    print(random_name)
    line = input(">>>")
    if (random_name == line):
        ok_counter += 1
        print("정확합니다.")
    else:
        print("오타가 있어요.")

end_time = time.time()

x = end_time - begin_time
tasu = (length/x) * 60

print(f"{ok_counter}번 성공하셨습니다.")
print(f"총 {end_time - begin_time}초가 걸리셨어요.")
print(f"{x * 60}분당 {tasu} 타가 나왔습니다.")