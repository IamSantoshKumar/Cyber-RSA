from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import sys

def generate_keys():
    modulus_length = 1024
    key = RSA.generate(modulus_length)
    privKey = key.exportKey('PEM').decode() 
    pubKey =  key.publickey().exportKey('PEM').decode()  
    with open('rsakey.pem', 'w') as file:  
        file.write(privKey)  
    with open('rsapub.pem', 'w') as file:  
        file.write(pubKey)
    return privKey,pubKey   

def encrypt(a_message, private_key):
    encryptor = PKCS1_OAEP.new(private_key)
    encrypted_msg = encryptor.encrypt(a_message)
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    return encoded_encrypted_msg

def decrypt(encoded_encrypted_msg, public_key):
    encryptor = PKCS1_OAEP.new(public_key)
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    decoded_decrypted_msg = encryptor.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg

def PrivateKey():
    private=RSA.importKey(open('rsakey.pem', 'r').read())
    return private
    
def PublicKey():
    public=RSA.importKey(open('rsapub.pem', 'r').read())
    return public