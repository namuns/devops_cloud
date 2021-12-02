import time

#인자에 대한 리턴값을 저장
# - key: 인자 값에 대한 튜플
# - value: 그 인자로 함수를 수행했을 때의 리턴값

cached = {} #전역변수 -> 가급적 지양해야합니다.

def mysum2(x, y):
    key = (x, y)
    if key not in cached:

        time.sleep(1) #1초간 대기
        cached[key] = x + y + 10
    return cached[key]

cached2 = {}
def mymultiply2(x, y):
    key = (x, y)
    if key not in cached2: 
        time.sleep(1)
        cached2[key] = x * y + 10
    return cached2[key]
    
#같은 캐시이름이 있고 같은 값이 중복되어있으면 print값도 중복되어 오류?

print(mysum2(1, 2))
print(mysum2(1, 3))   #인자의 종류가 2개라서 1초후 먼저 계산된 결과를 써서 빠르게 결과나옴
print(mysum2(1, 3))
print(mysum2(1, 2))
print(mysum2(1, 2))


print(mymultiply2(1,2))
print(mymultiply2(1,2))
print(mymultiply2(1,3))
print(mymultiply2(1,3))



# def base(base_number):
#     #number = 10 #함수 안에 있는 지역변수(base_10을 호출할 때 마다 fn이 새로 생성?)
#     #fn = lambda x, y: x + y + 10
#     def fn(x, y): return x + y + base_number
#     return fn

# base_10 = base(10)
# base_20 = base(20)

# print(base_10(1, 2))
# print(base_20(1, 2))


# name = "Tom"
# def mysum(x, y): return x + y


# other_name = name
# other_fn = mysum


# def fn(x):
#     y = "hello"
#     return y


# fn(name)
