st_digit(number):
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
