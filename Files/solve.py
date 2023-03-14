ctext = b'\x17\x18\x02\x16/*b\x10\t7u"\x109\r(\x05z<\x1e)\x1dg#\x1c#\x06\x17\x0e8\x06 5&\x02!#\x13r=\r\x01s\x0b0t\x17\x18!v=\x1a6\x07\x1e)\x116\x0eg \r+\x1c\x19\x17p:{ \x07\x1c\x0b$.\x0c?c<+(\x13\x13/x\x01,g>y;q+'

# get the dictionary-graph sorted first...
# note some items in here will have repeats, because the challenge creator got a bit lazy with making this perfect
mrt_map = {}
for line in open('database.txt','r').readlines():
    line = line.rstrip().split()
    for ptr, code in enumerate(line):
        
        if ptr == 0:
            add = [line[ptr+1]]
        elif ptr == len(line) - 1:
            add = [line[ptr-1]]
        else:
            add = [line[ptr-1], line[ptr+1]]

        if code not in mrt_map:
            mrt_map[code] = add
        else:
            mrt_map[code] += add

# known plaintext chunk of 'CSIT{' gives the first 2 blocks to be:
# TKK BTN
# which decodes the first 2 blocks as:
# CSIT{d

def stateoftheart_apocalyptic_decryptfunction(blkA, blkB):
    return bytes([i^j for i, j in zip(blkA, blkB)])

# fun little user input algo to obtain the flag
flag = b"CSIT{d"
keys = ["TKK", "BTN"]
currblock = "BTN"
user_input = []
#user_input = [3,1,1,3,1,1,3,1,1,1,2,2,0,0,4,1,1,2,1,0,0,1,3,1,2,1,0,0,0]
for i in range(6,len(ctext),3):
    values = []
    print(f"KEYS: {keys}")
    print(mrt_map[currblock])
    for ptr,val in enumerate(mrt_map[currblock]):
        value = stateoftheart_apocalyptic_decryptfunction(ctext[i:i+3], val.encode())
        print(f"{ptr}. {flag + value}")
        values.append(value)
    if not user_input:
        choice = int(input())
    else:
        choice = user_input[0]
        user_input.pop(0)
    flag += values[choice]
    currblock = mrt_map[currblock][choice]
    keys.append(currblock)
print(flag)