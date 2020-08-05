import datetime
import hashlib
import json,requests
from flask import Flask, jsonify
import pymongo

class Blockchain:

    def __init__(self,key,identifier,db,collectionName):
        #details must contain ID Email and Password
        #self.create_block(proof = 1, previous_hash = '0')
        #Request to server to recieve entire jsonify If chain doesn't exist create first block else procceed
        self.collection = db[collectionName]
        query = {key:identifier}
        self.ErrorMessage = ""
        self.chain =[]
        self.validQuery = False
        params = {"Transaction_So_Far":1}
        self.res = self.collection.find_one(query,params)
        if self.res is None:
            self.ErrorMessage = "Invalid Query! Kindly recheck the ID."
        else:
            if len(self.res) == 0:
                self.ErrorMessage = "Invalid Query! Kindly recheck the ID."
            else:
                self.chain = self.res["Transaction_So_Far"]
                self.validQuery = True
                #print(self.chain)
                #print(f"chain type:{type(self.chain)}")

    def create_block(self, proof, previous_hash,water_data):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'Transaction_So_Far':water_data
                 }
        self.chain.append(block)

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

    def mine_block(self,waterdetails):
        if self.is_chain_valid():
            previous_block = self.get_previous_block()
            previous_proof = previous_block['proof']
            proof = self.proof_of_work(previous_proof)
            previous_hash = self.hash(previous_block)
            self.create_block(proof, previous_hash,waterdetails)
            print("Mining a block!")
        else:
            print("Block-chain disrupted. Chain is not valid. Killing Process...")
        #Request MongoDB to serve the block

    def get_chain():
        return(self.chain)


#blockchain = Blockchain()
