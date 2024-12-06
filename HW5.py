import math

# Задача №1
def find_sin(x,y):
    x = abs(x)
    y = abs(y)
    gipotenuza = math.sqrt(x**2 + y**2)
    katet = y
    return katet / gipotenuza
def find_min_angle_point(X, Y, Z):
    points = [X,Y,Z]
    min_angle = 1
    for point in points:
        if find_sin(point[0], point[1]) < min_angle:
            min_angle = find_sin(point[0], point[1])
            min2 = point
    return min2
X = (1, 2) 
Y = (3, 1) 
Z = (2, 1) 
min_point = find_min_angle_point(X, Y, Z)
print(f"Координаты точки с минимальным углом: {min_point}")


# Задача №2
def sito_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * 2, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]
def find_palindromic_primes(n):
    palindromic_primes = []
    primes = sito_of_eratosthenes(n) 
    for prime in primes:
        binary_representation = bin(prime)[2:] 
        if binary_representation == binary_representation[::-1]:
            palindromic_primes.append(prime)
    return palindromic_primes
n = 50
result = find_palindromic_primes(n)
print(f"Простые числа <= {n}, двоичная запись которых является палиндромом: {result}")