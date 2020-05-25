def lcm(d1: int, d2: int):
    pass


def div_frac(n1: int, d1: int, n2: int, d2: int):

    new_n = n1 * d2
    new_d = d1 * n2

    print("\n" * 100)
    print(
        f"\nThe answer is:\n\n  {new_n}\n-----\n  {new_d}\n\nOr\n\n{new_n / new_d}\n\n--------------\n"
    )


def mul_frac(n1: int, d1: int, n2: int, d2: int):

    new_n = n1 * n2
    new_d = d1 * d2

    print("\n" * 100)
    print(
        f"\nThe answer is:\n\n  {new_n}\n-----\n  {new_d}\n\nOr\n\n{new_n / new_d}\n\n--------------\n"
    )


def add_frac(n1: int, d1: int, n2: int, d2: int):
    print("Sorry, this function is incomplete.👨‍🔧")


def sub_frac(n1: int, d1: int, n2: int, d2: int):
    print("Sorry, this function is incomplete.👨‍🔧")


def get_frac():
    print("\n" * 100)
    while True:
        function = input(
            "'+' = Addition\n\n'-' = Subtraction\n\n'*' = Multiplication\n\n'/' = Divition\n\n' ' = End\n\nWich one do you want to do?\n\n"
        )
        if function == "":
            print("\n" * 100)
            break
        frac1 = input("\nWhat is your first fraction? ")
        frac2 = input("\nWhat is your second fraction? ")

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


get_frac()
