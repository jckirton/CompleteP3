mthinput = input("")
mthinput = mthinput.split(" ")
mthinput.remove("")
action = mthinput[0].lower()
numbers = mthinput[1:]

print("\n")
print(f"Action: {action}")
print(f"Numbers: {numbers}\n\n")


def arithmatic():
    result = 0

    if "add" in action:
        result = numbers[0]
        result = float(result)
        for num in numbers[1:]:
            result += float(num)
    if "sub" in action:
        result = numbers[0]
        result = float(result)
        for num in numbers[1:]:
            result -= float(num)
    if "mul" in action:
        result = numbers[0]
        result = float(result)
        for num in numbers[1:]:
            result *= float(num)
    if "div" in action:
        result = numbers[0]
        result = float(result)
        for num in numbers[1:]:
            result /= float(num)
    if "root" in action:
        rtby = float(numbers[0])
        rtby = rtby ** -1
        result = float(numbers[1]) ** rtby
    if "power" in action:
        result = float(numbers[0]) ** float(numbers[1])
        result = round(result)
    print(f"Rounded Answer: {round(result)}")
    print(f"Unedited Answer: {result}")
    print(
        "Please note that the unedited answer will always be a floating point and may experience errors in accuracy."
    )


arithmatic()
