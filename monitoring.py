# monitoring.py
import requests
import threading

port_choices = ["Local", "Output", "Z1", "Z2", "Z3"]
thread = None
stop_thread_val = 0

# Fonction pour récupérer les statistiques de port
def get_port_stats(port_no):
    try:
        # Ici on ne prend que le switch S1 car il est connecté à z1,z2,z3
        response = requests.get("http://127.0.0.1:8080/stats/port/1")
        response.raise_for_status()
        data = response.json()
        port_stats = data["1"][port_no]
        return port_stats
    except Exception as e:
        return f"Error: {e}"

def thread_monitor(wpc, wd, f):
    global stop_thread_val
    while not stop_thread_val:
        port_no = wpc.value[0]
        port_stats = get_port_stats(port_no)
        if isinstance(port_stats, dict):
            wd.name = f"{port_choices[port_no]} Statistics:"
            wd.values = [
                "",
                f"  RX Packets: {port_stats['rx_packets']} ({port_stats['rx_bytes']} bytes)",
                f"  TX Packets: {port_stats['tx_packets']} ({port_stats['tx_bytes']} bytes)",
                f"  Lost Packets: {port_stats['tx_dropped']}",
                f"  Error Packets: {port_stats['tx_errors']}"
            ]
        else:
            wd.values = [port_stats]
        f.display()

def update_port(widget_port_choice, widget_debug, form):
    global thread
    if len(widget_port_choice.value) > 0:
            if thread is None or not thread.is_alive():
                thread = threading.Thread(target=thread_monitor, args=(widget_port_choice, widget_debug, form))
                thread.start()

def stop_thread():
    global stop_thread_val
    global thread

    if thread is not None:
        if thread.is_alive():
            stop_thread_val = 1
            thread.join()
            stop_thread_val = 0

