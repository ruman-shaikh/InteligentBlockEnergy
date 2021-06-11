import random
import decimal
import json

def dataStreamGen(sky,time):
    """
    Function that simulates the energy generation of an avarage household 
    with a full roof solar panel
    """
    val = 0
    if(sky=="Sunny"):
        if(time in range(7,11)):
            val=random.uniform(2.6,3.0)
            print(round(val,2))
        elif(time in range(11,15)):
            val=random.uniform(2.9,3.3)
            print(round(val,2))
        elif(time in range(15,18)):
            val=random.uniform(2.1,2.5)
            print(round(val,2))
    elif sky=="Cloudy" or sky=="Scattered clouds":
        if(time in range(7,11)):
            val=random.uniform(2.3,2.6)
            print(round(val,2))
        elif(time in range(11,15)):
            val=random.uniform(2.6,3.0)
            print(round(val,2))
        elif(time in range(15,18)):
            val=random.uniform(1.8,2.2)
            print(round(val,2))
    elif sky=="Rainy" or sky=="Light Rain" or sky=="Heavy Rain" :
        val=0.0
        print(val)
    elif time<7 or time>18:
        print("Sunlight is unavailable during this time")
    else:
        print("Defined weather is invalid")
    return val*1000

def dataStreamCon(temp,time):
    """
    Function that simulates the energy consumption an avarage household
    """
    unit = 0
    if(temp in range(14,22)):
        if(time in range(0,5)):
            t="Cold"
            unit=float(decimal.Decimal(random.randrange(7,12))/10)
            print(t)
            print(unit)  
        elif(time in range(5,11)):
            t="Mild"
            unit=float(decimal.Decimal(random.randrange(7,12))/10)
            print(t)
            print(unit)
        elif(time in range(11,15)):
            t="Cold"
            unit=float(decimal.Decimal(random.randrange(7,12))/10)
            print(t)
            print(unit)
        elif(time in range(15,20)):
            t="Mild"
            unit=float(decimal.Decimal(random.randrange(11,14))/10)
            print(t)
            print(unit)
        elif(time in range(20,24)):
            t="Cold"
            unit=float(decimal.Decimal(random.randrange(7,12))/10)
            print(t)
            print(unit)    
    elif(temp in range(22,27)):
        if(time in range(0,5)):
            t="Hot"
            unit=float(decimal.Decimal(random.randrange(14,17))/10)
            print(t)
            print(unit) 
        elif(time in range(5,11)):
            t="Hot"
            unit=float(decimal.Decimal(random.randrange(14,17))/10)
            print(t)
            print(unit)
        elif(time in range(11,15)):
            t="Mild"
            unit=float(decimal.Decimal(random.randrange(11,14))/10)
            print(t)
            print(unit)
        elif(time in range(15,20)):
            t="Mild"
            unit=float(decimal.Decimal(random.randrange(11,14))/10)
            print(t)
            print(unit)
        elif(time in range(20,24)):
            t="Hot"
            unit=float(decimal.Decimal(random.randrange(14,17))/10)
            print(t)
            print(unit)
    elif(temp in range(27,33)):
        if(time in range(5,11)):
            t="Hot"
            unit=float(decimal.Decimal(random.randrange(14,17))/10)
            print(t)
            print(unit)
        elif(time in range(11,15)):
            t="Mild"
            unit=float(decimal.Decimal(random.randrange(11,14))/10)
            print(t)
            print(unit)
        elif(time in range(15,20)):
            t="Hot"
            unit=float(decimal.Decimal(random.randrange(11,14))/10)
            print(t)
            print(unit)
        else:
            print("Temp would not be as high as mentioned, at the mentioned time");
    elif(temp in range(33,40)):
        if(time in range(10,18)):
            t="Hot"
            unit=float(decimal.Decimal(random.randrange(17,20))/10)
            print(t)
            print(unit)
        else:
            print("Temp would not be as high as mentioned, at the mentioned time");
    elif(temp>40):
        t="Hot"
        unit=float(decimal.Decimal(random.randrange(19,24))/10)
        print(t)
        print(unit)
    elif(temp<14):
        t="Cold"
        unit=float(decimal.Decimal(random.randrange(7,12))/10)
        print(t)
        print(unit)

    return unit*1000
            
    """
    Testing code for gridsim
    """
    temp=int(input("Temp: "))
    #time=int(input("Time: "))

    current_hour = int(time.strftime("%H", time.localtime()))

    units(temp,current_hour)

def meter_mapping(mid):
    """
    Maps meter IDs woth temperature and wether from the data.json file
    """
    f = open('data.json',)
    data = json.load(f)

    for i in data['meters']:
        if i['meter'] == mid:
            temp = i['temperature']
            weather = i['weather']

    f.close()
    return temp, weather
