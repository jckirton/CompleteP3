"""
Proof being tested:
    for n ∈ ℤ⁺:
    n^2 + n + 41 is prime
"""

n = 1
notPrime = False

try:
    while True:
        test = n**2 + n + 41
        for i in range(2, test):
            if test % i == 0:
                notPrime = True
                break
        if notPrime:
            print(
                f"At n={n}, n^2 + n + 41 is not pime, and is divisible by {i}.\nn^2 + n + 41 = {test}\n{test}/{i} = {test / i}"
            )
            cont = input("\nContinue?\n")
            if cont in "no":
                break
            elif cont in "yes":
                notPrime = False
        n += 1
except KeyboardInterrupt:
    print(f"\n\nTest stopped at n={n}.")
