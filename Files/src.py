def stateoftheart_apocalyptic_encryptfunction(blkA, blkB):
    return bytes([i^j for i, j in zip(blkA, blkB)])

flag = open('flag.txt','rb').read()
geo_codes = open('secret','rb').read().rstrip().split()
# example:
# BGB BBT JUR CNG LKS

ctext = b''
for i in range(0,len(flag),3):
    assert len(geo_codes[i//3]) == len(flag[i:i+3])
    ctext += stateoftheart_apocalyptic_encryptfunction(flag[i:i+3], geo_codes[i//3])
print(f"ctext = {ctext}")

#ctext = b'\x17\x18\x02\x16/*b\x10\t7u"\x109\r(\x05z<\x1e)\x1dg#\x1c#\x06\x17\x0e8\x06 5&\x02!#\x13r=\r\x01s\x0b0t\x17\x18!v=\x1a6\x07\x1e)\x116\x0eg \r+\x1c\x19\x17p:{ \x07\x1c\x0b$.\x0c?c<+(\x13\x13/x\x01,g>y;q+'