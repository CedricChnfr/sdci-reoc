import socket
import signal
import sys
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 10.0.0.254 is the address of 'gi'
server_address = ('10.0.0.254', 8080)

def signal_handler(sig, frame):
    print("\nInterrupt received, closing socket...")
    client_socket.close()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

try:
    message = "a"
    while True:
        client_socket.sendto(message.encode(), server_address)
        time.sleep(0.1)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Closing socket...")
    client_socket.close()
