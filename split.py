import re, sys
#filename='metamorphosis.txt'

f = sys.stdin

tweetbuf = []

pattern = re.compile('([-]\s|(?<!Mr)(?<!Mrs)[,.?!;]["]?\s+|\s(?=\\"))')

""" Split on fullstop, comma and question marks """
def split(line):
    line = line.strip()
    parts = []
    #if len(line) < 140:
    #    parts = [line]
    #else:
    bits = pattern.split(line)
    while bits:
        parts.append(''.join(bits[0:2]).strip())
        bits = bits[2:]
    return parts

for line in f:
    line = line.strip()
    if line:
        tweetbuf.append(line)
    else:
        if tweetbuf:
            parts = split(' '.join(tweetbuf))
            for part in parts:
                part = part.strip()
                print part
            tweetbuf = []
        print line



