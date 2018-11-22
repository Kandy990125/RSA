# -*- coding=UTF-8 -*-
from Crypto import Random
from Crypto.PublicKey import RSA
from RSA_PKCS1_V1_5 import RSA_PKCS1_v1_5
from RSA_PKCS1_OAEP import RSA_PKCS1_OAEP
'''RSA-PKCS1-V1-5'''
def rsa_pkcs1_v1_5():
    print "RSA-PKCS1-V1-5"
    # 程序输入：文本串 s
    # 伪随机数生成器
    random_generator = Random.new().read
    # rsa算法生成实例
    rsa = RSA.generate(1024, random_generator)
    # 私钥
    private_key = rsa.exportKey()
    # 公钥
    public_key = rsa.publickey().exportKey()
    # print "生成的密钥为:", private_key
    # print "生成的公钥为:", public_key
    s = raw_input("请输入明文：")
    rsa_pkcs1_v1_5 = RSA_PKCS1_v1_5()
    c1 = rsa_pkcs1_v1_5.encrypt(s, public_key)
    c2 = rsa_pkcs1_v1_5.encrypt(s, public_key)
    print "加密结果为(1)：", c1
    print "加密结果为(2)：", c2
    rsa_pkcs1_v1_5_de = RSA_PKCS1_v1_5()
    print "解密结果为(1)：", rsa_pkcs1_v1_5_de.decrypt(c1,private_key,random_generator)
    print "解密结果为(2)：", rsa_pkcs1_v1_5_de.decrypt(c2,private_key,random_generator)
'''RSA-PKCS1-OAEP'''
def rsa_pkcs1_oaep():
    print "RSA-PKCS1-OAEP"
    # 程序输入：文本串 s
    # 伪随机数生成器
    random_generator = Random.new().read
    # rsa算法生成实例
    rsa = RSA.generate(1024, random_generator)
    # 私钥
    private_key = rsa.exportKey()
    # 公钥
    public_key = rsa.publickey().exportKey()
    # print "生成的密钥为:", private_key
    # print "生成的公钥为:", public_key
    s = raw_input("请输入明文：")
    rsa_pkcs1_oaep = RSA_PKCS1_OAEP()
    c1 = rsa_pkcs1_oaep.encrypt(s, public_key)
    c2 = rsa_pkcs1_oaep.encrypt(s, public_key)
    print "加密结果为(1)：", c1
    print "加密结果为(2)：", c2
    print "解密结果为(1)：", rsa_pkcs1_oaep.decrypt(c1, private_key)
    print "解密结果为(2)：", rsa_pkcs1_oaep.decrypt(c2, private_key)

if __name__ == "__main__":
    rsa_pkcs1_v1_5()
    rsa_pkcs1_oaep()

