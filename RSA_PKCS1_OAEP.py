# -*- coding=UTF-8 -*-
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
class RSA_PKCS1_OAEP:
    def __init__(self):
        pass
        # self.message = s
        # self.cipher = c

    def encrypt(self, s, public_key):
        key = RSA.importKey(public_key)
        pkcs1 = PKCS1_OAEP.new(key)     # 根据公钥key对明文进行填充
        return base64.b64encode(pkcs1.encrypt(s))

    def decrypt(self, c, private_key):
        rsakey = RSA.importKey(private_key)
        cipher = PKCS1_OAEP.new(rsakey)
        cipher_text =base64.b64decode(c)
        return cipher.decrypt(cipher_text)