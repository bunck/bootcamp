"""read sequence and put in single line"""

#read sequence

with open('data/salmonella_spi1_region.fna', 'r') as f:
    f_list = f.readlines()
    f_list = f_list[1:]
    print('In the with block, is the file closed?', f.closed)

    seq = ''
    for i in range(len(f_list)):
        seq += f_list[i].rstrip()
        i = i + 1

    print(seq)

print('Out of the with block, is the file closed?', f.closed)
