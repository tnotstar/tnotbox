from scapy.all import sendp
from scapy.layers.l2 import Ether


def send_wakeonlan_layer2(mac_address):
    # convert mac_address from string to bytes
    mac_clean = mac_address.replace(":", "").replace("-", "")
    mac_bytes = bytes.fromhex(mac_clean)

    # create the WoL payload
    payload = b'\xFF' * 6 + mac_bytes * 16

    # create ethernet frame dst = broadcast address / payload
    magic_packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ payload
    
    # send magic packet to the broadcast address
    sendp(magic_packet)


def main():
    print("Voy...")
    send_wakeonlan_layer2("50:28:4A:98:DE:74")
    print("...vengo!")
