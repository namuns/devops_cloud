

# 사전
tom = {
    "name": "Tom",
    "age": 10,
    # = "ag" + "e": 10,
    # age: 10,
}

name = "Tom"
age = 10

tom1 = {
    "name": name,
    "age": age,

}

# f-string = String Interpolation이라고 한다.
print(f"안녕나는 {name}이야/ {age}살이지.")

# 두 줄 쓰는 """
print(f"""안녕나는 {name}이야
 {age}살이지.""")