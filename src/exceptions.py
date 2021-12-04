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