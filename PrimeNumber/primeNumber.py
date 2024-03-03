def primeNumber(n):
    if n == 1:
        print(f"{n} is not a prime number.")
    elif n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not a prime number.")
                print(f"{i} times {n // i} = {n}")
                break
        else:
            print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")


n = int(input("Enter an integer number: "))
primeNumber(n)
