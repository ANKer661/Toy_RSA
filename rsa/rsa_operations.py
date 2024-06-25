from .utils import quick_power
from .keys_generation import generate_keypair


def pre_processing(message: str, encoding: str = "utf-8") -> str:
    """
    Convert a message to an integer for RSA encryption.

    Args:
        message (str): The message to be preprocessed.
        encoding (str): The encoding used to convert the message to bytes (default: "utf-8").

    Returns:
        str: The integer representation of the message as a string.

    Examples:
        >>> pre_processing("No")
        "20079"
    """
    message_bytes = message.encode(encoding)
    return str(int.from_bytes(message_bytes, "big"))


def encrypt(m: str, public_keys: tuple[str, str]) -> str:
    """
    Encrypts a given message with the provided public key (e, n).
    RSA encryption: m' = m**e % n

    Args:
        m (str): The message to be encrypted, represented as a string of digits.
        public_keys (tuple[str, str]): A tuple containing the public key
                                       (e, n) in hexadecimal format.

    Returns:
        str: The encrypted message, represented as a hexadecimal string.

    Examples:
        >>> encrypt("20079", ('10001', '9e7ef'))
        "40610"
    """
    e, n = public_keys
    return f"{quick_power(int(m), int(e, 16), int(n, 16)):x}"


def decrypt(encrypted_m: str, private_keys: tuple[str, str]) -> str:
    """
    Decrypts an RSA-encrypted message.
    RSA decryption: m = (m')**d % n

    Args:
        encrypted_m (str): The encrypted message, represented as a hexadecimal string.
        private_keys (tuple[str, str]): A tuple containing the private key
                                        (d, n) in hexadecimal format.

    Returns:
        str: The decrypted message represented as a string of digits.

    Examples:
        >>> decrypt("40610", ('38a89', '9e7ef'))
        "20079"
    """
    d, n = private_keys
    encrypted_m, d, n = int(encrypted_m, 16), int(d, 16), int(n, 16)
    return quick_power(encrypted_m, d, n)


def post_processing(message: str, encoding: str = "utf-8"):
    """
    Convert an integer back to a byte sequence and decode it to a string.

    Args:
        message (str): The decrypted message represented as a string of digits.
        encoding (str): The encoding used to decode the bytes back to a string (default: "utf-8").

    Returns:
        str: The original message.

    Examples:
        >>> post_processing("20079")
        "No"
    """
    decrypted_int = int(message)
    byte_length = (decrypted_int.bit_length() + 7) // 8
    decrypted_bytes = decrypted_int.to_bytes(byte_length, "big")
    return decrypted_bytes.decode(encoding)


def rsa_pipeline(m: str, keys: dict[str, tuple[str, str]]) -> str:
    """
    Perform RSA encryption and decryption on a message.

    Args:
        m (str): The message to be encrypted and then decrypted.
        keys (dict[str, tuple[str, str]]): A dictionary containing the `public` and `private` keys.
                                           The keys are represented as tuples of hexadecimal strings.

    Returns:
        str: The decrypted message after encryption and decryption.

    Example:
        >>> keys = {
        ...     'public': ('10001', '200376b73967fad6d618371a07ab'), 
        ...     'private': ('26ee0f5fa09fa08d59e7295ac09', '200376b73967fad6d618371a07ab')
        ... }
        >>> rsa_pipeline("Hello, World!", keys)
        'Hello, World!'
    """
    m = pre_processing(m)
    m_p = encrypt(m, keys["public"])
    m = decrypt(m_p, keys["private"])
    return post_processing(m)
