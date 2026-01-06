import hashlib
import json
import time

class block:
    def __init__(self,a_index,a_timestamp,a_data,a_previous_hash):
        self.index=a_index
        self.timestamp=a_timestamp
        self.data=a_data
        self.previous_hash=a_previous_hash
        self.hash=self.compute_hash()
        self.nonce=0

    def compute_hash(self):
        block_attributes={"index":self.index,"timestamp":self.timestamp,"data":self.data,"previous_hash":self.previous_hash,"nonce":self.nonce}
        block_string=json.dumps(self.block_attributes,sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self,difficulty):
        target="0"*difficulty
        while self.hash[:difficulty]!=target:
            self.nonce+=1
            self.hash=self.compute_hash()
        print(f"Block has been mined with hash: {self.hash}")
    
class blockchain:
    def __init__(self):
        first_block_object=block(0,time.time(),"First block","0")
        self.chain=[]
        self.chain.append(first_block_object)

    def return_last_block(self):
        return self.chain[-1]
    
    def is_valid(self,new_block,previous_block):
        if previous_block.hash!=new_block.previous_hash or new_block.hash!=new_block.compute_hash():
            return False
        return True
    
    def add_block(self,data):
        previous_block=self.return_last_block()
        new_block=block(previous_block.index+1,time.time(),data,previous_block.hash)

        if self.is_valid(new_block,previous_block):
            self.chain.append(new_block)

