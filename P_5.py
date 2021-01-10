import hashlib
import datetime

class Block:
    def __init__(self,timestamp,data,previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
    
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()   
        
    def __repr__(self):
        return 'Timestamp: ' + str(self.timestamp) + str(" | ") + 'Data: '+ str(self.data) + str(" | ") + 'SHA256 Hash: '+ str(self.hash) + str(" | ")  + 'Prev_Hash: ' + str(self.previous_hash)

class BlockChain(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def appendBlock(self,data):
        if data is None or data == "":
            return
        elif self.head is None:
            self.head = Block(datetime.datetime.utcnow(),data,0)
            self.tail = self.head
        else:
            self.tail.next = Block(datetime.datetime.utcnow(),data,self.tail.hash)
            self.tail = self.tail.next

    def to_list(self):
        out = []
        block = self.head
        while block:
            out.append([block]) 
            block = block.next
        return out

def main():
    # Test case 1
    bl = BlockChain()

    data1= "First BlockChain Block"
    data2= "Second Blockchain Block"
    data3= "Third Blockchain Block"

    bl.appendBlock(data1)
    bl.appendBlock(data2)
    bl.appendBlock(data3)

    print(bl.to_list()) # prints block chain

    # Testcase 2
    bl1 = BlockChain()

    bl1.appendBlock("")
    bl1.appendBlock("")

    print(bl1.to_list())

    # Test case 3
    bl2 = BlockChain()

    bl2.appendBlock(None)
    bl2.appendBlock(None)

    print(bl2.to_list())

if __name__ == "__main__":
    main()

