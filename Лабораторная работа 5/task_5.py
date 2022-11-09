from random import sample


def get_random_password(length=8) -> str:
    var_up = [chr(i) for i in range(65, 91)]
    var_down = [chr(i) for i in range(97, 123)]
    var_num = [str(i) for i in range(10)]
    var_ = var_up + var_down + var_num
    password = ''.join(sample(var_, length))
    return password


print(get_random_password())
