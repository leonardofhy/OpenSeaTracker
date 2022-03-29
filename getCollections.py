import requests
import time
import json

while True:
    print("------------")
    action = input("Please enter your action: (E.g. collect, exit)\n")
    if action == "collect":
        collectName = input("Please enter the collection name:\n")
        headers = {"Accept": "application/json"}
        url = "https://api.opensea.io/api/v1/collection/{}/stats".format(collectName)
        response = requests.get(url, headers=headers)
        values = ["num_owners", "average_price", "total_sales", "total_volume", "total_supply", "floor_price"]
        for value in values:
            print(f"{value}: {json.loads(response.text)['stats'][value]}")
    elif action == "exit":
        print("Exit")
        break
    else:
        print("Invalid action, please enter again.")

    time.sleep(0.5)
    
