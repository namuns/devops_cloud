
"""1이상 100미만 범위에서 3과 5의 공배수를 모두 출력하기"""

for n in range(1, 100):
    if n % 3 == 0 and n % 5 == 0:
        print(n)


for i in range(1, 100):
    if i % 15 == 0:
        print(i)


for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
