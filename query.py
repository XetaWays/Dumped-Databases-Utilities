# coding: utf-8

import os
import argparse
import sys
from tabulate import tabulate

hash = []
def stopProg():
    print("\n")
    print("-"*10+'Enter an email'+"-"*10, 'red')
    print("\n")
    exit()

email = sys.argv[1].lower() if len(sys.argv) > 1 else stopProg()
if len(email) > 2:
    with open("Data/"+email[0]+"/"+email[1]+"/"+email[2]+".txt", "r", encoding="utf-8", errors='ignore') as f:
        for line in f:
            if line.split(":")[0].lower().lower() == email:
                temp = []
                temp.append(email)
                temp.append(line.split(":")[1])
                temp.append(line.split(":")[2].replace('\n',''))
                hash.append(temp)
print('\n')
print(tabulate(hash, headers=['Email', 'Passowrd', "Database"], tablefmt='github'))
print('\n')

