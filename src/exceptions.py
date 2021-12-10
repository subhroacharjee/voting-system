import json

class ImproperTypeError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)
        self.message = 'The user type is not valid'
    
    def to_json(self):
        return json.dumps(self.__dict__)

class InvalidVoterData(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)
        self.message = 'For voter type no data was provided'
    
    def to_json(self):
        return json.dumps(self.__dict__)

class EmptyDataPayloadError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = 'payload provided to function is empty'
    
    def to_json(self):
        return json.dumps(self.__dict__)

class InvalidTransaction(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)
        self.message = 'Invalid transaction data provided'
    
    def to_json(self):
        return json.dumps(self.__dict__)

class InvalidBlockError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = 'Invalid Block data'
    
    def to_json(self):
        return json.dumps(self.__dict__)

class IncomingChainIsShortError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = 'Incoming chain is shorter than the primary chain'
    
    def to_json(self):
        return json.dumps(self.__dict__)

class ChainValidationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
    def to_json(self):
        return json.dumps(self.__dict__)