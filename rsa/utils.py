def quick_power(base: int, exponent: int, mod: int) -> int:
    """Compute (base^exponent) % modulus efficiently."""
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        exponent >>= 1
        base = (base * base) % mod
    return result


def extend_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Compute the greatest common divisor of a and b along with the coefficients
    of Bézout's identity.

    This function is particularly useful in RSA for finding the multiplicative
    inverse of the public exponent e with respect to φ(n),
    where φ(n) = (p - 1) * (q - 1) and gcd(e, φ(n)) = 1.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        tuple[int, int, int]: A tuple (gcd, x, y) where gcd is the greatest
                              common divisor of a and b, and x and y are the
                              coefficients of Bézout's identity, i.e.,
                              gcd = a * x + b * y.
    """
    if b == 0:
        return a, 1, 0

    gcd, x, y = extend_gcd(b, a % b)
    return gcd, y, x - y * (a // b)
