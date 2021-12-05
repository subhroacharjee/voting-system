import json
import uuid, time

from src.blockchain.wallet import Wallet
from src.exceptions import EmptyDataPayloadError
class Transaction:
    '''
    The document which holds each transaction associated with voter
    Attributes are
        id: some id of the transaction
        timestamp: nanoseconds of the time it was created
        input: {
            sender: sender waller_id
            reciever: reciever wallet_id
            sender_public_key: senders public key
            signature: signed output
        }
        output: {
            sender: senders wallet_id
            reciever: reciever wallet_id
            amount: no of tokens send (in our case it will be one)
        }
    '''

    def __init__(self, sender, reciever, sender_pub_key, sender_pri_key, amount=1, signature=None, id=None, timestamp = None):
        self.id = id or f'tx_{uuid.uuid1().hex}'
        self.timestamp = timestamp or time.time_ns()
        self.output = self.create_output(reciever, amount)
        self.input = self.create_input(sender, sender_pub_key, sender_pri_key, amount, signature)

    
    def create_input(self, sender, pub_key, pri_key, amount, signature=None):
        return {
            'sender': sender,
            'senders_public_key': pub_key,
            'signature': signature or Wallet.create_signature(pri_key,self.output),
            'amount': amount
        }
    
    def create_output(self, reciever, amount):
        return {
            f'{reciever}':amount,
        }
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def is_transaction_valid(data):
        if not data:
            return False
        
        input_data = data.get('input')
        output_data = data.get('output')
        if not input_data or not output_data:
            return False
        
        if not input_data.get('senders_public_key') or not input_data.get('signature') or not input_data.get('sender') or not input_data.get('amount'):
            return False
        
        return Wallet.verify_signature(input_data.get('senders_public_key'),output_data, input_data.get('signature'))
    
    @staticmethod
    def from_json(data):
        if not data:
            raise EmptyDataPayloadError()
        json_data = json.loads(data)

        try:
            tx = Transaction(
                sender = json_data['input']['sender'], 
                reciever= list(json_data['output'].keys())[0], 
                sender_pub_key= json_data['input']['senders_public_key'], 
                sender_pri_key= None,amount= json_data['input']['amount'], 
                signature= json_data['input']['signature'],
                id= json_data['id'],
                timestamp= json_data['timestamp'])
            if Transaction.is_transaction_valid(tx.__dict__):
                return tx
            return None
        except Exception as e:
            print(e)
            return None
