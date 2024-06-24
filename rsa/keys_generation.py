import math
from .primes import generate_prime
from .utils import extend_gcd


def generate_pqn(bits: int) -> tuple[int, int, int]:
    """
    Generate two prime numbers p and q for RSA algorithm, and their product n,
    ensuring that n is within the specified bit range.

    Args:
        bits (int): The desired bit length of the modulus n.

    Returns:
        tuple[int, int, int]: A tuple containing (p, q, n), where p and q are prime numbers,
                              and n is their product.
    """
    p = q = n = 0
    upper_limit = 2 ** bits
    lower_limit = 2 ** (bits - 1) - 1

    while not (lower_limit < n < upper_limit):
        p = generate_prime(bits // 2 - 1)
        q = generate_prime(bits // 2 + 1)
        n = p * q

    return p, q, n


def find_multiplicative_inverse(num: int, mod: int) -> int:
    _, result, _ = extend_gcd(num, mod)
    return (result % mod + mod) % mod


def generate_keypair(bits: int) -> dict[str, tuple[str, str]]:
    p, q, n = generate_pqn(bits)
    phi = (p - 1) * (q - 1)

    e = 65537
    while math.gcd(phi, e) != 1:
        e = generate_prime(bits=15)

    d = find_multiplicative_inverse(e, phi)

    return {
        "public": (hex(e), hex(n)),
        "private": (hex(d), hex(n))
    }
