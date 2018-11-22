# -*- coding=UTF-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
class RSA_PKCS1_v1_5:
    def __init__(self):
        pass

    def encrypt(self, s, public_key):
        key = RSA.importKey(public_key)
        pkcs1 = PKCS1_v1_5.new(key)     # 根据公钥key对明文进行填充
        return base64.b64encode(pkcs1.encrypt(s))

    def decrypt(self, c, private_key, random_generator):
        rsakey = RSA.importKey(private_key)
        cipher = PKCS1_v1_5.new(rsakey)
        return cipher.decrypt(base64.b64decode(c), random_generator)