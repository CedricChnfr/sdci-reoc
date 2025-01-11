import requests
import json

# Replace with your Ryu controller's URL (this is the default)
RYU_URL = 'http://localhost:8080/stats/flowentry/add'

# Create the meter entry data payload
data = {
    "dpid": 1,
    "priority": 10000,
    "match": {
        "eth_type": 2048,
        "ipv4_dst": "10.0.0.254"
    },
    "instructions": [
        {
            "type": "APPLY_ACTIONS",
            "actions": [
                {
                    "type": "SET_FIELD",
                    "field": "ipv4_dst",
                    "value": "10.0.0.100"
                },
                {
                    "type": "OUTPUT",
                    "port": "NORMAL"
                }
            ]
        }
    ]
}

# Send the POST request to the Ryu controller
response = requests.post(RYU_URL, json=data)

# Check the response
if response.status_code == 200:
    print("Entry added successfully.")
else:
    print(f"Failed to add entry. Status Code: {response.status_code}, Response: {response.text}")
