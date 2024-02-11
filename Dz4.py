import random

class Encryptor:
    def __init__(self):
        self.secret_number = None

    def encrypt(self, number):
        self.secret_number = number + random.randint(1, 100)

    def decrypt(self):
        if self.secret_number is not None:
            return self.secret_number - random.randint(1, 100)
        else:
            return None

encryptor = Encryptor()
number = 42
encryptor.encrypt(number)

print("1 число:", encryptor.secret_number)
print("2 число:", encryptor.decrypt())
