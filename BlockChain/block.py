import time

class Block:
    """
    A unit of storage
    Store transactions in a blockchain that support cryptocurrency
    """
    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return f"Block ( Timestamp: {self.timestamp}, Last Hash: {self.last_hash}, Hash: {self.hash}, Data: {self.data})\n"

    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on the given last block and data
        """
        timesramp = time.time_ns()
        last_hash = last_block.hash
        hash = f"{timesramp} - {last_hash}"

        return Block(timesramp, last_hash, hash, data)

    @staticmethod
    def genesis():
        """
        Generate a genesis block
        """
        return Block(1, "genesis_last_hash", "genesis_hash", [])

def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, "test")
    print(block)

if __name__ == '__main__':
    main()