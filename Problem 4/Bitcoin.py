# First lets import the modules that we will use

import sys # Recall that this will allow us hold the command-line arguments passed to the script
import requests

if  len(sys.argv) == 2: # This will check if user has put anything after 'bitcoin.py'
    try:
        value = float(sys.argv[1])

    except ValueError: #In the situation where a user does not insert a number
        print("command-line is not a number")
        sys.exit(1) # This is just a feature of the sys library. The number '1' is arbitary.


else: # In the situation where the user did not input anything after
    print("Missing command-line argument")
    sys.exit(1)




######Understand this better!!!

try:
    r  = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json') # Sends a GET request to CoinDesk API ( JSON is commonly used for data exchange between a server and a web application,)
    reply = r.json() #converts our response to a JSON object
    bitcoin_value = reply['bpi']['USD']['rate_float'] #This will extract the current USD rate of Bitcoin
    amount = bitcoin_value * value
    print(f"${amount:,.4f}")

except requests.RequestException: # This will catch any errors which might occur when making a request to the CoinDesk API.
    print("RequestException")
    sys.exit(1)
