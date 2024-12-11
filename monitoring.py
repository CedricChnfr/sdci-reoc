# monitoring.py
import requests

def get_port_stats(port_no):
    try:
        response = requests.get("http://127.0.0.1:8080/stats/port/1")
        response.raise_for_status()
        data = response.json()
        port_stats = data["1"][port_no]
        return port_stats
    except Exception as e:
        return f"Error: {e}"

def update_port(widget_port_choice, widget_debug, form):
    if len(widget_port_choice.value) > 0:
        port_no = widget_port_choice.value[0]
        port_stats = get_port_stats(port_no)
        if isinstance(port_stats, dict):
            widget_debug.values = [
                f"Port {port_no + 1} Statistics:",
                f"  packet_reçu: {port_stats['rx_packets']}",
                f"  packet_envoyé: {port_stats['tx_packets']}",
                f"  octets_reçu: {port_stats['rx_bytes']}",
                f"  octets_envoyé: {port_stats['tx_bytes']}",
                f"  paquet_perdu_reçu: {port_stats['rx_dropped']}",
                f"  paquet_perdu_envoyé: {port_stats['tx_dropped']}",
                f"  erreurs_reçu: {port_stats['rx_errors']}",
                f"  erreurs_envoyé: {port_stats['tx_errors']}"
            ]
        else:
            widget_debug.values = [port_stats]
        form.display()  # Redraw the form with the updated debug box