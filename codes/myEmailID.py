#/bin/bash

myEmail = [100, 97, 115, 109, 97, 109, 97, 116, 97, 46, 105, 110, 100, 105, 97]

for i in range(len(myEmail)):
    print(chr(myEmail[i]), end = '')

print("@gmail.com")
