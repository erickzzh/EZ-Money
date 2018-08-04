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
        self.difficultyIncrement = 0
        self.hash = self.calculateHash(data, timeStamp, self.difficultyIncrement)


    
    def calculateHash(self, data, timeStamp, difficultyIncrement):
        data = str(data) + str(timeStamp) + str(difficultyIncrement)
        data = data.encode()
        hash = hashlib.sha256(data)
        return hash.hexdigest()

    def mineBlock(self,difficulty):
        difficultyCheck = "0" * difficulty
        while self.hash[:difficulty] != difficultyCheck:
            self.hash = self.calculateHash(self.data,self.timeStamp,self.difficultyIncrement)
            self.difficultyIncrement = self.difficultyIncrement + 1 

       

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
        newBlock.mineBlock(2)
                #this is obv not the best way to append a block but wth
        self.chain.append(newBlock)

    def isChainValid(self):
        for x in range(1,len(self.chain)):
            currentBlock = self.chain[x]
            previousBlock = self.chain[x-1]

            if (currentBlock.previousBlock != previousBlock.hash):
                return False
            
            
        return True


    



ezmoney = Blockchain()
hey =  Block(1,str(datetime.datetime.now()),{"amount":5})
what =  Block(1,str(datetime.datetime.now()),{"amount": 69})
ezmoney.appendBlock(hey)
ezmoney.appendBlock(what)
#this is to convert the blockchain into a json format
testChain = []
for x in ezmoney.chain:
    temp = json.dumps(x.__dict__)
    testChain.append(temp)


pprint.pprint(testChain)
print(ezmoney.isChainValid())
  


#---------------------------------debug methods--------------------------#
#add a block
#what =  Block(1,"1",{"amount": 69})

#print the whole chain in json format
#pprint.pprint(testChain)