import time

stage1 = """           ____
          /    \\          /
         /      \\        /
        |        |      /
        |        |     /
         \\      /     /
          \\____/     /
          /    \\    /
         /      \\  /
        /        \\/
       /          \\       """
stage2 = """           ____
          /    \\      |
         /      \\     |
        |        |    |
        |        |    |
         \\      /     |
          \\____/     /
          /    \\    /
         /      \\  /
        /        \\/
       /          \\       """
stage3 = """           ____
          /    \\   \\
         /      \\   \\
        |        |   \\
        |        |    \\
         \\      /     |
          \\____/     /
          /    \\    /
         /      \\  /
        /        \\/
       /          \\"""

while True:
    print("\n" * 100)
    print(stage1)
    time.sleep(0.15)
    print("\n" * 100)
    print(stage2)
    time.sleep(0.15)
    print("\n" * 100)
    print(stage3)
    time.sleep(0.15)
    print("\n" * 100)
    print(stage2)
    time.sleep(0.15)
