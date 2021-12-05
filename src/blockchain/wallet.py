'''
An wallet can be thought of an user in block chain. This user in terms creates data
encrypted data with a public key which works as an identity for the user and private key works as well private key.
Now in this block chain we will have 2 types of users 
1. Voter : with only public key for identification
2. Candidate: with both public key and private key and each candidate will have a miner related to it
'''
import json

from hashlib import sha256
from src import constants,exceptions
from src.utils import asymetric

class Wallet:

    def __init__(self, type, data=None):
        if type not in constants.TYPES_OF_USER:
            raise exceptions.ImproperTypeError()
        data['type'] = constants.TYPES_OF_USER[type]
        self.balance = constants.INITIAL_BALANCE
        self.wallet_id = sha256(json.dumps(data).encode('utf-8')).hexdigest()
        pri, pub = asymetric.create_rsa_pair_keys()
        self.private_key = asymetric.seralize_private_key(pri)
        self.public_key = asymetric.seralize_public_key(pub)
            
    
    @staticmethod
    def create_signature(private_key:str, data:dict):
        pri_k = asymetric.deseralize_private_key(private_key)
        signature = asymetric.sign(pri_k, json.dumps(data))
        return signature
    
    @staticmethod
    def verify_signature(public_key:str, data:dict, signature:str):
        pub_k = asymetric.deseralize_public_key(public_key)
        return asymetric.verify(pub_k, json.dumps(data), signature)
    
    @staticmethod
    def current_balance(blockchain, wallet_id):
        if not blockchain:
            raise ValueError('Invalid blockchain')
        
        current_balance = constants.INITIAL_BALANCE

        for chain in blockchain.chain:
            for tx in chain.data:
                if tx['input']['sender'] == wallet_id:
                    current_balance-=tx['input']['amount']
                elif wallet_id in tx['output']:
                    current_balance += tx['output'][wallet_id]
        
        return current_balance
