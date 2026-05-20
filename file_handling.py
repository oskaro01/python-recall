# Open the file in read mode. "r" means read-only access.
# encoding='utf8' tells Python to decode the file text using UTF-8 character encoding.


with open("myfile.txt", "r", encoding='utf8') as file:
    for line in file:
        print(line) 
