from backend.blockchain.block import Block

class Blockchain:
    """
    Blockchain implemented as a class
    chain is implemented as list of blocks
    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1] ,data))

    def __repr__(self):
        return f"Blockchain {self.chain}"

def main():
    blockchain = Blockchain()
    blockchain.add_block("one")
    blockchain.add_block("two")
    print(blockchain)

if __name__ == "__main__":
    main()