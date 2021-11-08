
def get_max_number(number_list):
    number = number_list[0] # index 참조
    for currunt_number in number_list:
        if currunt_number > number:
            number = currunt_number
    
    return number


def get_max_index(number_list):
    number = number_list[0] # index 참조
    
    max_index = 0
    for index, currunt_number in enumerate(number_list):
        if currunt_number > number:
            number = currunt_number
            max_index = index

    return max_index


numbers = [17, 92, 18, 33, 48, 7, 33, 42]

print(get_max_number(numbers)) #92임을 기대하고 있다.
print(get_max_index(numbers)) #1임을 기대
