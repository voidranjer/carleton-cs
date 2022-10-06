def is_prime(N):
    counter = 2
    while counter <= N:
        if (N % counter == 0) and (N != counter):
            return False
        counter += 1
    return True


def largest_prime_factor(N):
    # Assuming that N > 0
    X = 1
    max_prime_factor = X

    while X <= N:
        if (N % X == 0) and is_prime(X):
            max_prime_factor = X
        X += 1

    return max_prime_factor
