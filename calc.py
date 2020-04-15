def add(n1: int, n2: int):
    print("\n" * 100)
    print(f"The answer is:\n\n      {n1 + n2}\n\n--------------\n")


def sub(n1: int, n2: int):
    print("\n" * 100)
    print(f"The answer is:\n\n      {n1 - n2}\n\n--------------\n")


def mul(n1: int, n2: int):
    print("\n" * 100)
    print(f"The answer is:\n\n      {n1 * n2}\n\n--------------\n")


def div(n1: int, n2: int):
    print("\n" * 100)
    print(f"The answer is:\n\n      {n1 / n2}\n\n--------------\n")


def get_num():
    print("\n" * 100)
    while True:
        function = input(
            "'+' = Addition\n\n'-' = Subtraction\n\n'*' = Multiplication\n\n'/' = Divition\n\n' ' = End\n\nWich one do you want to do?\n\n"
        )
        if function == "":
            print("\n" * 100)
            break
        n1 = int(input("\nWhat is your first number? "))
        n2 = int(input("\nWhat is your second number? "))

        if function == "/":
            div(n1, n2)
        elif function == "*":
            mul(n1, n2)
        elif function == "-":
            sub(n1, n2)
        elif function == "+":
            add(n1, n2)


get_num()
