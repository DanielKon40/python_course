# The function checks for integers


def int_checker(num):
    for x in num:
        if x % 1 != 0 or x < 0:
            raise ValueError(x, "does not belong on the list")
        else:
            pass

user_input = input("enter your list:\n(use this format X, Y, Z..) ")
new_list = user_input.split(", ")
n_list = [float(x) for x  in new_list]


if __name__ == '__main__':
    print(int_checker(n_list))
