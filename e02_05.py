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


#returns a tuple of GC content as a percent
def mapped_seq (seq, block_size, gc_thresh):
    b = block_size
    t = gc_thresh
    gc_count = 0

    upper_lower = ''
    for i in range(len(seq)//block_size):
        gc_count = seq[i*block_size:(i+1)*block_size].count('G') + seq[i*block_size:(i+1)*block_size].count('C')
        #print(seq[i*block_size:(i+1)*block_size], gc_count, gc_count/b)

        if gc_count/b > t:
            upper_lower += seq[i*block_size:(i+1)*block_size].upper()
            print('upper')
        else:
            upper_lower += seq[i*block_size:(i+1)*block_size].lower()
            print('lower')


    with open('salmonella_mod.fna', 'w') as f:
        f.write('>')
        for i in range(60):
            f.write(seq[0:60])
    return(upper_lower)
