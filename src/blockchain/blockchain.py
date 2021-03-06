from typing import List
from src.blockchain.block import Block, mine
from src.blockchain.transaction import Transaction
from src.blockchain.transactionpool import TransactionPool
from src.blockchain.wallet import Wallet
from src.exceptions import ChainValidationError, IncomingChainIsShortError, InvalidBlockError
from src.constants import GENESIS_DATA
class BlockChain:
    '''
    @TODO This class will hold the chain of blocks and will be responsible for list of tasks
        - add genesis block when blockchain is getting created
        - add block after mining it with proper data
        - add a block after recieving it's data and verifying if the block is correct or not
        - replace the current chain ->
            if incoming chain is longer and is valid chain
        - validate chain
            valid if chain[0] is genesis block
            if chain[i] | i>0 has a valid block
            if chain has valid transaction
        - validate transactions of a chain
            if chain[i].data | i > 0 contains valid transactions
            if one transaction appears only once
        - serialize chain
        - create a blockchain from serialized chain
        - a function which will take a function as parameter and will work on the duplicate copy of the chain and return the value produced by the function.

        note: for wrapper we can give user a sql like query language for adding, and mainly selection and processing clauses, which can makes this block chain.
    '''

    def __init__(self):
        self.chain = [Block.genesis()]
        pass

    def add_block_by_mine(self, data):
        self.chain.append(mine(self.chain[-1], data))
    
    def add_block_by_verification(self, json_data):
        blk = Block(**json_data)
        status, msg = Block.validate(self.chain[-1], blk)
        if status:
            self.chain.append(blk)
            return
        
        raise InvalidBlockError()
    
    def replace_chain(self, chain):
        
        if len(chain) <= self.chain_length:
            raise IncomingChainIsShortError()
        
        BlockChain.validate_chain(chain)
        self.chain = chain
    
    def query_on_chain(self, function):
        copy_chain = self.get_chain
        return function(copy_chain)

    @property
    def chain_length(self):
        return len(self.chain)
    
    @property
    def get_chain(self):
        return self.chain.copy()
    

    @staticmethod
    def serialize(chain):
        return list(map(lambda block: Block.to_json(block), chain))
    
    @staticmethod
    def from_serialized(serialized_obj:List[str]):
        block = BlockChain()
        block.chain = list(map(lambda json_block: Block.from_json(json_block)))
        return block
    
    @staticmethod
    def validate_chain(chain):
        '''
        A chain is valid
            if chain[0] is genesis block
            if chain[i] | i>0 has a valid block
            if chain has valid transaction
        '''
        if chain[0].__dict__ != GENESIS_DATA:
            raise ChainValidationError('Genesis block not found')
        
        for index in range(1, len(chain)):
            if not Block.validate(chain[index - 1], chain[index]):
                raise ChainValidationError('Invalid Block Found')
            
        BlockChain.validate_tx(chain)
        pass

    @staticmethod
    def validate_tx(chain):
        '''
            if chain[i].data | i > 0 contains valid transactions
            if one transaction appears only once
            if the amount sent by each sender is valid, i.e if they have that balance
        '''
        tx_ids = set()

        for i in range(len(chain)):
            block = chain[i]

            for tx_json in block.data:
                tx = Transaction.from_json(tx_json)
                if not tx:
                    raise InvalidBlockError(f"transaction {tx_json['id']} is invalid")
                
                if tx.id in tx_ids:
                    raise InvalidBlockError(f"Duplicate transaction found")
                
                tx_ids.add(tx.id)

                sender = tx.input['sender']
                amount = tx.input['amount']

                prev_block_chain = BlockChain()
                prev_block_chain.chain = chain[0:i]

                wallet_balance = Wallet.current_balance(prev_block_chain, sender)

                if amount > wallet_balance:
                    raise InvalidBlockError(f"The amount sent by {sender} in transaction {tx.id} is way above the wallet balance!")

        pass

