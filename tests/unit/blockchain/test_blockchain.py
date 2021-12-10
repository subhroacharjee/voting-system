'''
List of checks are
 - If a new block chain is created, we need to check if the 0th block is the genesis block or not
 - We need a list of mock transaction data to check if the mining is working or not
 - We need a serialized block to check if add_block_by verification is working or not
 - We need some function with predifined return value to check if the query is working or not
 - we need to run validate_chain on some invalid chain to check if the validation is working or not
'''

from src.blockchain.blockchain import BlockChain
from src.constants import GENESIS_DATA


def test_genesis_block():
    new_block_chain = BlockChain()
    assert new_block_chain.get_chain[0].__dict__ == GENESIS_DATA

def test_mining_in_block_chain(create_a_mock_block_chain, create_some_mock_transaction):
    for data in create_some_mock_transaction:
        create_a_mock_block_chain.add_block_by_mine([data])
    assert create_a_mock_block_chain.chain_length == 11
    assert BlockChain.validate_chain(create_a_mock_block_chain.get_chain) == None

