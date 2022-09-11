import time

print("\n" * 100)
length = int(input("How long is this countdown?\n"))

while length:
    print("\n" * 100)
    print(length)
    time.sleep(1)
    length -= 1
print("\n" * 100)
print("Blastoff!!!")
