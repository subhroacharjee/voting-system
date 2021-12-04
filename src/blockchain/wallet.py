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
        
        self.type = constants.TYPES_OF_USER[type]
        if self.type == 'VOTER':
            if not data:
                raise exceptions.InvalidVoterData()

            self.public_key = sha256(json.dumps(data)).hexdigest()
            self.private_key = None
        else:
            self.private_key, self.public_key = asymetric.create_pair_keys()

