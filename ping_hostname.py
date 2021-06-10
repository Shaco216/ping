# idea is from: https://stackoverflow.com/questions/2953462/pinging-servers-in-python
import platform
import subprocess
import csv


print('Bitte speicher mir eine Liste mit Namen: all_clients.csv ab.')
print('Wichtig: Bitte im selben Ordner wie das auszuführende Programm speichern')
print('Bitte nur Clientnames in Datei speichern!')
input()
#hostname = input()
transfered_csv = []
with open('all_clients.csv','r', newline='') as f:
    reader = csv.reader(f, delimiter= ',')
    for row in reader:
        transfered_csv.append(row)
        
def ping(transfered_csv):
    clientlist = []
    param = '-n' if platform.system().lower()=='windows' else '-c'
    for entrie in transfered_csv:
        entrie = str(entrie)
        entrie = entrie.replace("['","")
        entrie = entrie.replace("']","")
        command = ['ping', param, '1', entrie] # entrie ist der hostname
        #fjklsfj = subprocess.call(command).
        if subprocess.call(command) == 0: #pingable
            entrie = entrie  + ', ' + 'online'
            clientlist.append(entrie)
            print(entrie)
        else:
            entrie = entrie + ', ' + 'offline'
            clientlist.append(entrie)
            print(entrie)
        #with open('on_offline_clients.csv', 'a', newline=''):
            #writer = csv.writer(f)
            #writer.writerow(entrie)

    with open('on_offline_clients.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            for thing in clientlist:
                writer.writerow([thing])
    #print(clientlist)
            
ping(transfered_csv)
print('fertig!')
input()
