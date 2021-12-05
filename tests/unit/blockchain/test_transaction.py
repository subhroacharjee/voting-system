import json
from src.blockchain.transaction import Transaction
from src.blockchain.wallet import Wallet
from src.exceptions import EmptyDataPayloadError
from tests.test_constants import (
    PUBLIC_KEY, PRIVATE_KEY, 
    CANDIDATE_HASH as RECIEVER_ID, VOTER_HASH as SENDER_ID,
    INVALID_TX, VALID_TX
    )


def test_transaction_initalisation():
    tx = Transaction(SENDER_ID,RECIEVER_ID,PUBLIC_KEY,PRIVATE_KEY,100)
    assert tx.input['sender'] == SENDER_ID
    assert tx.input['senders_public_key'] == PUBLIC_KEY
    assert tx.output[RECIEVER_ID] == 100
    assert Wallet.verify_signature(PUBLIC_KEY,tx.output, tx.input['signature'])

def test_transaction_json():
    tx = Transaction(SENDER_ID,RECIEVER_ID,PUBLIC_KEY,PRIVATE_KEY,100).__dict__

    assert tx['input']['sender'] == SENDER_ID
    assert tx['input']['senders_public_key'] == PUBLIC_KEY
    assert tx['input']['amount'] == 100
    assert tx['output'][RECIEVER_ID] == 100
    assert Wallet.verify_signature(PUBLIC_KEY,tx['output'], tx['input']['signature'])
    
def test_is_transaction_valid():
    assert Transaction.is_transaction_valid(None) == False
    assert Transaction.is_transaction_valid({}) == False

    assert Transaction.is_transaction_valid(VALID_TX)
    assert Transaction.is_transaction_valid(INVALID_TX) == False

def test_from_json():
    try:
        Transaction.from_json({})
        assert False
    except EmptyDataPayloadError:
        assert True
    except:
        assert False
    
    json_payload = json.dumps(VALID_TX)

    tx = Transaction.from_json(json_payload)
    assert tx.__dict__ == VALID_TX

    json_payload = json.dumps(INVALID_TX)

    tx = Transaction.from_json(json_payload)

    assert tx == None
    
