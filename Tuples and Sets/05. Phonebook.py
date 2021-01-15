from collections import defaultdict
phones = {}
while True:
    line = input()
    if line.isdigit():
        n= int(line)
        break
    name, phone = line.split('-')
    phones[name]=phone

for _ in range (n):
    contact= input()
    if contact in phones:
        print(f"{contact} -> {phones[contact]}")
    else:
        print(f"Contact {contact} does not exist.")

