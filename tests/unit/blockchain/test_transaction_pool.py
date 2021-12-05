import random
import json
import string
from src.blockchain.transactionpool import TransactionPool
from src.blockchain.transaction import Transaction

from tests.test_constants import (
    VOTER_HASH as SENDER, 
    CANDIDATE_HASH as RECIEVER, 
    PUBLIC_KEY, PRIVATE_KEY)

def test_transaction_pool():
    pool = TransactionPool()
    no_of_iter = random.randint(1,16)
    tx_ar = []

    counter = {
        SENDER: 0,
        RECIEVER: 0
    }
    for i in range(no_of_iter):
        x = random.choice((SENDER, RECIEVER))
        y = SENDER if x == RECIEVER else RECIEVER

        counter[x]+=1
        tx = Transaction(x, y, PUBLIC_KEY, PRIVATE_KEY, random.random()*100)
        tx_ar.append(tx)
        pool.add_transaction(tx)
    

    for index, tx in enumerate(tx_ar):
        assert tx.id in pool.transaction_map
        assert tx.input == pool.transaction_map[tx.id].input
        assert tx.output == pool.transaction_map[tx.id].output
    
    wallets_tx = pool.find_transaction_of_wallet(SENDER)
    assert len(wallets_tx) == counter[SENDER]

    wallets_tx = pool.find_transaction_of_wallet(RECIEVER)
    assert len(wallets_tx) == counter[RECIEVER]

    list_of_transaction_data = pool.transaction_data()

    assert len(list_of_transaction_data) == len(tx_ar)

    for json_tx in list_of_transaction_data:
        assert Transaction.from_json(json_tx) != None

