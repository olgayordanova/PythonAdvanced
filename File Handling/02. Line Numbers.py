import string

with open ('text.txt', 'r') as input_fh:
    lines = input_fh.read().split("\n")

symbols = ["-", ",", ".", "!", "?", "'" ]


with open ( 'output.txt', 'w' ) as output_fh:
    for i in range ( 0, len ( lines ) ):
        count_char = len ( [ch for ch in lines[i] if ch.isalpha ()] )
        count_punct = len ( [ch for ch in lines[i] if ch in symbols] )
        print(f'Line {i+1}: {lines[i]} ({count_char})({count_punct})',file=output_fh )