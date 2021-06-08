import time
from flask import Flask, request

from GridSim import dataStreamCon, dataStreamGen, meter_mapping
from DBUtils import AccVerify

app = Flask(__name__)

@app.route('/')
def route_welcome():
    return 'Welcome to the IBE homepage'

@app.route('/gridsim/con', methods=['POST'])
def route_gridsim_con():
    req_data = request.get_json()
    temp, _ = meter_mapping(req_data['meter'])
    T = int(time.strftime("%H", time.localtime()))
    return {"data": dataStreamCon(int(temp), T)}

@app.route('/gridsim/gen', methods=['POST'])
def route_gridsim_gen():
    req_data = request.get_json()
    _, weather = meter_mapping(req_data['meter'])
    T = int(time.strftime("%H", time.localtime()))
    return {"data": dataStreamGen(str(weather), T)}

@app.route('/ibe/login', methods=['POST'])
def route_login():
    req_data = request.get_json()
    userID, password = req_data['username'], req_data['password']
    rdata = AccVerify(userID, password)
    print(rdata)
    return rdata

if __name__ == '__main__':
    app.run(host='localhost', port=7000)