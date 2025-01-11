import requests

# Function to add a flow entry
def add_flow_entry(flow_data):
    flow_url = "http://127.0.0.1:8080/stats/flowentry/add"
    flow_headers = {
        "Content-Type": "application/json"
    }

    flow_response = requests.post(flow_url, json=flow_data, headers=flow_headers)

    if flow_response.status_code == 200:
        print("Flow entry was successful")
    else:
        print(f"Failed to add flow entry: {flow_response.status_code}")

# Drop flow in zone 2
flow_data_zone_2 = {
    "dpid": 1,
    "table_id": 0,
    "priority": 1,
    "match": {
        "in_port": 2
    },
    "instructions": [
        {
            "type": "APPLY_ACTIONS",
            "actions": [
                {
                    "type": "DROP"
                }
            ]
        }
    ]
}
add_flow_entry(flow_data_zone_2)

# Drop flow in zone 3
flow_data_zone_3 = {
    "dpid": 1,
    "table_id": 0,
    "priority": 1,
    "match": {
        "in_port": 3
    },
    "instructions": [
        {
            "type": "APPLY_ACTIONS",
            "actions": [
                {
                    "type": "DROP"
                }
            ]
        }
    ]
}
add_flow_entry(flow_data_zone_3)
