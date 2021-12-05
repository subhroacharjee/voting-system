from src.blockchain.transaction import Transaction
class TransactionPool:
    '''
    This class will hold all the unconfirmed transaction in it and will check for transactions
    '''

    def __init__(self):
        self.transaction_map = {}
    
    def add_transaction(self, tx:Transaction):
        self.transaction_map[tx.id] = tx

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