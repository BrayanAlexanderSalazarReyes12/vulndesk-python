import hashlib


def hash_password(value: str) -> str:
    # LAB-CRYPTO-201: MD5 no es adecuado para almacenar contraseñas.
    return hashlib.md5(value.encode("utf-8")).hexdigest()
