def get_count_char(str_):
    str_ = str_.lower().strip()
    dict = {}
    for char in str_:
        if char in dict:
            dict[char] += 1
        elif char.isalpha():
            dict[char] = 1
    return dict


def get_proc_char(dictinary):
    sum_ = 0
    for alpha in dictinary:
        sum_ += dictinary.get(alpha)
    for alpha in dictinary:
        dictinary[alpha] = round((dictinary.get(alpha) / sum_) * 100, 2)
    return dictinary


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
