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
    if len(dimensions) > 2:
        calculate(
            "square", float(dimensions[0]), float(dimensions[1]), int(dimensions[2])
        )
    else:
        calculate("square", float(dimensions[0]), float(dimensions[1]))
    print("\n" * 100)
    print(area)
elif shape == "2":
    print("\n" * 100)
    dimensions = input(
        "Please enter your base and height demensions, and the amount of significant digits to round to, with no input meaning no rounding.\nFormat: b h sig_digits\n"
    ).split()
    if len(dimensions) > 2:
        calculate(
            "triangle", float(dimensions[0]), float(dimensions[1]), int(dimensions[2])
        )
    else:
        calculate("triangle", float(dimensions[0]), float(dimensions[1]))
    print("\n" * 100)
    print(area)
elif shape == "3":
    print("\n" * 100)
    dimensions = input(
        f"Please enter your base and height demensions, and the amount of significant digits to round to, with no input meaning no rounding.\nFormat: b₁ b₂ h sig_digits\n"
    ).split()
    if len(dimensions) > 3:
        calculate(
            "trapezoid",
            [float(dimensions[0]), float(dimensions[1])],
            float(dimensions[2], int(dimensions[3])),
        )
    else:
        calculate(
            "trapezoid",
            [float(dimensions[0]), float(dimensions[1])],
            float(dimensions[2]),
        )
    print("\n" * 100)
    print(area)
elif shape == "4":
    print("\n" * 100)
    dimensions = input(
        f"Please enter the length of one of the sides, and the amount of significant digits to round to, with no input meaning no rounding.\nFormat: a sig_digits\n"
    ).split()
    if len(dimensions) > 1:
        calculate("hexagon", float(dimensions[0]), None, float(dimensions[1]))
    else:
        calculate("hexagon", float(dimensions[0]), None)
    print("\n" * 100)
    print(area)
