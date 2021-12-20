
# list
# 항상 좌항과 우항의 개수가 같아야한다.
name, age, region = ["Tom", 10, "Seoul"]

name, *extra = ["Tom", 10, "Seoul"]
name, *__ = ["Tom", 10, "Seoul"]

name, age, region = ["Tom", 10, "Seoul"]
__, age, __ = ["Tom", 10, "Seoul"]