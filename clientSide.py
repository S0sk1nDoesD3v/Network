import socket
from datetime import datetime
#initializing host, port, filename, total time and number of times to send the file
host = '192.168.0.14'
port = 9000
fileName = "send.txt"
totalTime = 0
numTimesSend = 100
print('I am connecting to server side: ', host,'\n')
#using a for loop to send the file 100 times 
for x in range(numTimesSend):
    #recording the start time
    startTime = datetime.now()
    #connecting to the server
    s = socket.socket()
    s.connect((host, port))
    x+=1
    #s.send('name.txt'.ljust(100).encode('utf-8'))
    print('I am sending file', fileName,' for the ',x,'th  time')
    #opening file to read
    file_to_send = open(fileName, 'rb')    
    #reading the first 1024 bits
    data = file_to_send.read(1024)
    
    while data:
        s.send(data)
        #reading the next 1024 bits
        data = file_to_send.read(1024)
    print('I am finishing sending file', fileName,' for the ',x,'th  time')
    file_to_send.close()
    #recording the end time
    endTime = datetime.now()
    timeTaken = int((endTime - startTime).total_seconds() * 1000)
    totalTime += timeTaken
    print('The time used in millisecond to receive ', fileName ,' for ', x,'th time is: ',timeTaken,"\n")
    s.close()

print('The average time to receive file ',fileName,' in millisecond is: ',totalTime/numTimesSend)
print('Total time to receive file ',fileName,' for ',numTimesSend,' times in millisecond is: ',totalTime)
print('I am done')
