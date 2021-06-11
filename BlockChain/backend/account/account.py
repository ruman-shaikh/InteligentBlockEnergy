import json
import requests

from backend.wallet.wallet import Wallet
from backend.account.meter import Meter
from backend.account.etran import Etran

def AccVerify(userID, passsword):
    res = requests.post('http://localhost:7000/ibe/login', json={'username': userID, 'password': passsword})
    return json.loads(res.text)

class Account:
    """
    An individual user account that connects:
     - wallet 
     - smart meter
     - account details
    """
    def __init__(self, wallet):
        self.wallet = wallet
        self.etranPool = []
        self.etranPoolAck = []

    def getAcc(self, userID, passsword):
        account_details = AccVerify(userID, passsword)
        if account_details['loginState'] == True:
            self.meter = Meter(account_details['meter'])
            self.name = account_details['name']
            self.address = account_details['address']
            self.userID = userID
        else:
            return False

    def requestEnergy(self, energyQuantity):
        energyQuantity = int(energyQuantity)
        if self.wallet.balance < energyQuantity:
            return False
        return Etran(self.userID, energyQuantity)
    
    def __repr__(self):
        return (
            'Account('
            f'name: {self.name}, '
            f'userID: {self.userID}, '
            f'address: {self.address}, '
            f'meter: {self.meter}'
        )

def main():
    wallet = Wallet()
    acc = Account(wallet)
    acc.getAcc('rs112', 'rpass')
    print(acc)
    #etran = acc.requestEnergy(50)
    #print(acc.wallet.balance)
    #print(etran)
    
if __name__ == '__main__':
    main()