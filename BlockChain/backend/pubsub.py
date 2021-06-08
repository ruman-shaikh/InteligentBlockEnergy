import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from backend.blockchain.block import Block
from backend.wallet.transaction import Transaction
from backend.account.account import Account
from backend.account.etran import Etran

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-ea6d15cc-9c1e-11eb-9adf-f2e9c1644994'
pnconfig.publish_key = 'pub-c-4eb9c06d-af7e-4051-9498-081f91956328'

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK',
    'TRANSACTION': 'TRANSACTION',
    'ENERGY': 'ENERGY',
    'ETRANACK': 'ETRANACK'
}

class Listener(SubscribeCallback):
    def __init__(self, blockchain, transaction_pool, account):
        self.blockchain = blockchain
        self.transaction_pool = transaction_pool
        self.account = account

    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                self.transaction_pool.clear_blockchain_transactions(
                    self.blockchain
                )
                print('\n -- Successfully replaced the local chain')
            except Exception as e:
                print(f'\n -- Did not replace chain: {e}')

        elif message_object.channel == CHANNELS['TRANSACTION']:
            transaction = Transaction.from_json(message_object.message)
            self.transaction_pool.set_transaction(transaction)
            print('\n -- Set the new transaction in the transaction pool')

        elif message_object.channel == CHANNELS['ENERGY']:
            print("recived etran")
            etran = Etran.from_json(message_object.message)
            self.account.etranPool.append(etran)
        
        elif message_object.channel == CHANNELS['ETRANACK']:
            print("recived etran ack")
            etran = Etran.from_json(message_object.message)
            self.account.etranPoolAck.append(etran)

class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self, blockchain, transaction_pool, account):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain, transaction_pool, account))

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())

    def broadcast_transaction(self, transaction):
        """
        Broadcast a transaction to all nodes.
        """
        self.publish(CHANNELS['TRANSACTION'], transaction.to_json())

    def broadcast_energy(self, etran):
        """
        Broadcast a energy request to all nodes.
        """
        print("broadcast etran")
        self.publish(CHANNELS['ENERGY'], etran.to_json())

    def broadcast_energy_tran(self, etran):
        """
        Broadcast a energy request to all nodes.
        """
        print("broadcast etran ack")
        self.publish(CHANNELS['ETRANACK'], etran.to_json())

def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'], { 'foo': 'bar' })

if __name__ == '__main__':
    main()
