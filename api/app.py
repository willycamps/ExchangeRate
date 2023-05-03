from apiflask import APIFlask
from flask_cors import CORS, cross_origin
from flask import request, escape
import requests
import json

#URL & ApiKey variables
urlExchangeRate = 'https://v6.exchangerate-api.com/v6/'
apiKey = '5578f53e5dfd610b97368d18/'

#name APIflask
app = APIFlask(__name__) 
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/getExchange',methods=['POST'])
@cross_origin()
def getExchange():
    dataget = request.get_json()
    
    dataAmount = dataget["amount"] 
    baseCode = dataget["from"]
    targetCode = dataget["to"]
    
    # Where 'dataFrom' is the base currency
    url = urlExchangeRate + apiKey + '/pair/'+baseCode + '/' + targetCode + '/' + dataAmount
    response = requests.get(url)
    data = response.json()
    
    #conversion_rate
    #conversion_result
    #strFrom = 1 / float(data["conversion_rates"][dataTo]) 
    #strTo = float(data["conversion_rates"][dataTo]) 
    #final = float(dataAmount) * float(strTo)

    final = data["conversion_result"]
    #Return JSON response
    result = {}
    #result['rateFrom'] = "1 "+dataFrom+" = "+ str(strTo)
    #result['rateTo'] = "1 "+dataTo+" = "+ str(strFrom)
    #result['result'] = str(final)+ " "+ dataTo 
    result['rateFrom'] = ""
    result['rateTo'] = data["conversion_rate"]
    result['result'] = data["conversion_result"]
    response = app.response_class(
        response=json.dumps(result),
        mimetype='application/json'
    )
    return response


@app.route('/getCodes')
# Enable CORS in flask
@cross_origin()
def getCodes():
    # Get the currency codes
    url = urlExchangeRate + apiKey + 'codes'
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    app.run()
