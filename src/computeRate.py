from scapy.config import conf
conf.ipv6_enabled = False
from scapy.all import *
import sys

# get path of pcap file
#INPUTPATH_TCP_h3 = sys.argv[1]
#INPUTPATH_TCP_h4 = sys.argv[2]
#INPUTPATH_UDP_h3 = sys.argv[3]
#INPUTPATH_UDP_h4 = sys.argv[4]
INPUTPATH_TCP_h3 = "../out/TCP_h3.pcap"
INPUTPATH_TCP_h4 = "../out/TCP_h4.pcap"
INPUTPATH_UDP_h3 = "../out/UDP_h3.pcap"
INPUTPATH_UDP_h4 = "../out/UDP_h4.pcap"


# Create dictionaries to store the timestamps of the first and last packets for each flow
first_packet_timestamp = {}
last_packet_timestamp = {}

# Initialize the dictionaries for TCP and UDP flows
first_packet_timestamp['TCP_Flow1'] = float('inf')  # Initialize with a large value
first_packet_timestamp['TCP_Flow2'] = float('inf')
first_packet_timestamp['TCP_Flow3'] = float('inf')
last_packet_timestamp['TCP_Flow1'] = 0  # Initialize with zero
last_packet_timestamp['TCP_Flow2'] = 0
last_packet_timestamp['TCP_Flow3'] = 0
first_packet_timestamp['UDP_Flow1'] = float('inf')
first_packet_timestamp['UDP_Flow2'] = float('inf')
first_packet_timestamp['UDP_Flow3'] = float('inf')
last_packet_timestamp['UDP_Flow1'] = 0
last_packet_timestamp['UDP_Flow2'] = 0
last_packet_timestamp['UDP_Flow3'] = 0

# read pcap
packets_TCP_h3 = rdpcap(INPUTPATH_TCP_h3)
packets_TCP_h4 = rdpcap(INPUTPATH_TCP_h4)
packets_UDP_h3 = rdpcap(INPUTPATH_UDP_h3)
packets_UDP_h4 = rdpcap(INPUTPATH_UDP_h4)

port1=7777
port2=7778
total_packet_size_TCP_Flow1=0
total_packet_size_TCP_Flow2=0
total_packet_size_TCP_Flow3=0
total_packet_size_UDP_Flow1=0
total_packet_size_UDP_Flow2=0
total_packet_size_UDP_Flow3=0

#TCP
count1=0
count2=0
count3=0
for packet in packets_TCP_h3[TCP]:
    #print("dport:",packet[2].dport)
    #print("sport:",packet[2].sport)
    if ((packet[2].dport==port1 or packet[2].sport==port1)):
        total_packet_size_TCP_Flow1+=len(packet)
        count1 +=1
        timestamp = packet.time
        if timestamp < first_packet_timestamp['TCP_Flow1']:
            first_packet_timestamp['TCP_Flow1'] = timestamp
        if timestamp > last_packet_timestamp['TCP_Flow1']:
            last_packet_timestamp['TCP_Flow1'] = timestamp
    elif ((packet[2].dport==port2 or packet[2].sport==port2)):
        total_packet_size_TCP_Flow2+=len(packet)
        count2 +=1
        timestamp = packet.time
        if timestamp < first_packet_timestamp['TCP_Flow2']:
            first_packet_timestamp['TCP_Flow2'] = timestamp
        if timestamp > last_packet_timestamp['TCP_Flow2']:
            last_packet_timestamp['TCP_Flow2'] = timestamp
for packet in packets_TCP_h4[TCP]:
    if ((packet[2].dport==port1 or packet[2].sport==port1)):
        total_packet_size_TCP_Flow3+=len(packet)
        count3 +=1
        timestamp = packet.time
        if timestamp < first_packet_timestamp['TCP_Flow3']:
            first_packet_timestamp['TCP_Flow3'] = timestamp
        if timestamp > last_packet_timestamp['TCP_Flow3']:
            last_packet_timestamp['TCP_Flow3'] = timestamp

# Calculate the time span for each flow
time_span_TCP_Flow1 = last_packet_timestamp['TCP_Flow1'] - first_packet_timestamp['TCP_Flow1']
time_span_TCP_Flow2 = last_packet_timestamp['TCP_Flow2'] - first_packet_timestamp['TCP_Flow2']
time_span_TCP_Flow3 = last_packet_timestamp['TCP_Flow3'] - first_packet_timestamp['TCP_Flow3']

print ("--- TCP ---")
print (f"Flow1(h1->h3):{8*total_packet_size_TCP_Flow1/(1000000*time_span_TCP_Flow1)} Mbps")
print (f"Flow2(h1->h3):{8*total_packet_size_TCP_Flow2/(1000000*time_span_TCP_Flow2)} Mbps")
print (f"Flow3(h2->h4):{8*total_packet_size_TCP_Flow3/(1000000*time_span_TCP_Flow3)} Mbps")
# print ("number of Flow1 packets: ", count1)
# print ("number of Flow2 packets: ", count2)
# print ("number of Flow3 packets: ", count3)

#UDP
count1=0
count2=0
count3=0
for packet  in packets_UDP_h3[UDP]:
    if ((packet[2].dport==port1 or packet[2].sport==port1)):
        total_packet_size_UDP_Flow1+=len(packet)
        count1 +=1
        timestamp = packet.time
        if timestamp < first_packet_timestamp['UDP_Flow1']:
            first_packet_timestamp['UDP_Flow1'] = timestamp
        if timestamp > last_packet_timestamp['UDP_Flow1']:
            last_packet_timestamp['UDP_Flow1'] = timestamp
    elif ((packet[2].dport==port2 or packet[2].sport==port2)):
        total_packet_size_UDP_Flow2+=len(packet)
        count2 +=1
        timestamp = packet.time
        if timestamp < first_packet_timestamp['UDP_Flow2']:
            first_packet_timestamp['UDP_Flow2'] = timestamp
        if timestamp > last_packet_timestamp['UDP_Flow2']:
            last_packet_timestamp['UDP_Flow2'] = timestamp
for packet in packets_UDP_h4[UDP]:
    if ((packet[2].dport==port1 or packet[2].sport==port1)):
        total_packet_size_UDP_Flow3+=len(packet)
        count3 +=1
        timestamp = packet.time
        if timestamp < first_packet_timestamp['UDP_Flow3']:
            first_packet_timestamp['UDP_Flow3'] = timestamp
        if timestamp > last_packet_timestamp['UDP_Flow3']:
            last_packet_timestamp['UDP_Flow3'] = timestamp

time_span_UDP_Flow1 = last_packet_timestamp['UDP_Flow1'] - first_packet_timestamp['UDP_Flow1']
time_span_UDP_Flow2 = last_packet_timestamp['UDP_Flow2'] - first_packet_timestamp['UDP_Flow2']
time_span_UDP_Flow3 = last_packet_timestamp['UDP_Flow3'] - first_packet_timestamp['UDP_Flow3']
print ("--- UDP ---")
print (f"Flow1(h1->h3):{8*total_packet_size_UDP_Flow1/(1000000*time_span_UDP_Flow1)} Mbps")
print (f"Flow2(h1->h3):{8*total_packet_size_UDP_Flow2/(1000000*time_span_UDP_Flow2)} Mbps")
print (f"Flow3(h2->h4):{8*total_packet_size_UDP_Flow3/(1000000*time_span_UDP_Flow3)} Mbps")
# print ("number of Flow1 packets: ", count1)
# print ("number of Flow2 packets: ", count2)
# print ("number of Flow3 packets: ", count3)












