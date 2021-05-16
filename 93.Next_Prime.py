def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def find_next_prime(n):
    next_prime = 0
    current = n
    while next_prime < n:
        current += 1
        if is_prime(current):
            next_prime = current
    print(f'Next prime number after {n} is {next_prime}')


# First 25 prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
find_next_prime(2)
find_next_prime(4)
find_next_prime(7)
find_next_prime(8)
find_next_prime(9)
find_next_prime(27)
find_next_prime(51)
