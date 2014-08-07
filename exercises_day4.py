def gcd(number_one, number_two):
	remainder = number_one % number_two
	while remainder != 0:
		new_remainder = number_two % remainder
		number_two = remainder
		remainder = new_remainder
	return number_two

print gcd(1071, 462)


def find_primes():
	numbers = range(2, 122)
	primes = []
	while len(numbers) != 0:
		primes.append(numbers[0])
		p = numbers[0]
		numbers_erased = []
		for number in numbers:
			if number % p == 0:
				numbers.remove(number)
	return primes

print find_primes()
	