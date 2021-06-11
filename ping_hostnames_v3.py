import subprocess
import csv

def import_csv_clients():
    hostnames = []
    with open('all_clients.csv', 'r', newline='') as csvlist:
        reader = csv.reader(csvlist)
        for item in reader:
            hostnames.append(item)
    return hostnames

def ping(hostname):


        #ip = name.split()[1]

        hostname = str(hostname)
        hostname = hostname.replace("['","")
        hostname = hostname.replace("']","")
        cmd = f'ping {hostname} -n 1'
        try:
            pingresult = subprocess.check_output(cmd)


            print(pingresult)#wenn pingable dann 0 wenn nicht dann 1
            pingresult = str(pingresult)
            if 'Zielhost nicht erreichbar' in pingresult:
                hostname =hostname + ', ' + 'offline'
                with open('on_offline_clients.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([hostname])
            elif 'Zeitüberschreitung' in pingresult:
                hostname = hostname + ', ' + 'offline'
                with open('on_offline_clients.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([hostname])
            elif 'nicht finden' in pingresult:
                hostname = hostname + ', ' + 'offline'
                with open('on_offline_clients.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([hostname])
            else:
                hostname = hostname + ', ' + 'online'
                with open('on_offline_clients.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([hostname])
            return pingresult
        except Exception as e:
            pingresult = 'Zielhost nicht erreichbar'
            print(pingresult)
            if 'Zielhost nicht erreichbar' in pingresult:
                hostname =hostname + ', ' + 'offline'
                with open('on_offline_clients.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([hostname])
            return pingresult
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
for hostname in hostnames:
    ping(hostname)