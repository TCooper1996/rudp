import socket
import pickle
import Packet
from datetime import datetime, time
import time

server_address = "localhost"
server_port = 45454

receiver_address = None
receiver_port = None

file_name = "send.txt"

files_to_send = 100

packet_size = 8 * 1024

seq = None

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start_time = time.time()


def synchronize():
    enquiry = 0
    address = None
    while enquiry != 5:
        (seq_num, address) = s.recvfrom(4)
        enquiry = pickle.loads(seq_num).get_seq()
    s.bind(address)
    s.send(enquiry.reply())

    seq = pickle.loads(s.recv(4)).get_seq()
    print(f"Connected to {address}, with starting sequence number {seq}")


synchronize()
for file_count in range(files_to_send):
    send_time = time.time()
    server_location = (server_address, server_port)
    print("Sending file ")
