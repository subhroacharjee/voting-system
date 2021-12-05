import json
from cryptography.hazmat.primitives import hashes
from tests.test_constants import STR_MESSAGE, DICT_DATA

from src.utils import asymetric

"""
    tests wil be
    1. verify if two keys are generated or not
    2. check if the two keys are working or not
    3. use serialization and deserialization and verify working or not
    4. use a serialized public key to call verify function
"""

def test_create_pair_keys():
    private_key, public_key = asymetric.create_rsa_pair_keys()

    encrypted_data = public_key.encrypt(STR_MESSAGE, 
        asymetric.put_padding()
    )
    assert private_key.decrypt(encrypted_data, 
        asymetric.put_padding()
    ) == STR_MESSAGE

def test_encrpyt_decrypt():
    private_key, public_key = asymetric.create_rsa_pair_keys()

    ENC_DATA = asymetric.rsa_encrypt(public_key, DICT_DATA)
    S_PRI = asymetric.seralize_private_key(private_key)
    S_PUB = asymetric.seralize_public_key(public_key)

    private_key = asymetric.deseralize_private_key(S_PRI)
    public_key = asymetric.deseralize_public_key(S_PUB)

    enc = asymetric.rsa_encrypt(public_key, DICT_DATA)
    assert enc != ENC_DATA


    payload = json.loads(asymetric.rsa_decrypt(private_key, ENC_DATA))

    assert payload == DICT_DATA
