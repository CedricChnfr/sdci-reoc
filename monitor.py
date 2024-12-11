import requests

# Fonction pour récupérer les statistiques de port
def get_port_stats(port_no):
    try:
        # Ici on ne prend que le switch S1 car il est connecté à z1,z2,z3
        response = requests.get("http://127.0.0.1:8080/stats/port/1")
        response.raise_for_status()
        data = response.json()
        return data["1"][port_no]
    except Exception as e:
        return f"Error: {e}"