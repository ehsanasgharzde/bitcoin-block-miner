import datetime
import hashlib
import json


class Blockchain:
    def __init__(self):
        """
        previous: Previous Block hash
            Info --> 810195558SinaMirzaei
            Info Hex --> 38313031393535353853696e614d69727a616569
            Student Bitcoin Address --> 0x38313031393535353853696e614d69727a616569
        """
        self.previous = "00000000b8dc5f844239cdf2a13a5e4a71b3e767c13004d310a5042696a0517b"
        self.address = "0x38313031393535353853696e614d69727a616569"
        self.proof = 8101
        self.chain = []
        self.create(self.proof, self.previous)

    def create(self, proof: int, previous: str):
        """
        Block Creator Fucntion:
            proof: Proof of Work
            previous: Previous Block Hash
            length: Total Number of Created Blocks
            time: Time of Newly Created Block
            block: Block of Inforamtion
        """
        length = len(self.chain)
        time = str(datetime.datetime.now())

        block = {
            "index": length + 1,
            "timestamp": time,
            "proof": proof,
            "previous": previous,
            "bit-address": self.address
        }
        self.chain.append(block)


    def pow(self, previous: int):
        """
        Proof of Work Function:
            previous: Previous Proof of Work
            isValid: Validation Flag
        """
        proof = 8101
        isValid = False

        while not isValid:
            operation = str((proof ** 2) - (previous ** 2)).encode()
            hashed = hashlib.sha256(operation).hexdigest()

            if hashed[:4] == "0000":
                isValid = True
            else:
                proof += 1
        return proof

    def hashed(self, block):
        """
        Block SHA256 Hash Function:
            encoded: Encoded Block with JSON format
            hashed: SHA256 Hashed Encoded Version of the Block
        """
        encoded = json.dumps(block, sort_keys=True).encode()
        hashed = hashlib.sha256(encoded).hexdigest()

        return hashed
    

    def validation(self, chain: list):
        """
        Chain Validation Function:
            previous: Previous Block
            length: Length of the chain
            index: Block index
            block: Block of Information
        """
        previous = chain[0]
        length = len(chain)
        index = 1

        while length > index:
            block = chain[index]
            if block["previous"] != self.hashed(previous):
                return False

        operation = str((block["proof"] ** 2) - (previous["proof"] ** 2)).encode()
        hashed = hashlib.sha256(operation).hexdigest()

        if hashed[:4] != "0000":
            return False
        
        previous = block
        index += 1

    def document(self):
        docs = """
        Libraries:
        datetime
            Date and Time library
            --> Usage: Timestamps
        hashlib
            Hash Encodings Library
            --> Usage: Encoding
        json
            .JSON library
            --> Usage: Storing Data

        __init__:
        This method will consist of a variable called chain 
        to store a list of all the blocks in the blockchain.

        create:
        This method will allow us to create our 
        Genesis block on instantiation of the class.

        pow:
        In this method, we create a variable to store the proof submitted by miners.
        Next, we create a control statement to check 
        the status of the proof of work, which by default will be False.

        hashed:
        In this method, we generate a hash for the entire block itself.
        We use JSON dumps to encode the block and return a cryptographic hash of the entire block.

        validation:
        A method that checks if the entire blockchain is valid.
        This step is crucial in maintaining the integrity of our 
        blockchain to ensure that none of our blocks is corrupt.
        """
        print(docs)
