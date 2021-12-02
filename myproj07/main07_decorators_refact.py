import time

#인자에 대한 리턴값을 저장
# - key: 인자 값에 대한 튜플
# - value: 그 인자로 함수를 수행했을 때의 리턴값

# cached = {} #전역변수 -> 가급적 지양해야합니다.

# def mysum2(x, y):
#     key = (x, y)
#     if key not in cached:

#         time.sleep(1) #1초간 대기
#         cached[key] = x + y + 10
#     return cached[key]


def memoize(fn):
    cached = {} #호출이 될 떄마다 새로운 캐시드가 생성된다.
    def wrap(x, y): #메모라이즈가 호출될 떄마다 새로운 
        key = (x, y)
        if key not in cached:
            cached[key] = fn(x, y)
        return cached[key]
    return wrap


@memoize
def mysum2(x, y):
    time.sleep(1)
    return x + y + 10


# mysum2 = memoize(mysum2) #@memoize (장식자) 앞 뒤 뭘 써도 똑같다

@memoize
def mymultiply2(x, y):
    time.sleep(1)
    return x + y + 10

#mymultiply2 = memoize(mymultiply2)

print(mysum2(1, 2))
print(mysum2(1, 3))   #인자의 종류가 2개라서 1초후 먼저 계산된 결과를 써서 빠르게 결과나옴
print(mysum2(1, 3))
print(mysum2(1, 2))
print(mysum2(1, 2))


print(mymultiply2(1,2))
print(mymultiply2(1,2))
print(mymultiply2(1,3))
print(mymultiply2(1,3))


#전역변수 없이도 각각 함수
#장식자의 중요성