def prime_checker(number):
    for n in range(2, number):
        if number % n  == 0:
            print("It is not a prime number")
            return
    print("It is a prime number")
n = int(input("Check this number: "))
prime_checker(number=n)

