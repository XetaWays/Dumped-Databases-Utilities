    # coding: utf-8

import re
import os
import sys
import time

tested = 0
symbols = '0123456789abcdefghijklmnopqrstuvwxyz'
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
filename = "Collection_1 \n"

for x in symbols+"!":
    x = x if x != "!" else "symbols"
    for y in symbols+"!":
        y = y if y != "!" else "symbols"
        for z in symbols+"!":
            z = z if z != "!" else "symbols"
            path = "Data/" + x + "/" + y + "/"
            if not os.path.exists(path):
                os.makedirs(path)
            with open(path+z+".txt", "a", encoding='utf8', errors='ignore') as f2:
                for folder in os.listdir("Pending/"):
                    for subfolder in os.listdir("Pending/"+folder):
                        with open("Pending/"+folder+'/'+subfolder, "r", encoding='utf8', errors='ignore') as f:
                            for line in f:
                                if "@" in line:
                                    line = line.replace(";", ":").lower()
                                    char0 = line[0] if line[0] in symbols else "symbols"
                                    char1 = line[1] if line[2] in symbols else "symbols"
                                    char2 = line[2] if line[2] in symbols else "symbols"
                                    if char0 == x and char1 == y and char2 == z:
                                        f2.writelines(line)
                                        print(f"x = {x}, y = {y}, z = {z}, count = {tested}")
                                    tested+=1
                                else:
                                    with open("Errors/" + folder +'.txt', "a", encoding='utf8', errors='ignore') as f3:
                                        f3.writelines(line.replace(";",":"))