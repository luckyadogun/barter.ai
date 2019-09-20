from cryptography.fernet import Fernet

class Hasher:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def make_hash(self, secret_key):
        hash = self.cipher.encrypt(str.encode(secret_key))
        return hash

    def reveal_hash(self, hash):
        unhash = self.cipher.decrypt(hash)
        return unhash

