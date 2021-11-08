"""1이상 100미만 범위에서 3과 5의 공배수를 합을 출력하기
"""

result = 0
for n in range(1, 100):
    if 3 % n == 0 and 5 % n == 0:
        result += n
    print(result)


number_list = []
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        number_list.append(i)

print(sum(number_list))
