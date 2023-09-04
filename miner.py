import json


class Miner:
    def __init__(self, blockchain: object):
        self.blockchain = blockchain
        
    def mine(self):
        block = self.blockchain.chain[-1]
        proof = self.blockchain.pow(block["proof"])
        hash = self.blockchain.hashed(block)
        mined = self.blockchain.create(proof, hash)

        results = json.dumps({
            "message": "200, Block Mined.",
            "index": block["index"],
            "timestamp": block["timestamp"],
            "proof": block["proof"],
            "previous": block["previous"]
        })
        print(results)


    def display(self):
        results = json.dumps({
            "chain": self.blockchain.chain,
            "length": len(self.blockchain.chain)
        })
        print(results)

    def document(self):
        docs = """
        Libraries:
        json
            .JSON library
            --> Usage: Storing Data

        mine:
        we fetch the data we need to create a block.

        display:
        return a response that contains the blockchain's 
        length and the blockchain within the chain.
        """
        print(docs)
