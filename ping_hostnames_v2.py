import os
import csv

def import_csv_clients():
    hostnames = []
    with open('all_clients.csv', 'r', newline='') as csvlist:
        reader = csv.reader(csvlist)
        for item in reader:
            hostnames.append(item)
    return hostnames

def ping(hostnames):
    for name in hostnames:
        #ip = name.split()[1]
        hostname = name
        hostname = str(hostname)
        hostname = hostname.replace("['","")
        hostname = hostname.replace("']","")
        #os.popen()
        pingresult = os.system("ping "+hostname+" -n 1")#.read()
        print(pingresult)#wenn pingable dann 0 wenn nicht dann 1
        if pingresult == 0:
            hostname =hostname + ', ' + 'online'
            with open('on_offline_clients.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([hostname])
        if pingresult == 1:
            hostname = hostname + ', ' + 'offline'
            with open('on_offline_clients.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([hostname])
        #if 'Zeitüberschreitung der Anforderung' in pingresult:
            #print(pingresult)
            #hostname = hostname + ', ' + 'offline'
            #with open('on_offline_clients.csv', 'a', newline='') as f:
                #writer = csv.writer(f)
                #writer.writerow([hostname])
        #elif 'Zielhost nicht erreichbar' in pingresult:
            #print(pingresult)
            #hostname = hostname + ', ' + 'offline'
            #with open('on_offline_clients.csv', 'a', newline='') as f:
                #writer = csv.writer(f)
                #writer.writerow([hostname])
        #else:
            #print(pingresult)
            #hostname =hostname + ', ' + 'online'
            #with open('on_offline_clients.csv', 'a', newline='') as f:
                #writer = csv.writer(f)
                #writer.writerow([hostname])
hostnames = import_csv_clients()
ping(hostnames)