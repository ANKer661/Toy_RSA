def quick_power(base: int, exponent: int, mod: int) -> int:
    """Compute (base^exponent) % modulus efficiently."""
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        exponent >>= 1
        base = (base * base) % mod
    return result


def extend_gcd(a: int, b: int) -> tuple[int, int]:
    if b == 0:
        return a, 1, 0

    gcd, x, y = extend_gcd(b, a % b)
    return gcd, y, x - y * (a // b)
