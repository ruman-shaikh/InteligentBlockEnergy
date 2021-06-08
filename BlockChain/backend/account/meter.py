import requests
import json

class Meter:
    def __init__(self, id):
        self.id = id
        
    @property
    def storage(self):
        con_response = requests.post('http://localhost:7000/gridsim/con', json={'meter': self.id})
        con_data_json = json.loads(con_response.text)

        gen_response = requests.post('http://localhost:7000/gridsim/gen', json={'meter':self.id})
        gen_data_json = json.loads(gen_response.text)
        
        return int(gen_data_json['data']) - int(con_data_json['data'])

    def __repr__(self):
        return (
            'Meter('
            f'meter ID: {self.id}, '
            f'storage: {self.storage}'
        )

def main():
    m1 = Meter('m01')
    print(m1.storage)
    
if __name__ == '__main__':
    main()