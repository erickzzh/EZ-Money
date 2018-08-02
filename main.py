import hashlib
import datetime
import json
import pprint as pprint

class Block:
    def __init__(self,index, timeStamp, data, previousBlock = ''):
        self.index = index
        self.timeStamp = timeStamp
        self.data = data
        self.previousBlock = previousBlock
        self.hash = self.calculateHash(data, timeStamp)

    
    def calculateHash(self, data, timeStamp):
        data = str(data) + str(timeStamp)
        data = data.encode()
        hash = hashlib.sha256(data)
        return hash.hexdigest()
       

class Blockchain:
    def __init__(self):
        self.chain = [self.GenesisBlock()]
    
    def GenesisBlock(self):
        genesisBlock = Block(0,str(datetime.datetime.now()),"Genesis Block","0")
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

    def isChainValid(self):
        for x in range(1,len(self.chain)):
            currentBlock = self.chain[x]
            previousBlock = self.chain[x-1]

            if (currentBlock.previousBlock != previousBlock.hash):
                return False
            
            if (currentBlock.hash != currentBlock.calculateHash(currentBlock.data,currentBlock.timeStamp)):
                return False
            
        return True


    



ezmoney = Blockchain()
hey =  Block(1,"1",{"amount":5})
what =  Block(1,"1",{"amount": 69})
ezmoney.appendBlock(hey)
ezmoney.appendBlock(what)
"""this is to convert the blockchain into a json format"""
testChain = []
for x in ezmoney.chain:
    temp = json.dumps(x.__dict__)
    testChain.append(temp)


pprint.pprint(testChain)
print(ezmoney.isChainValid())
  


