#!/usr/bin/env python3
# UDP  server on localhost

import time
from random import *
from socket import *
serverPort = 12111
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
rand =0
while 1:
        #Genertaing random number
        rand = randrange(0, 100, 5)
        print('random number is', rand)
        message, clientAddress = serverSocket.recvfrom(2048)
        servermsg = message.decode('ascii')
        #Extracting the frequency
        freq = servermsg.splitlines()[1]
        servermsg = servermsg.rstrip(freq)
        modifiedMessage = servermsg.upper().encode('ascii')
        print('frequency', freq)
        if rand <= int(freq):
            serverSocket.sendto(modifiedMessage, clientAddress)
        else:
            #Sleep for 2s if the random number generated is more than the frequency
            time.sleep(2)
            serverSocket.sendto(modifiedMessage, clientAddress)