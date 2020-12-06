import csv
import hashlib

def print_md5(file): #functia ce returneaza md5-ul, primind ca parametru calea completa a unui fisier
    code = file.encode()
    byte = hashlib.md5(code)
    hex = byte.hexdigest()
    return hex

d = {} #declaram dictionarul

with open("checksum.csv", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    for line in csv_reader:
        d[line[0]] = line[1]

for file in d:
    if d[file] == print_md5(file):
        print("Same md5")
    else:
        print("Different md5")