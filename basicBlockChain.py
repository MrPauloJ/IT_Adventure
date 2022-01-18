# Adventure on BlockChain
# Basic BlockChaing idea
# by Paulo Francisco 

# Imports 
from hashlib import sha256
from datetime import date, datetime

class blockChain:
    # construct
    def __init__(self, dificulty=4):
        self.blocks=[]
        self.dificulty=dificulty
        self.genesisBlock()
    
    # Generate genesis block
    def genesisBlock(self):
        data="First block!"
        self.hashBlock(data,datetime.utcnow(),0,0)

    # Generate hash block
    def hashBlock(self,data,time,index,prevHash):
        hashChanger=1 # No need cause date format
        hash=""
        while not self.is_valid_hash(hash):
            block = '{}:{}:{}:{}:{}'.format(data, time, prevHash, index, hashChanger)
            hash=sha256(block.encode()).hexdigest()
            hashChanger+=1
        self.blocks.append(hash)
        print(block)
        print(hash)
        print("")

    # Validation block
    def is_valid_hash(self, hash):
        return hash.startswith(self.dificulty*"0")
    
    # Get last hash block
    def getLastHash(self):
        return self.blocks[-1]

    # Generate a new block
    def newBlock(self,data):
        self.hashBlock(data,datetime.utcnow(),len(self.blocks),self.getLastHash())

chain = blockChain(dificulty=2)
chain.newBlock("hahaha")
