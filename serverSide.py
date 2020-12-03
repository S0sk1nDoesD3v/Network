import socket
import filecmp
from datetime import datetime
#initializing host, port
HOST = '192.168.0.14'
PORT = 9000
#starting the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
totalTime = 0
print('I am ready for any client side request \n')
totalFilesCount = 100
i=0;
fileName = 'rec.txt';
while True:
    conn, addr = s.accept()
    #recording the start time
    startTime = datetime.now()
    i = i+1
    
    file = 'receive'+str(i)+'.txt';
    
    print('I am starting receiving file ', fileName, 'for the ',i,'th time')
    #opening the file to write
    f = open(file, 'wb')
    data = conn.recv(1024)
    while (data):
        f.write(data)
        data = conn.recv(1024)
    
    f.close()

    print('I am finishing receiving file ', fileName, 'for the ',i,'th time ')
    #recording the end time
    endTime = datetime.now()
    timeTaken = int((endTime - startTime).total_seconds() * 1000)
    totalTime += timeTaken
    print('The time used in millisecond to receive ', fileName ,' for ', i,'th time is: ',timeTaken,'\n')
    if i == totalFilesCount: break;
    conn.close()
s.close()
print('The average time to receive file ',fileName,' in millisecond is: ',totalTime/totalFilesCount)
print('Total time to receive file ',fileName,' for ',totalFilesCount,' times in millisecond is: ',totalTime)
f=0
#checking whether the correct data is recieved or not
for x in range(totalFilesCount):
    x += 1
    res = filecmp.cmp('CompareStandard.txt','receive'+str(x)+'.txt',shallow=False)
    if res == False: f += 1
print(f , ' Times out of ' , totalFilesCount , ' are not correct!')
print('I am done')



    


