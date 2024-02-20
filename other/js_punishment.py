with open("mypunishment.txt", "w") as f:
    for line in range(1, 1001):
        f.write("\n{:10} I will write my lines by hand.".format(line))
