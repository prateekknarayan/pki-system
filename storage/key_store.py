import os

KEY_DIR = "storage/keys"


def save_key(filename: str, data: bytes):
    os.makedirs(KEY_DIR, exist_ok=True)

    path = os.path.join(KEY_DIR, filename)

    with open(path, "wb") as f:
        f.write(data)

    return path
