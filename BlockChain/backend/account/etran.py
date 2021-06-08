import uuid
import json

from collections import OrderedDict

class Etran:
    def __init__(self, initiator, quantity, etuid=None, status=None, acceptorAddress=None):
        self.initiator = initiator
        self.quantity = quantity
        self.etuid = etuid or str(uuid.uuid4())[0:8]
        self.status = status or -1
        self.acceptorAddress = acceptorAddress or ""

    def __repr__(self):
        return f'Initiator: {self.initiator} Quantity {self.quantity} UID {self.etuid} Status {self.status}'

    def acceptRequest(self, acceptorAddress):
        if self.status == -1:
            self.acceptorAddress = acceptorAddress

    def to_json(self):
        """
        Serialize the etran.
        """
        data = json.loads(json.dumps((OrderedDict(sorted(self.__dict__.items())))))
        return data
    
    @staticmethod
    def from_json(etran_json):
        """
        Deserialize a etran's json representation back into a
        Etran instance
        """
        return Etran(**etran_json)

def main():
    etran = Etran('rs112', 50)
    print(etran)
    etran_json = etran.to_json()
    print(etran_json)
    etran_back = Etran.from_json(etran_json)
    print(etran_back)
    
if __name__ == '__main__':
    main()