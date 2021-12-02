min, max = map(int, input().split())
temp = int(input())


while temp != -999:
    if min <= temp <= max:
        print("NtRport")
        temp = int(input())
    else:
        print("A")
    break        
