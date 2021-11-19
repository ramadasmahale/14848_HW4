import sys

for line in sys.stdin:
    line = line.strip()
    temperature = int(line[87:92])
    qlty_idx = int(line[92])
    qlty_flags = [0,1,4,5,9]
    if ((temperature != 9999) and qlty_idx in qlty_flags):
        print('%s\t%d' % (line[15:23], int(line[87:92])))