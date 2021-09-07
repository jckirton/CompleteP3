import time

with open("diary", "w") as file:
    file.write(input("What do you want to write?\n"))
    print("Done")
    time.sleep(1)
    print("\n" * 100)
