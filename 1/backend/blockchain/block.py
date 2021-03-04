import time
from backend.util.crypto_hash import crypto_hash

class Block:
    """
    Implemeted as a unit to store tarnscations to sopport cyptocurrency
    """
    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return (
            '\nBlock ('
            f'timestamp: {self.timestamp}, '
            f'last hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data})'
        )

    @staticmethod
    def mine_block(last_block, data):
        """
        Mines a block
        """
        timestamp = time.time()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp, last_hash, data)

        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def genesis():
        """
        Generate the genesis block
        """
        return Block(1, 'genesis_last_hash', 'genesis_hash', [])

def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, "test")
    print(block)

if __name__ == "__main__":
    main()