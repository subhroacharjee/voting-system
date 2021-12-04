import json
from typing import Tuple
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

def padding():
    return padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)

def create_pair_keys():
    '''
    This function will generate a private and public key for encryption.
    '''
    private_key = rsa.generate_private_key(public_exponent=65537, public_exponent=65537, backend=default_backend())
    public_key = private_key.public_key()
    return private_key, public_key


def seralize_public_key(public_key: rsa.RSAPublicKey):
    """
    Reset the public key to its serialized version.
    """
    return public_key.public_bytes( encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo).decode()

def deseralize_public_key(public_key:str):
    """
    Reset the seralized public key to public key
    """
    return serialization.load_pem_public_key(
            public_key.encode('utf-8'),
            default_backend()
    )

def seralize_private_key(private_key: rsa.RSAPrivateKey):
    """
    Reset the private key to its serialized version
    """
    return private_key.private_bytes(encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()).decode()

def deseralize_private_key(private_key:str):
    """
    Reset the seralized private key to public key
    """
    return serialization.load_pem_private_key(
            private_key.encode('utf-8'),
            password=None,
            backend=default_backend()
        )

def encrypt(public_key: rsa.RSAPublicKey, data:dict): 
    '''
    Data is encrypted using rsa public key
    '''
    return public_key.encrypt(json.dumps(data).encode('utf-8'), padding()).decode()

def decrypt(private_key: rsa.RSAPrivateKey, signature:str):
    '''
    Data is decrypted using rsa private key
    '''
    return private_key.decrypt(signature.encode('utf-8'), padding()).decode()

def verify(public_key: rsa.RSAPublicKey, data:dict, signature: str):
    """
    Check if the signature can be obtained by public_key
    """
    signature = signature.encode('utf-8')

    try:
        public_key.verify(signature.encode('utf-8'), json.dumps(data).encode('utf-8'), padding(), hashes.SHA256())
        return True
    except InvalidSignature:
        return False
    


