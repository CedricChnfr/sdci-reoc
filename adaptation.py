import requests

def send_packets(port_no, packet_size, packet_count):
    try:
        response = requests.post(f"http://127.0.0.1:8080/stats/port/1", json={
            "port_no": port_no,
            "packet_size": packet_size,
            "packet_count": packet_count
        })
        response.raise_for_status()
        return f"Sent {packet_count} packets of size {packet_size} bytes to Port {port_no + 1}"
    except Exception as e:
        return f"Error: {e}"

def update_adaptation(widget_port_choice, widget_packet_size, widget_packet_count, widget_debug, form):
    if len(widget_port_choice.value) > 0:
        port_no = widget_port_choice.value[0]
        packet_size = widget_packet_size.value
        packet_count = widget_packet_count.value
        result = send_packets(port_no, packet_size, packet_count)
        widget_debug.values = [result]
        form.display()  