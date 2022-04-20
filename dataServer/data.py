from flask import Flask
from flask import jsonify
import requests
import schedule

app = Flask(__name__)
@app.route("/backEnd")

def backEnd():
    #fetch data from texas breweries
    data = requests.get("https://api.openbrewerydb.org/breweries?by_state=texas")
    breweries = data.json()

    #create a user-friendly list of texas breweries
    lst = []
    for x in breweries:
        lst.append({'Name':x['name'],
                    'Brewery Type':x['brewery_type'],
                    'Address':x['street'],
                    'City':x['city'],
                    'Zip Code':x['postal_code'],
                    'Phone':x['phone'],
                    'Website':x['website_url']})
    return jsonify(lst)

#schedule data collection every day
schedule.every().day.do(backEnd)

if __name__ == "__main__":
    app.run(debug = True)
