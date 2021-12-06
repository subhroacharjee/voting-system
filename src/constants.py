TYPES_OF_USER = {
    'VOTER': 0x01,
    'CANDIDATE': 0x02
}

INITIAL_BALANCE = 1

GENESIS_DATA = {
    'id': 1,
    'timestamp': 1,
    'last_hash': 'lsthash',
    'data': [],
    'hash': '439e5cc4d0266de151b02bc1f9cce04292e1ce2f42632c86d24d8bd88f55594e',
    'difficulty': 3,
    'nonce': 0
}

HEX_TO_BIN = {
    '0': '0000', 
    '1': '0001', 
    '2': '0010', 
    '3': '0011', 
    '4': '0100', 
    '5': '0101', 
    '6': '0110', 
    '7': '0111', 
    '8': '1000', 
    '9': '1001', 
    'a': '1010', 
    'b': '1011', 
    'c': '1100', 
    'd': '1101', 
    'e': '1110', 
    'f': '1111'
}

SECONDS = 1000000000
MINUTE = 60 * SECONDS
HOUR = 60 * MINUTE


UPPER_LIMIT_MINE_RATE = 10
LOWER_LIMIT_MINE_RATE = 4