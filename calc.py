from typing import Union


def add(n1: Union[int, float], n2: Union[int, float]):
    print("\n" * 100)
    fin_num = n1 + n2
    if fin_num % 1 == 0:
        fin_num = int(fin_num)
    print(f"The answer is:\n\n      {fin_num}\n\n--------------\n")


def sub(n1: Union[int, float], n2: Union[int, float]):
    print("\n" * 100)
    fin_num = n1 - n2
    if fin_num % 1 == 0:
        fin_num = int(fin_num)
    print(f"The answer is:\n\n      {fin_num}\n\n--------------\n")


def mul(n1: Union[int, float], n2: Union[int, float]):
    print("\n" * 100)
    fin_num = n1 * n2
    if fin_num % 1 == 0:
        fin_num = int(fin_num)
    print(f"The answer is:\n\n      {fin_num}\n\n--------------\n")


def div(n1: Union[int, float], n2: Union[int, float]):
    print("\n" * 100)
    fin_num = n1 / n2
    if fin_num % 1 == 0:
        fin_num = int(fin_num)
    print(f"The answer is:\n\n      {fin_num}\n\n--------------\n")


def get_num():
    print("\n" * 100)
    invalid_numbers = True
    while invalid_numbers:
        function = input(
            "'+' = Addition\n\n'-' = Subtraction\n\n'*' = Multiplication\n\n'/' = Divition\n\n' ' = End\n\nWich one do you want to do?\n\n"
        )
        if function == "":
            print("\n" * 100)
            break
        n1 = input("\nWhat is your first number? ")
        try:
            new_n1 = int(n1)
        except Exception:
            new_n1 = float(n1)

        n2 = input("\nWhat is your second number? ")
        try:
            new_n2 = int(n2)
        except Exception:
            new_n2 = float(n2)

        if function == "/":
            div(new_n1, new_n2)
        elif function == "*":
            mul(new_n1, new_n2)
        elif function == "-":
            sub(new_n1, new_n2)
        elif function == "+":
            add(new_n1, new_n2)


get_num()
