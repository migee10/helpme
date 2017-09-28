import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 :  continue
    num = float(stuff[0])
    numlist.append(num)
print ('Number of Values:',len(numlist))
print ('Maximum:', max(numlist))
print ('Minimum:', min(numlist))
print ('Average:', "{:.3f}".format(sum(numlist)/len(numlist)))

