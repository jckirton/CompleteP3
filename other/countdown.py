import time

print("\n" * 100)
hi = int(input("How long is this countdown?\n"))

while hi:
    print("\n" * 100)
    print(hi)
    time.sleep(1)
    hi -= 1
print("\n" * 100)
print("Blastoff!!!")
