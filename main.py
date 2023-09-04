from blockchain import Blockchain
from miner import Miner


blockchain = Blockchain()
miner = Miner(blockchain)


if __name__ == '__main__':
    blockchain.document()
    miner.document()

    miner.mine()
    miner.display()