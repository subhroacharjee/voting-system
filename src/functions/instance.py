import os, pathlib, json
from src.exceptions import NoConfigFileError
from src.blockchain import blockchain, transactionpool
class Instance:
    '''
    Will run the instance of the blockchain and tx_pool.
    This will interact with wrapper with event pipes.
    This will do background tasks such as backups and chain validations
    '''

    ready = False

    def __init__(self, pipe):
        self.pipe = pipe
        self.search_for_chain_files()

        if not self.blockchain: 
            self.create_setup_files()
        
        self.ready = True

        self.run_event_listener()
        self.run_autobackup()
    
    def search_for_chain_files(self):
        '''
        Searches for chain files in the wild and if present add them to block and tx_pool.
        Files which are searched and parsed are,
         - config.ini for the path to where the app folder is stored
         - goto the folder (if not exists make it)
         - check if folder has our required files
         - if files present parse them and add them to our instance of the blockchain
         - else make blockchain and tx_pool as None
        '''
        import configparser
        configr = configparser.ConfigParser()

        path_to_config_ini = os.path.join(pathlib.Path.cwd(), 'config.ini')
        if not os.path.exists(path_to_config_ini):
            raise NoConfigFileError()
        configr.read(path_to_config_ini)
        self.path_to_chain = configr.get('Instance','PATH_TO_CHAIN')
        self.path_to_pool = configr.get('Instance', 'PATH_TO_TX_POOL')
        if not (os.path.exists(self.path_to_chain) and os.path.exists(self.path_to_pool)):
            self.blockchain = None
            self.pool = None
            return
        
        with open(self.path_to_chain, 'r') as chain:
            blockchain_json = chain.read()
        
        self.blockchain = blockchain.BlockChain.from_serialized(blockchain_json)
        
        with open(self.path_to_pool, 'r') as pool:
            pool_json = chain.read()
        
        self.pool = transactionpool.TransactionPool.from_serialized(pool_json)

    def create_setup_file(self):
        '''
        In case pool or chain.json is not present we will be creating the json to the given file.
        '''
        self.blockchain = blockchain.BlockChain()
        self.pool = transactionpool.TransactionPool()

        with open(self.path_to_chain, 'w') as chain:
            json.dump(blockchain.BlockChain.serialize(self.blockchain.get_chain),chain)
        
        with open(self.path_to_pool, 'w') as pool:
            json.dump(self.pool.transaction_data(),pool)
    
    def run_event_listener(self):
        '''
        It will create a background running thread that will listen for any events send with the pipe, and will perform the 
        appropiate job according to the event. The threading function will just be an indexer function.
        This function should (if possible) needs to create a good exception handler for the threads so that no memory is leaked.
        The thread created will be will be attached to daemon thread. We might need to create a class for the thread which will give us better 
        handling ablities.
        '''
        pass

    def run_autobackup(self):
        '''
        Like the name suggest it will run a background process using thread and this class instance which will be using blockchain and pool and will be
        storing it in the predestined path whenever there is some change in any both.
        '''
        pass
    
    


