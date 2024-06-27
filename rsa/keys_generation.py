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
    upper_limit = 2**bits
    lower_limit = 2 ** (bits - 1) - 1

    while not (lower_limit < n < upper_limit):
        p = generate_prime(bits // 2 - 1)
        q = generate_prime(bits // 2 + 1)
        n = p * q

    return p, q, n


def find_multiplicative_inverse(num: int, mod: int) -> int:
    """Find the (positive) multiplicative inverse of a number under a given modulus."""
    _, result, _ = extend_gcd(num, mod)
    return (result % mod + mod) % mod


def generate_keypair(bits: int) -> dict[str, tuple[str, str]]:
    """
    Generate RSA public key and private key.

    Args:
        bits (int): The desired bit length of the modulus n.

    Returns:
        dict[str, tuple[str, str]]: A dictionary containing the `public` and `private` keys.
                                    The keys are represented as tuples of hexadecimal strings.
    """
    p, q, n = generate_pqn(bits)
    phi = (p - 1) * (q - 1)

    # Use a common choice for public exponent
    e = 65537
    while e >= phi:
        e = generate_prime(bits=bits - 1)
    while math.gcd(phi, e) != 1:
        e = generate_prime(bits=min(15, bits - 1))

    d = find_multiplicative_inverse(e, phi)

    return {"public": (f"{e:x}", f"{n:x}"), "private": (f"{d:x}", f"{n:x}")}
