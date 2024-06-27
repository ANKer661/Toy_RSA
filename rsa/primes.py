import secrets

from .utils import quick_power


def miller_rabin_test(n: int, test_times: int = 16) -> bool:
    """
    Perform the Miller-Rabin primality test on a given integer.
    (https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)

    Args:
        n (int): The number to test for primality.
        test_times (int): The number of testing iterations (default is 16).

    Returns:
        bool: True if n is likely a prime, False if n is composite.
    """
    if n < 3 or (n & 1) == 0:
        return n == 2

    # a^2 ≡ 1 (mod n)  =>  a = 1 or a = n - 1
    # let n - 1 = u * 2^k, u is odd
    k = 0
    u = n - 1
    while (u & 1) == 0:
        u = u >> 1
        k += 1

    for _ in range(test_times):
        a = 2 + secrets.randbelow(n - 2)  # a in [2, n)
        v = quick_power(a, u, n)
        if v == 1:
            continue

        i = 0
        while i < k:
            if v == (n - 1):
                break
            v = (v * v) % n
            i += 1

        # if the loop above reaches (i == k)
        # there exist v such that v != (n - 1) and v^2 ≡ 1 (mod n) => n is Composite
        # or
        # a^(n-1) ≡/ 1 (mod n)
        # by Fermat little thm.: a^(n-1) ≡ 1 (mod n) if n is prime  =>  n is Composite
        if i == k:
            return False

    return True


def generate_prime(bits: int) -> int:
    """Generate a prime number within the specified bit length."""
    while True:
        prime_candidate = secrets.randbits(bits)
        if (prime_candidate & 1) == 0:
            prime_candidate += 1
        if miller_rabin_test(prime_candidate):
            return prime_candidate
