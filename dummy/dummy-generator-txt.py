import json
import os
import random
import string

alphabet = [char for char in string.ascii_lowercase]

size = 1024*1024*1 # 1MB / 하나의 데이터

str = ""

for i in range(size):
    idx = random.randint(0, 25)
    str += alphabet[idx]

with open('dummy.txt', 'w') as file:
    file.write(str)
 
file_size = os.path.getsize('./dummy.txt') 
print('File Size:', file_size, 'bytes')