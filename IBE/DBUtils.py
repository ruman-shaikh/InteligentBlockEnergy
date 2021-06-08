import json

def AccVerify(userID, passsword):
    f = open('user_data.json',)
    data = json.load(f)

    output = {
        'loginState': False
    }

    for i in data['user']:
        if(i['userID'] == userID):
            if(i['password'] == passsword):
                output['loginState'] = True
                output['name'] = i['name']
                output['address'] = i['address']
                output['meter'] = i['meter']
                output['userID'] = i['userID']
                return output
            output['errorDescription'] = 'incorrect passowrd'
            return output

    f.close()
    output['errorDescription'] = 'incorrect userID'
    return output