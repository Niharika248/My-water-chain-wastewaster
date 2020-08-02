import datetime
import hashlib
import json,requests
from flask import Flask, jsonify

class Blockchain:

    def __init__(self,details,endpointUrl):
        #details must contain ID Email and Password
        #self.create_block(proof = 1, previous_hash = '0')
        #Request to server to recieve entire jsonify If chain doesn't exist create first block else procceed
        res = requests.post(endpointUrl, json = details)
        self.res = res.json()
        if self.res["Is_Valid"]!=True:
            print(f"Error in connecting:{res.json()['Error_Message']}")
            self.chain = []
        else:
            self.chain = self.res["Block_Chain"]

    def create_block(self, proof, previous_hash,water_data):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'water_data':water_data
                 }
        self.chain.append(block)
        return block
    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        previous_block = self.chain[0]
        block_index = 1
        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    def serverPushRequest(self,credentials,endpointUrl):
        if self.is_chain_valid():
            self.res["Block_Chain"] = self.chain
            self.res["email"] = credentials["email"]
            self.res["password"] = credentials["password"]
            #print(self.res["Block_Chain"])
            res = requests.post(endpointUrl, json = self.res)
            #print("Update success!")
            return(res.json())
        else:
            print("Invalid-Chain Request")


    def mine_block(self,waterdetails):
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)
        self.create_block(proof, previous_hash,waterdetails)
    def get_chain():
        return(self.chain)


#blockchain = Blockchain()
