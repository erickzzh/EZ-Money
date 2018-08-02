import hashlib
import datetime

class Block:
    def __init__(self,index, timeStamp, data, previousBlock = ''):
        self.index = index
        self.timeStamp = timeStamp
        self.data = data
        self.previousBlock = previousBlock
        self.hash = self.calculateHash(data, timeStamp)

    
    def calculateHash(self, data, timeStamp):
        data = data + str(timeStamp)
        data = data.encode()
        hash = hashlib.sha256(data)
        return hash.hexdigest()
       

class Blockchain:
    def __init__(self):
        self.chain = [self.GenesisBlock()]
    
    def GenesisBlock(self):
        genesisBlock = Block(0,datetime.datetime.now(),"Genesis Block","0")
        return genesisBlock

    def getLastBlock(self):
        '''print(self.chain[len(self.chain) - 1].hash
        debug method
        '''
        return self.chain[len(self.chain) - 1]
    
    def appendBlock(self,newBlock):
        newBlock.previousBlock = self.getLastBlock().hash
        newBlock.hash = newBlock.calculateHash(newBlock.data,newBlock.timeStamp)
        '''this is obv not the best way to append a block but wth'''
        self.chain.append(newBlock)

ezmoney = Blockchain()
hey =  Block(1,"1","1")
what =  Block(1,"1","1")
ezmoney.appendBlock(hey)
ezmoney.appendBlock(what)


  


