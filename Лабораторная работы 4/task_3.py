def delete(list_, index=None):
    new_list = []
    if index is None:
        index = -1
        f_list = list_[:index]
        new_list = f_list
    else:
        f_list = list_[:index]
        s_list = list_[index + 1:]
        new_list = f_list + s_list
    return new_list


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
