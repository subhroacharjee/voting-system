# Voting system
Just an implementation of a voting system using Blockchain.

## Features list
 - [ ] Blockchain
 - [x] Wallets
 - [ ] P2p system
 - [ ] EC council password and candidate adder

### Blockchain
The base principle behind the project is to learn and make a blockchain application from scratch, so <b>Blockchain</b> was the obious feature.

### Wallets
This will allow the party to recieve votes and voters to give vote. The vote will be the token which will be exchanged from voters wallet to parties wallet, ironical.

### P2P system
This system will allow to the application to spread over bunch of peers and send recieve bunch of instruction/data making the whole system a peer to peer network. The code will be challenging so looking forward to it.

### EC council password and candidate adder
Only the Election commisionare will be able to make wallets for parties, that will be maintained, well it will be a hybrid system with centralised party formation and decentralized voting.

## How to install

Make an virtual environment and source the virtual env
```bash
$ virtualenv venv
$ source venv/bin/activate
```

Install dependencies
```bash
$ pip install -r requirements.txt
```

Run the tests
```bash
$ pytest
```

## References
 - [15Dkatz/python-blockchain-tutorial](https://github.com/15Dkatz/python-blockchain-tutorial)
 - [How To Build A Blockchain In Python ](https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/)
 - [Cryptography](https://cryptography.io/en/latest/)
 - [Simply Explained](https://www.youtube.com/watch?v=GSTiKjnBaes&list=PLzvRQMJ9HDiSM_uLyxy5B6ml_BpmLFAHU)
