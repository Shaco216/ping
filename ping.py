import os

hostname_to_check = input('Hostname to Check: ')
os.system('ping '+hostname_to_check+' -n 2')
input()