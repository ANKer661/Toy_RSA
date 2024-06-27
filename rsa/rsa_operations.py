from dataclasses import dataclass

from .utils import quick_power


@dataclass
class RSAOutputs:
    """
    Data class to store intermediate results of RSA encryption and decryption.
    """

    message_as_number: str
    encrypted_message: str
    decrypted_message: str
    final_message: str


def pre_processing(message: str, encoding: str = "utf-8") -> str:
    """
    Convert a message to an integer for RSA encryption.

    Args:
        message (str): The message to be preprocessed.
        encoding (str): The encoding used to convert the message to bytes (default: "utf-8").

    Returns:
        str: The integer representation of the message as a hexadecimal string.

    Examples:
        >>> pre_processing("No")
        "20079"
    """
    message_bytes = message.encode(encoding)
    return f"{int.from_bytes(message_bytes, 'big'):x}"


def encrypt(message_as_number: str, public_keys: tuple[str, str]) -> str:
    """
    Encrypts a given message with the provided public key (e, n).
    RSA encryption: m' = m**e % n

    Args:
        message_as_number (str): The message to be encrypted, represented as a hexadecimal string.
        public_keys (tuple[str, str]): A tuple containing the public key
                                       (e, n) in hexadecimal format.

    Returns:
        str: The encrypted message, represented as a hexadecimal string.

    Examples:
        >>> encrypt("20079", ("10001", "9e7ef"))
        "40610"
    """
    e, n = public_keys
    e, n = int(e, 16), int(n, 16)
    message_as_number = int(message_as_number, 16)

    if message_as_number >= n:
        raise ValueError("Message is too long for the given key size")

    encrypted_message = quick_power(message_as_number, e, n)
    return f"{encrypted_message:x}"


def decrypt(encrypted_message: str, private_keys: tuple[str, str]) -> str:
    """
    Decrypts an RSA-encrypted message.
    RSA decryption: m = (m')**d % n

    Args:
        encrypted_message (str): The encrypted message, represented as a hexadecimal string.
        private_keys (tuple[str, str]): A tuple containing the private key
                                        (d, n) in hexadecimal format.

    Returns:
        str: The decrypted message represented as a hexadecimal string.

    Examples:
        >>> decrypt("40610", ("38a89", "9e7ef"))
        "20079"
    """
    d, n = private_keys
    encrypted_message, d, n = int(encrypted_message, 16), int(d, 16), int(n, 16)
    return f"{quick_power(encrypted_message, d, n):x}"


def post_processing(message: str, encoding: str = "utf-8"):
    """
    Convert an integer back to a byte sequence and decode it to a string.

    Args:
        message (str): The decrypted message represented as a hexadecimal string.
        encoding (str): The encoding used to decode the bytes back to a string (default: "utf-8").

    Returns:
        str: The original message.

    Examples:
        >>> post_processing("20079")
        "No"
    """
    decrypted_message_as_number = int(message, 16)
    byte_length = (decrypted_message_as_number.bit_length() + 7) // 8
    decrypted_bytes = decrypted_message_as_number.to_bytes(byte_length, "big")
    return decrypted_bytes.decode(encoding)


def rsa_pipeline(m: str, keys: dict[str, tuple[str, str]]) -> tuple[str, RSAOutputs]:
    """
    Perform RSA encryption and decryption on a message.

    Args:
        m (str): The message to be encrypted and then decrypted.
        keys (dict[str, tuple[str, str]]): A dictionary containing the `public` and `private` keys.
                                           The keys are represented as tuples of hexadecimal strings.

    Returns:
        tuple[str, RSAOutputs]: A tuple containing the decrypted message and an instance of RSAOutputs
                                with intermediate results.

    Example:
        >>> keys = {
        ...     "public": ("10001", "200376b73967fad6d618371a07ab"),
        ...     "private": (
        ...         "26ee0f5fa09fa08d59e7295ac09",
        ...         "200376b73967fad6d618371a07ab",
        ...     ),
        ... }
        >>> rsa_pipeline("Hello, World!", keys)[0]
        'Hello, World!'
    """
    message_as_number = pre_processing(m)
    encrypted_message = encrypt(message_as_number, keys["public"])
    decrypted_message = decrypt(encrypted_message, keys["private"])
    final_message = post_processing(decrypted_message)

    return final_message, RSAOutputs(
        message_as_number, encrypted_message, decrypted_message, final_message
    )
