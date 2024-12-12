import requests
# docker exec -it mn.z1 bash
# Add a meter entry to limit the flow to 2 bytes per second
meter_url = "http://127.0.0.1:8080/stats/meterentry/add"
meter_data = {
    "dpid": 1,
    "meter_id": 1,
    "flags": "KBPS",
    "bands": [
        {
            "type": "DROP",
            "rate": 2  # 2 bytes per second
        }
    ]
}
meter_headers = {
    "Content-Type": "application/json"
}

meter_response = requests.post(meter_url, json=meter_data, headers=meter_headers)

if meter_response.status_code == 200:
    print("Meter entry was successful")
else:
    print(f"Failed to add meter entry: {meter_response.status_code}")

# Add a flow entry to use the meter
flow_url = "http://127.0.0.1:8080/stats/flowentry/add"
flow_data = {
    "dpid": 1,
    "table_id": 0,
    "priority": 1,
    "match": {
        "in_port": 1
    },
    "instructions": [
        {
            "type": "METER",
            "meter_id": 1
        },
        {
            "type": "APPLY_ACTIONS",
            "actions": [
                {
                    "type": "OUTPUT",
                    "port": 2
                }
            ]
        }
    ]
}
flow_headers = {
    "Content-Type": "application/json"
}

flow_response = requests.post(flow_url, json=flow_data, headers=flow_headers)

if flow_response.status_code == 200:
    print("Flow entry was successful")
else:
    print(f"Failed to add flow entry: {flow_response.status_code}")