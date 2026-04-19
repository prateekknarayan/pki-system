import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from core.key_management import KeyManager

km = KeyManager()

result = km.generate_and_store_keys("user1", "strongpassword")

print("Keys generated:")
print(result)
