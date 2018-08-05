import hashlib
import datetime
import json
import pprint as pprint

class Transaction:
    def __init__(self,fromWallet,toWallet,amount):
        self.fromWallet = fromWallet
        self.toWallet = toWallet
        self.amount = amount

class Block:
    def __init__(self, timeStamp, trans, previousBlock = ''):
        self.timeStamp = timeStamp
        self.trans = trans
        self.previousBlock = previousBlock
        self.difficultyIncrement = 0
        self.hash = self.calculateHash(trans, timeStamp, self.difficultyIncrement)



    
    def calculateHash(self, data, timeStamp, difficultyIncrement):
        data = str(data) + str(timeStamp) + str(difficultyIncrement)
        data = data.encode()
        hash = hashlib.sha256(data)
        return hash.hexdigest()

    def mineBlock(self,difficulty):
        difficultyCheck = "0" * difficulty
        while self.hash[:difficulty] != difficultyCheck:
            self.hash = self.calculateHash(self.trans,self.timeStamp,self.difficultyIncrement)
            self.difficultyIncrement = self.difficultyIncrement + 1 

       

class Blockchain:
    def __init__(self):
        self.chain = [self.GenesisBlock()]
        self.difficulty = 1
        self.pendingTransaction = []
        self.reward = 10
    
    def GenesisBlock(self):
        genesisBlock = Block(str(datetime.datetime.now()),Transaction(str(datetime.datetime.now()),"System","Genesis Block"))
        return genesisBlock

    def getLastBlock(self):
        '''print(self.chain[len(self.chain) - 1].hash
        debug method
        '''
        return self.chain[len(self.chain) - 1]
    
    def minePendingTrans(self,minerRewardAddress):
        #in reality not all of the pending transaction go into the block the miner gets to pick which one to mine
        newBlock = Block(str(datetime.datetime.now()),self.pendingTransaction)        
        newBlock.mineBlock(self.difficulty)
        newBlock.previousBlock = self.getLastBlock().hash

        print("Block Created")
        self.chain.append(newBlock)
        print("Block added")

        rewardTrans = Transaction("System",minerRewardAddress,self.reward)
        self.pendingTransaction.append(rewardTrans)
        self.pendingTransaction = []



    def createTrans(self,transaction):
        self.pendingTransaction.append(transaction)

    def getBalance(self,walletAddress):
        balance = 0
        for block in self.chain:
            print(block.previousBlock)

            if block.previousBlock == "" :
                #dont check the first block
                continue 
            for transaction in block.trans:
                if transaction.fromWallet == walletAddress:
                    balance -= transaction.amount
                if transaction.toWallet == walletAddress:
                    balance += transaction.amount
                    
        return balance





    def isChainValid(self):
        for x in range(1,len(self.chain)):
            currentBlock = self.chain[x]
            previousBlock = self.chain[x-1]

            if (currentBlock.previousBlock != previousBlock.hash):
                return False
            
            
        return True


ezmoney = Blockchain()
ezmoney.createTrans(Transaction("from1","to2",100))
ezmoney.createTrans(Transaction("from3","to2",100))
ezmoney.createTrans(Transaction("from4","to2",100))

print("Gloria started minning")

ezmoney.minePendingTrans("gloria")
ezmoney.createTrans(Transaction("from1","to2",100))
ezmoney.createTrans(Transaction("from3","to2",100))
ezmoney.createTrans(Transaction("from4","to2",100))

ezmoney.minePendingTrans("gloria")

print(ezmoney.chain[1].trans)
print(ezmoney.isChainValid())
print(ezmoney.getBalance("gloria"))




  


#---------------------------------debug methods--------------------------#
#add a block
#what =  Block(1,"1",{"amount": 69})

#print the whole chain in json format
#pprint.pprint(testChain)



#test 
'''hey =  Block(1,str(datetime.datetime.now()),{"amount":5})
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



    def appendBlock(self,newBlock):
        newBlock.previousBlock = self.getLastBlock().hash
        #set the difficulity by passing a number as a param
        newBlock.mineBlock(self.difficulty)
                #this is obv not the best way to append a block but wth
        self.chain.append(newBlock)
'''