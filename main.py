import hashlib
import datetime
import json
import pprint

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
        difficultyCheck = "9" * difficulty
        while self.hash[:difficulty] != difficultyCheck:
            self.hash = self.calculateHash(self.trans,self.timeStamp,self.difficultyIncrement)
            self.difficultyIncrement = self.difficultyIncrement + 1 

class Blockchain:
    def __init__(self):
        self.chain = [self.GenesisBlock()]
        self.difficulty = 5
        self.pendingTransaction = []
        self.reward = 10
    
    def GenesisBlock(self):
        genesisBlock = Block(str(datetime.datetime.now()),"I am the Gensis Block")
        return genesisBlock

    def getLastBlock(self):
        return self.chain[len(self.chain) - 1]

    def minePendingTrans(self,minerRewardAddress):
        #in reality not all of the pending transaction go into the block the miner gets to pick which one to mine
        newBlock = Block(str(datetime.datetime.now()),self.pendingTransaction)        
        newBlock.mineBlock(self.difficulty)
        newBlock.previousBlock = self.getLastBlock().hash

        print("Previous Block's Hash: " + newBlock.previousBlock)
        testChain = []
        for trans in newBlock.trans:
            temp = json.dumps(trans.__dict__,indent=5, separators=(',', ': '))
            testChain.append(temp)
        pprint.pprint(testChain)

        self.chain.append(newBlock)
        print("Block's Hash: " + newBlock.hash)
        print("Block added")

        rewardTrans = Transaction("System",minerRewardAddress,self.reward)
        self.pendingTransaction.append(rewardTrans)
        self.pendingTransaction = []

    def isChainValid(self):
        for x in range(1,len(self.chain)):
            currentBlock = self.chain[x]
            previousBlock = self.chain[x-1]

            if (currentBlock.previousBlock != previousBlock.hash):
                return ("The Chain is not valid!")
        return ("The Chain is valid and secure")

    def createTrans(self,transaction):
        self.pendingTransaction.append(transaction)

    def getBalance(self,walletAddress):
        balance = 0
        for block in self.chain:
            if block.previousBlock == "" :
                #dont check the first block
                continue 
            for transaction in block.trans:
                if transaction.fromWallet == walletAddress:
                    balance -= transaction.amount
                if transaction.toWallet == walletAddress:
                    balance += transaction.amount
        return balance

class Transaction:
    def __init__(self,fromWallet,toWallet,amount):
        self.fromWallet = fromWallet
        self.toWallet = toWallet
        self.amount = amount



ezmoney = Blockchain()
ezmoney.createTrans(Transaction("Erick","Alex",3.2))
ezmoney.createTrans(Transaction("Erick","Raymond",1))
ezmoney.createTrans(Transaction("Alex","Raymond",5.12))

print("Gloria started minning")

ezmoney.minePendingTrans("Gloria")
ezmoney.createTrans(Transaction("Zining","Alex",0.01))
ezmoney.createTrans(Transaction("Klay","Erick",100))
ezmoney.createTrans(Transaction("Raymond","Erick",0.0000001))

print("Gloria started minning")
ezmoney.minePendingTrans("Gloria")

print("Gloria has " + str(ezmoney.getBalance("Gloria")) + " EZCoins on her account")
print(ezmoney.isChainValid())
