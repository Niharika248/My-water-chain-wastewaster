import datetime
import hashlib
import json,requests
from flask import Flask, jsonify

class Blockchain:

    def __init__(self,chain):
        self.chain = chain

    def create_block(self, proof, previous_hash,water_data):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'water_data':water_data
                 }
        self.chain.append(block)
        #print(f"Previous-index: {block['index']} && Previous hash: {block['previous_hash']}")
        #print(f"valid: {self.is_chain_valid()}")
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
        print("\n\n\nBAKCHODI")
        previous_block = self.chain[0]
        block_index = 1
        while block_index < len(self.chain):
            block = self.chain[block_index]
            print(f"current: {block['previous_hash']} for index = {block['index']}")
            print(f"previous hash: {previous_block['previous_hash']} for index = {previous_block['index']}")
            if block['previous_hash'] != self.hash(previous_block):
                print(f"{block['previous_hash']} is not equal to {self.hash(previous_block)}")
                #print("Previous hash of the block isn't equal to the previous hash. Chain disrupted. This is a bad news :-(")
                #print(f"In valididty is caused for the block index: {block_index}")
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                print("This goes wrong")
                return False
            previous_block = block
            block_index += 1
        #print(f"{block['previous_hash']} is equal to {self.hash(previous_block)}")
        return True


    def mine_block(self,waterdetails):
        previous_block = self.get_previous_block()
        #print(f"Previous block is : {previous_block.keys()}")
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)
        #print(f"Previous-index: {previous_block['index']} && Previous hash: {previous_hash}")
        self.create_block(proof, previous_hash,waterdetails)

    def get_chain(self):
        return(self.chain)

    def getJsonInitial(self):
        return(self.chain[-1]["water_data"])




#blockchain = Blockchain()
