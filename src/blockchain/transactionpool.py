from src.blockchain.transaction import Transaction
from src.exceptions import InvalidTransaction
class TransactionPool:
    '''
    This class will hold all the unconfirmed transaction in it and will check for transactions
    '''

    def __init__(self):
        self.transaction_map = {}
    
    def add_transaction(self, tx:Transaction):
        if Transaction.is_transaction_valid(tx.__dict__):
            self.transaction_map[tx.id] = tx
        else:
            raise InvalidTransaction
        

    def find_transaction_of_wallet(self, wallet_id):
        '''
        finds all the transaction for the given sender's wallet id
        '''
        txs = []
        for tx in self.transaction_map.values():
            if tx.input['sender'] == wallet_id:
                txs.append(tx)
        
        return txs

    def transaction_data(self):
        '''
        List of transaction data in json format
        '''
        return list(
            map(
                lambda tx: tx.to_json(), self.transaction_map.values()
            )
        )

    def clear_blockchain_transactions(self, blockchain):
        """
        Delete blockchain recorded transactions from the transaction pool.
        """
        for block in blockchain.chain:
            for transaction in block.data:
                try:
                    del self.transaction_map[transaction['id']]
                except KeyError:
                    pass
    
    @staticmethod
    def from_serialized(json_obj):
        import json
        pool = TransactionPool()
        pool_tx = json.loads(json_obj)

        for tx_json in pool_tx:
            tx = Transaction.from_json(tx_json)
            pool.add_transaction(tx)
        
        return pool
