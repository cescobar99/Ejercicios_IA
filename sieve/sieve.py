def primes(limit):
    if limit < 2:
        return []

    multiples, primes = set(), [2]

    for num in range(3, limit + 1, 2):
        if not num in multiples:
            primes.append(num)
            multiples.update(range(num ** 2, limit, num))

    return primes
