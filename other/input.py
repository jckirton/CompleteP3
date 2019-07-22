while True:
    try:
        fav_num = int(input("What is your favourite number? "))
    except ValueError as error:
        print("That's not a number. Try again \nError is: " + str(error).capitalize())
        continue
    else:
        print("Mine too!")
        break
