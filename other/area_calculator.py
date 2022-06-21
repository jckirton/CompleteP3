print("\n" * 100)
shape = input(
    "What is the shape you want the area for?\n\n1: Square/Rectangle/parallelogram\n2: Rhombus/Kite/Triangle\n3: Trapezoid\n4: Hexagon\n\n"
)


def calculate(shape, x, y, sig_digits=None):
    global area
    if shape == "square":
        area = x * y
        if (area % 1) == 0:
            area = f"Area = {int(area)}"
        elif sig_digits != None:
            area = f"Area = {round(area, sig_digits)}"
    elif shape == "triangle":
        area = (x * y) / 2
        if (area % 1) == 0:
            area = f"Area = {int(area)}"
        elif sig_digits != None:
            area = f"Area = {round(area, sig_digits)}"
    elif shape == "trapezoid":
        area = (y * (x[0] + x[1])) / 2
        if (area % 1) == 0:
            area = f"Area = {int(area)}"
        elif sig_digits != None:
            area = f"Area = {round(area, sig_digits)}"
    elif shape == "hexagon":
        area = ((3 * (3 ** (3**-1))) / 2) * (x**2)
        if (area % 1) == 0:
            area = f"Area = {int(area)}"
        elif sig_digits != None:
            area = f"Area = {round(area, sig_digits)}"


if shape == "1":
    print("\n" * 100)
    dimensions = input(
        "Please enter your x and y demensions, and the amount of significant digits to round to, with no input meaning no rounding.\nFormat: x y sig_digits\n"
    ).split()
    numbers = []
    for n in dimensions:
        if len((n.split("/"))) == 2:
            numbers.append((float(n.split("/")[0]) / float(n.split("/")[1])))
        else:
            if (float(n.split("/")[0]) % 1) == 0:
                numbers.append(int(n.split("/")[0]))
            else:
                numbers.append(float(n.split("/")[0]))
    if len(numbers) > 2:
        calculate("square", float(numbers[0]), float(numbers[1]), int(numbers[2]))
    else:
        calculate("square", float(numbers[0]), float(numbers[1]))
    print("\n" * 100)
    print(area)
elif shape == "2":
    print("\n" * 100)
    dimensions = input(
        "Please enter your base and height demensions, and the amount of significant digits to round to, with no input meaning no rounding.\nFormat: b h sig_digits\n"
    ).split()
    numbers = []
    for n in dimensions:
        if len((n.split("/"))) == 2:
            numbers.append((float(n.split("/")[0]) / float(n.split("/")[1])))
        else:
            if (float(n.split("/")[0]) % 1) == 0:
                numbers.append(int(n.split("/")[0]))
            else:
                numbers.append(float(n.split("/")[0]))
    if len(numbers) > 2:
        calculate("triangle", float(numbers[0]), float(numbers[1]), int(numbers[2]))
    else:
        calculate("triangle", float(numbers[0]), float(numbers[1]))
    print("\n" * 100)
    print(area)
elif shape == "3":
    print("\n" * 100)
    dimensions = input(
        f"Please enter your base and height demensions, and the amount of significant digits to round to, with no input meaning no rounding.\nFormat: b₁ b₂ h sig_digits\n"
    ).split()
    numbers = []
    for n in dimensions:
        if len((n.split("/"))) == 2:
            numbers.append((float(n.split("/")[0]) / float(n.split("/")[1])))
        else:
            if (float(n.split("/")[0]) % 1) == 0:
                numbers.append(int(n.split("/")[0]))
            else:
                numbers.append(float(n.split("/")[0]))
    if len(numbers) > 3:
        calculate(
            "trapezoid",
            [float(numbers[0]), float(numbers[1])],
            float(numbers[2], int(numbers[3])),
        )
    else:
        calculate(
            "trapezoid",
            [float(numbers[0]), float(numbers[1])],
            float(numbers[2]),
        )
    print("\n" * 100)
    print(area)
elif shape == "4":
    print("\n" * 100)
    dimensions = input(
        f"Please enter the length of one of the sides, and the amount of significant digits to round to, with no input meaning no rounding.\nFormat: a sig_digits\n"
    ).split()
    numbers = []
    for n in dimensions:
        if len((n.split("/"))) == 2:
            numbers.append((float(n.split("/")[0]) / float(n.split("/")[1])))
        else:
            if (float(n.split("/")[0]) % 1) == 0:
                numbers.append(int(n.split("/")[0]))
            else:
                numbers.append(float(n.split("/")[0]))
    if len(numbers) > 1:
        calculate("hexagon", float(numbers[0]), None, int(numbers[1]))
    else:
        calculate("hexagon", float(numbers[0]), None)
    print("\n" * 100)
    print(area)
