import random
import string

from tests.test_constants import VOTER_DATA, VOTER_HASH, CANDIDATE_DATA, CANDIDATE_HASH, DICT_DATA
from src.constants import INITIAL_BALANCE
from src.exceptions import ImproperTypeError
from src.blockchain.wallet import Wallet

def test_wallet_for_voter():
    wallet = Wallet('VOTER', VOTER_DATA)
    assert wallet.wallet_id == VOTER_HASH
    assert wallet.balance == INITIAL_BALANCE

def test_wallet_for_candidate():
    wallet = Wallet('CANDIDATE', CANDIDATE_DATA)
    assert wallet.wallet_id == CANDIDATE_HASH
    assert wallet.balance == INITIAL_BALANCE

def test_wallet_incorrect_type():
    try:
        rand_str = ''.join((random.choice(string.ascii_uppercase) for x in range(random.randint(5,100))))
        while rand_str == 'CANDIDATE' or rand_str == 'VOTER':
            rand_str = ''.join((random.choice(string.ascii_uppercase) for x in range(random.randint(5,100))))

        wallet = Wallet(rand_str, DICT_DATA)
        assert False
    except ImproperTypeError:
        assert True
    except:
        assert False

