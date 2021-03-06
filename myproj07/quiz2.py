# def myfilter(filter_fn, alter_value):
#     def wrap(fn):
#         def inner(*args):
#             new_args = []
#             for arg in args:
#                 if filter_fn(arg):
#                     new_args.append(alter_value)
#                 else:
#                     new_args.append(arg)
#             return fn(*new_args)
#         return inner
#     return wrap


def myfilter(filter_fn, alter_value):
    def wrap(fn):
        def inner(*args):
            new_args = []
            for arg in args:
                new_args.append(
                    alter_value if filter_fn(arg) else arg)
            return fn(*new_args)
        return inner
    return wrap



@myfilter(lambda i: i % 2 == 0, 0)
def mysum(a, b, c, d, e):
    return a + b + c + d + e
print(mysum(1, 2, 3, 4, 5))  # 9



@myfilter(lambda i: i % 2 == 0, 1)
def mymultiply(a, b, c, d, e):
    return a * b * c * d * e
print(mymultiply(1, 2, 3, 4, 5))  # 15