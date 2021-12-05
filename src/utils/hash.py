import json
from hashlib import sha256

def hash(data):
    try:
        payload = json.dumps(data).encode('utf-8')
        return sha256(payload).hexdigest()
    except Exception as e:
        print(e)
        return None