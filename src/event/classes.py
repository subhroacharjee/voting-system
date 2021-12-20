class Event:
    '''
    This class is the class which we will use for propagating any event across this system.
    '''

    def __init__(self, src_id, event_type, event_body, dest_id):
        self.src_id = src_id
        self.event_type = event_type
        self.event_body = event_body
        self.dest_id = dest_id

        import json
        return json.dumps(self.__dict__)
    
