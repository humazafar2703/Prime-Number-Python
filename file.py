def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start_num = 1
end_num = 250
primes_list = find_primes(start_num, end_num)

# Write results to a file
file_path = 'results.txt'
with open(file_path, 'w') as file:
    for prime in primes_list:
        file.write(str(prime) + '\n')

print(f"Prime numbers between {start_num} and {end_num} have been saved to {file_path}.")
