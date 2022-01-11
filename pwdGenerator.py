from hashlib import sha256

def hashing(pwd: str, num_char: int) -> str:
    # кодирование
    byte_str = pwd.encode()
    # хеширование
    hash_str = sha256(byte_str)
    # преобразование в строку 16-ричных чисел
    hex_str = hash_str.hexdigest()
    # возврат значения
    if num_char != 0:
        return hex_str[:num_char]
    return hex_str