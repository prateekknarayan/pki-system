from crypto.crypto_utils import (
    generate_rsa_key_pair,
    serialize_private_key,
    serialize_public_key,
    create_self_signed_certificate,
    serialize_certificate
)
from storage.key_store import save_key


class RootCA:

    def create_root_ca(self, name: str, password: str):
        private_key, public_key = generate_rsa_key_pair()

        cert = create_self_signed_certificate(private_key, name)

        private_bytes = serialize_private_key(private_key, password)
        public_bytes = serialize_public_key(public_key)
        cert_bytes = serialize_certificate(cert)

        private_path = save_key(f"{name}_root_private.pem", private_bytes)
        public_path = save_key(f"{name}_root_public.pem", public_bytes)
        cert_path = save_key(f"{name}_root_cert.pem", cert_bytes)

        return {
            "private_key": private_path,
            "public_key": public_path,
            "certificate": cert_path
        }
    