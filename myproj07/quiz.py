# fmt: off



def mysum2(x, y):
    return x + y + 10

def mysum3(x, y, z):
    return x + y + z + 10


# mysum4, 5, 쭉 늘려가고싶으면 가변인자를 써라.
# *args는 튜플이다. 다수의 값을 저장할 수 있다.
# mysum(x, y, )인자는 최소 2개로 지정한 거고, 나머지는 args로 무한으로 인자 받음


def mysum(x, y, *args):
    print("args :", args)
    return x + y + sum(args) + 10

print(mysum())
print(mysum(1))
print(mysum(1, 2))
print(mysum(1, 2, 3))
