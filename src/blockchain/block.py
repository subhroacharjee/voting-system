import uuid
import json
import time
from src.constants import GENESIS_DATA, HOUR, UPPER_LIMIT_MINE_RATE
from src.utils import hash, hex_to_bin
from src.exceptions import EmptyDataPayloadError
class Block:

    def __init__(self,id, timestamp, nonce, hash, difficulty, prev_hash, data):
        self.id = id 
        self.timestamp = timestamp
        self.nonce = nonce 
        self.difficulty = difficulty
        self.prev_hash = prev_hash
        self.hash = hash
        self.data = data
    
    def __eq__(self, __o: object) -> bool:
        return __o.__dict__ == self.__dict__
        pass
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def genesis():
        return Block(**GENESIS_DATA)
    
    @staticmethod
    def validate(last_block, block):
        '''
        A block is valid if
         - block.prev_hash == last_block.hash
         - block.hash matches difficulty level 
         - block.hash should match the hash constructed from its data
         - difficulty level in last block and this block must have a difference of only 1
         - if block timestamp is less than two hours old
        '''

        if not block or not last_block:
            raise EmptyDataPayloadError()
        
        if block.prev_hash != last_block.hash:
            return False, 'Doesn\'t match previous blocks hash'
        
        if not hex_to_bin.hex_to_bin(block.hash).startswith('0'*block.difficulty):
            return False, 'Difficulty level doesn\'t match'
        
        block_data = block.__dict__.copy()
        del block_data['hash']

        if hash.hash(block_data) != block.hash:
            return False, 'Invalid Hash'
        
        if abs(block.difficulty - last_block.difficulty) >1:
            return False, 'Difference in difficulty is more than 1'
        

        now = time.time_ns()


        if (now - block.timestamp) > ( 2 * HOUR):
            return False, 'Block more than is 2 hours old'
        
        return True, None
    
    @staticmethod
    def make_data(id, timestamp, nonce, difficulty, data, prev_hash):
        return {
            'id': id,
            'timestamp': timestamp,
            'nonce': nonce,
            'difficulty': difficulty,
            'prev_hash': prev_hash,
            'data': data
        }   


def adjust_difficulty(last_block: Block, timestamp):
    '''
    We would need this to adjust the mining speed for the block. we have to make sure that the difficulty is not too hard or too low.
    in case too hard it will take really long and hence in efficient, in case it's too fast there is a chance of conflict in blocks
    '''

    if last_block.difficulty < UPPER_LIMIT_MINE_RATE:
        return last_block.difficulty + 1 
    
    if last_block.difficulty-1 > 0:
        return last_block.difficulty - 1

    return 1

def mine(last_block, data):
    '''
    The function which will work on adding a new block
    '''

    timestamp = time.time_ns()
    id = f'blk_{uuid.uuid1().hex}'
    nonce = 0

    difficulty = adjust_difficulty(last_block, timestamp)

    proof = hash.hash(Block.make_data(id,timestamp, nonce,difficulty, data, last_block.hash))

    while not hex_to_bin.hex_to_bin(proof).startswith('0' * difficulty):
        nonce+=1
        timestamp = time.time_ns()
        difficulty = adjust_difficulty(last_block, timestamp)

        proof = hash.hash(Block.make_data(id,timestamp, nonce,difficulty, data, last_block.hash))
    
    return Block(id, timestamp, nonce, proof, difficulty, last_block.hash, data)