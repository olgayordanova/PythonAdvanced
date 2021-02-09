def reverse_line(str):
    # l = str.split()
    return ' '.join(list(reversed(str.split())))

def replaced_line(line, symbols):
    res =''
    for ch in line:
        if ch not in symbols:
            res += ch
        else:
            res += '@'
    res = reverse_line(res)
    return res


with open ('text.txt', 'r') as input_fh:
    lines = input_fh.read().split("\n")
symbols = ["-", ",", ".", "!", "?" ]

lines = [lines[i] for i in range (len(lines)) if i%2==0]
lines = [replaced_line(line, symbols) for line in lines]

for el in lines:
    print(el)


