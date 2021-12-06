import json
from src.blockchain.block import Block, mine

from tests.test_constants import INIT_BLOCK, VALID_TX

def test_block_and_mine():

    init_block = Block(**INIT_BLOCK)
    new_block = mine(init_block, VALID_TX)

    x = new_block == init_block
    assert x == False
    assert new_block.prev_hash == init_block.hash
    assert Block.validate(init_block, new_block)[0]
    assert new_block.data == VALID_TX
    assert json.loads(init_block.to_json()) == INIT_BLOCK