import hashlib
import datetime

class block():                                # Craete Block
    def __init__(self,data,id,x):
        self.data=data
        self.id=id
        self.x=x
        self.hash=self.gethash()

    def gethash(self):                        # Proof of Work
        nonce=0;
        while 1:         
            hash=(data+str(nonce))
            hash=hashlib.sha256(hash.encode()).hexdigest()
            if hash[:4]=="".zfill(4):
    	        break
            nonce+=1 
        return hash

    def printblock(self):                     # Print Block
        if(id==0):
            bid="0"
            prevhash="none"
        else:
            bid=self.id 
            lastblock=self.x[-1]
            prevhash=lastblock["hash"]  
        b={"ID":bid,"hash":self.hash,"Data":self.data,"prevhash":prevhash,"Timestamp":datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")}
        self.x.append(b)
        return (self.x)

x=[]
id=0
while(1):
    data=input("Enter The Data : ")           # Input Data
    if(data=="stop"):
        break
    else:
        Block=block(data,id,x)                # Function Call
        cbc=Block.printblock()
        print(cbc)
    id=id+1
print("Final Block chain : ",cbc);    