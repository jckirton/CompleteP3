def div_frac(n1: int, d1: int, n2: int, d2: int):

    new_n = n1 * d2
    new_d = d1 * n2

    print(f"\nThe answer is:\n\n {new_n}\n---\n {new_d}\n\nOr\n\n{new_n / new_d}\n\n")


def mul_frac(n1: int, d1: int, n2: int, d2: int):

    new_n = n1 * d2
    new_d = d1 * n2

    print(f"\nThe answer is:\n\n {new_n}\n---\n {new_d}\n\nOr\n\n{new_n / new_d}\n\n")


def add_frac(n1: int, d1: int, n2: int, d2: int):
    pass


def sub_frac(n1: int, d1: int, n2: int, d2: int):
    pass


def get_frac():
    print("\n" * 100)
    function = input(
        "+ = Addition\n\n- = Subtraction\n\n* = Multiplaction\n\n/ = Divition\n\nWich one do you want to do?\n\n"
    )
    frac1 = input("What is your first fraction? ")
    frac2 = input("What is your second fraction? ")

    split_frac1 = frac1.split("/")
    split_frac2 = frac2.split("/")

    # print(split_frac1)
    # print(split_frac2)

    # n1 = int(split_frac1[0])
    # d1 = int(split_frac1[1])
    # n2 = int(split_frac2[0])
    # d2 = int(split_frac2[1])

    split_fracs = split_frac1 + split_frac2
    n1, d1, n2, d2 = [int(x) for x in split_fracs]

    if function == "/":
        div_frac(n1, d1, n2, d2)
    elif function == "*":
        mul_frac(n1, d1, n2, d2)
    elif function == "-":
        sub_frac(n1, d1, n2, d2)
    elif function == "+":
        add_frac(n1, d1, n2, d2)
    else:
        pass


get_frac()
