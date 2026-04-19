from crypto.crypto_utils import generate_rsa_key_pair, serialize_private_key, serialize_public_key
from storage.key_store import save_key


class KeyManager:

    def generate_and_store_keys(self, name: str, password: str):
        private_key, public_key = generate_rsa_key_pair()

        private_bytes = serialize_private_key(private_key, password)
        public_bytes = serialize_public_key(public_key)

        private_path = save_key(f"{name}_private.pem", private_bytes)
        public_path = save_key(f"{name}_public.pem", public_bytes)

        return {
            "private_key": private_path,
            "public_key": public_path
        }
    