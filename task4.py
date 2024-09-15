l, r = map(int, input().split())

result_count = 0
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
for num in range(l, r + 1):
    if num > 1 and not is_prime(num):  # Проверка, является ли число1 составным
        divisors_count = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divisors_count += 1
                if i != num // i:
                    divisors_count += 1
        if is_prime(divisors_count):
            result_count += 1

print(result_count)