from random import randint


def get_unique_list_numbers() -> list[int]:
    min_ = -10
    max_ = 10
    length = 15
    list_ = []
    while len(list_) != length:
        list_ = list(list_)
        list_.append(randint(min_, max_))
        list_ = set(list_)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
