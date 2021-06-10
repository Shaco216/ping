# idea is from: https://stackoverflow.com/questions/2953462/pinging-servers-in-python
import platform
import subprocess
import csv
print('Bitte speicher mir eine Liste mit Namen: all_clients.csv ab.')
print('Wichtig: Bitte im selben Ordner wie das auszuführende Programm speichern')
print('Bitte nur Clientnames in Datei speichern!')
#input()
hostname = input()
transfered_csv = []
with open('all_clients.csv','r', newline='') as f:
    reader = csv.reader(f, delimiter= ',')
    for row in reader:
        transfered_csv.append(row)
test = transfered_csv[2]
test = str(test)
test = test.replace("['","")
test = test.replace("']","")
print(hostname)
def ping(hostname):
    

    #onlinelist = []
    #offlinelist = []
    clientlist = []
    param = '-n' if platform.system().lower()=='windows' else '-c'
    #for entrie in transfered_csv:
        #entrie = str(entrie)
    command = ['ping', param, '1', hostname] # entrie ist der hostname
    if subprocess.call(command) == 0: #pingable
        hostname = hostname + ', ' + 'online'
        clientlist.append(hostname)
        print('online')
    else:
        hostname = hostname + ', ' + 'offline'
        clientlist.append(hostname)
        print('offline')
    return clientlist
clientlist = ping(hostname)
#ping(hostname)
with open('on_offline_clients.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(clientlist)
input()
