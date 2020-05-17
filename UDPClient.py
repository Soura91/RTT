#!/usr/bin/env python3
# UDP client on localhost

import time
import socket
serverName = 'localhost'
serverPort = 12111
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('Input lowercase sentence:')
freq = [40,50,60]
rtt = dict([])
#Outer loop loops for frequency 40 50 and 60
for i in freq:
    m = ''
    rttf = 0;
    #Inner loop where Client sends 100 messages with frequency in a loop
    for j in range(100):
        m += message + '\n'
        #Packet format message + frequency
        message1 = m + str(i)
        clientmsg = message1.encode('ascii')
        start = time.time()
        clientSocket.sendto(clientmsg,(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        end = time.time()
        #Calculating rtt for each message
        rttf = rttf + (end - start);
        text = modifiedMessage.decode('ascii')
        print(text)
        #print RTT for each message
        print("rtt", float(round(((end - start)*1000),2)) ,"ms")
        m = ''
        #Average RTT for 100 messages for every threshold frequency
    rtt[i] = float(round(((rttf/100)*1000),2))

print("     RTT     " + "   Threshold          " +"\n")

for key, value in rtt.items():
    print(value,'ms', '    ->    ', key)


clientSocket.close()
