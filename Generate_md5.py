import os
import hashlib
import csv

paths = [] #lista in care vom memora caile fisierelor
codes = [] #lista in care vom memora md5-urile pentru fiecare fisier din lista paths

def print_md5(file): #functia ce returneaza md5-ul, primind ca parametru calea completa a unui fisier
    code = file.encode()
    byte = hashlib.md5(code)
    hex = byte.hexdigest()
    return hex

def list_dir(dir): #functia ce primeste ca parametru calea unui director si adauga recursiv la lista paths toate fisierele din director
    filenames = os.listdir(dir)
    for file in filenames:
        new_path = os.path.abspath(os.path.join(dir,file))
        if os.path.isfile(new_path):
            paths.append(new_path)
            codes.append(print_md5(new_path))
        else:
            list_dir(new_path)

f = open("input.txt", encoding="utf8") #deschidem fisierul de intrare

for path in f:
    path_type = 0
    l = len(path)
    if path[l-1] == "\n":
        path = path[:-1]

    if os.path.isdir(path): #daca este director
        path_type = 1
    elif os.path.isfile(path): #altfel, daca este fisier
        path_type = 2

    if path_type == 1: #daca este fisier
        list_dir(path) #ii cautam fisierele
    else: #altfel adaugam la liste calea si md5-ul
        paths.append(path)
        codes.append(print_md5(path))

    l = len(paths)

    #introducem datele din listele paths si codes in fisierul checksum
    with open("checksum.csv", "w", encoding="utf-8", newline="") as output:
        output_writer = csv.writer(output)

        for index in range(l):
            output_writer.writerow([paths[index] , codes[index]])