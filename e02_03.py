"""read sequence and put in single line"""

#read sequence

with open('data/salmonella_spi1_region.fna', 'r') as f:
    f_list = f.readlines()

    #remove first line
    f_list = f_list[1:]
    print('In the with block, is the file closed?', f.closed)

    seq = ''
    for i in range(len(f_list)):
        #append lines to sequence
        seq += f_list[i].rstrip()
        i = i + 1


print('Out of the with block, is the file closed?', f.closed)


def gc_content (seq, block_size):
    b = block_size
    gc_count = 0

    gc_tuple = ()
    for i in range(len(seq)//block_size):
        gc_count = seq[i*block_size:(i+1)*block_size].count('G') + seq[i*block_size:(i+1)*block_size].count('C')
        print(seq[i*block_size:(i+1)*block_size], gc_count, gc_count/b)
        gc_tuple += (gc_count/b,)

    return(gc_tuple)
