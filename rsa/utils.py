def quick_power(base: int, exponent: int, mod: int) -> int:
    """Compute (base^exponent) % modulus efficiently."""
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        exponent >>= 1
        base = (base * base) % mod
    return result
