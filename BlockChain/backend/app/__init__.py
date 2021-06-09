import os
import requests
import random

from flask import Flask, jsonify, request
from flask_cors import CORS

from backend.blockchain.blockchain import Blockchain
from backend.wallet.wallet import Wallet
from backend.account.account import Account
from backend.account.etran import Etran
from backend.wallet.transaction import Transaction
from backend.wallet.transaction_pool import TransactionPool
from backend.pubsub import PubSub

app = Flask(__name__)
CORS(app, resources={ r'/*': { 'origins': 'http://localhost:3000' } })
blockchain = Blockchain()
wallet = Wallet(blockchain)
account = Account(wallet)
transaction_pool = TransactionPool()
pubsub = PubSub(blockchain, transaction_pool, account)

@app.route('/')
def route_default():
    return 'Welcome to the blockchain'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/range')
def route_blockchain_range():
    # http://localhost:5000/blockchain/range?start=2&end=5
    start = int(request.args.get('start'))
    end = int(request.args.get('end'))

    return jsonify(blockchain.to_json()[::-1][start:end])

@app.route('/blockchain/length')
def route_blockchain_length():
    return jsonify(len(blockchain.chain))

@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = transaction_pool.transaction_data()
    transaction_data.append(Transaction.reward_transaction(wallet).to_json())
    blockchain.add_block(transaction_data)
    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)
    transaction_pool.clear_blockchain_transactions(blockchain)

    return jsonify(block.to_json())

@app.route('/wallet/transact', methods=['POST'])
def route_wallet_transact():
    transaction_data = request.get_json()
    transaction = transaction_pool.existing_transaction(wallet.address)

    if transaction:
        transaction.update(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
        )
    else:
        transaction = Transaction(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
        )

    pubsub.broadcast_transaction(transaction)

    return jsonify(transaction.to_json())

@app.route('/wallet/info')
def route_wallet_info():
    return jsonify({ 'address': wallet.address, 'balance': wallet.balance })

@app.route('/account/login', methods=['POST'])
def route_account_login():
    credentials = request.get_json()
    print("before checking for {credentials}")
    if account.getAcc(credentials['username'], credentials['password']) == False:
        return jsonify({'status': False, 'text':'invalid username/password'})
    return jsonify({'status': True, 'text':'success'})

@app.route('/account/info')
def route_account_info():
    data = {
        'name': account.name,
        'userid': account.userID,
        'address': account.address,
        'meterid': account.meter.id,
        'storage': account.meter.storage
    }
    return jsonify(data)

@app.route('/account/request', methods=['POST'])
def route_account_energy_request():
    request_data = request.get_json()
    etran = account.requestEnergy(request_data['quantity'])
    if etran == False:
        return jsonify({'status': False})
    print("Broadcast energy")
    pubsub.broadcast_energy(etran)
    print("waiting")
    while(not account.etranPoolAck):
        pass
    etran_ack = account.etranPoolAck[-1]
    print('last etran found')
    while etran.etuid != etran_ack.etuid and etran_ack.status != 0:
        etran_ack = account.etranPoolAck[-1]
    print(f'make transaction for {etran_ack.acceptorAddress}')
    transact_url = 'http://localhost:' + str(PORT) + '/wallet/transact'
    print(PORT)
    requests.post(transact_url, json={ 'recipient': etran_ack.acceptorAddress, 'amount': etran.quantity })
    mine_url = 'http://localhost:' + str(PORT) + '/blockchain/mine'
    requests.get(mine_url)
    print('made transaction')
    etran.status = 1
    pubsub.broadcast_energy(etran)
    etran_ack.status = 1
    pubsub.broadcast_energy_tran(etran_ack)

    return jsonify({'status': True})

@app.route('/account/esell', methods=['POST'])
def route_account_energy_sell():
    etuid = request.get_json()['etuid']
    for i in account.etranPool:
        if i.etuid == etuid:
            print(f"etran {i.etuid} found")
            etran = i
            etran.acceptRequest(account.wallet.address)
            print(etran.acceptorAddress)
            etran.status = 0
            print('pre-broadcast ertan ack')
            pubsub.broadcast_energy_tran(etran)
            print('post-broadcast ertan ack')
            return jsonify({'status': True})

    return jsonify({'status': False})

@app.route('/account/etran')
def route_account_etran():
    if (not account.etranPool):
        return jsonify({'status': False})
    data = []
    for i in account.etranPool:
        if i.status == -1:
            data.append(i.to_json())
    if (len(data) == 0):
        return jsonify({'status': False})
    return jsonify({'status': True, 'etran': data})

@app.route('/account/tranpool')
def route_account_tranpool():
    return jsonify(list(account.etranPool))

@app.route('/account/tranpoolack')
def route_account_tranpoolack():
    return jsonify(list(account.etranPool))

@app.route('/known-addresses')
def route_known_addresses():
    known_addresses = set()

    for block in blockchain.chain:
        for transaction in block.data:
            known_addresses.update(transaction['output'].keys())

    return jsonify(list(known_addresses))

@app.route('/transactions')
def route_transactions():
    return jsonify(transaction_pool.transaction_data())

ROOT_PORT = 5000
PORT = ROOT_PORT

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)
    
    result = requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
    result_blockchain = Blockchain.from_json(result.json())

    try:
        blockchain.replace_chain(result_blockchain.chain)
        print('\n -- Successfully synchronized the local chain')
    except Exception as e:
        print(f'\n -- Error synchronizing: {e}')

if os.environ.get('SEED_DATA') == 'True':
    for i in range(10):
        blockchain.add_block([
            Transaction(Wallet(), Wallet().address, random.randint(2, 50)).to_json(),
            Transaction(Wallet(), Wallet().address, random.randint(2, 50)).to_json()
        ])

    for i in range(3):
        transaction_pool.set_transaction(
            Transaction(Wallet(), Wallet().address, random.randint(2, 50))
        )

app.run(port=PORT)
