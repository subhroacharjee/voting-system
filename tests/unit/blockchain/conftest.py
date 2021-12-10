import pytest
import random

from src.blockchain.blockchain import BlockChain
from src.blockchain.transactionpool import TransactionPool
from src.blockchain.transaction import Transaction
from src.blockchain import wallet
from tests import test_constants as Constants
from src.constants import INITIAL_BALANCE

@pytest.fixture
def create_a_mock_block_chain():
    yield BlockChain()

@pytest.fixture
def create_some_mock_transaction(mocker):
    mocker.patch.object(wallet,'INITIAL_BALANCE' , 1000)
    wallet_id_1 = Constants.CANDIDATE_HASH
    wallet_id_2 = Constants.VOTER_HASH

    pool = TransactionPool()

    for i in range(10):
        x = random.choice([wallet_id_1, wallet_id_2])
        y = wallet_id_1 if x == wallet_id_2 else wallet_id_2

        amount = random.randint(10, 50)
        pool.add_transaction(Transaction(
            sender= x,
            reciever= y,
            sender_pub_key = Constants.PUBLIC_KEY,
            sender_pri_key = Constants.PRIVATE_KEY,
            amount=amount
        ))
    yield pool.transaction_data()
    

