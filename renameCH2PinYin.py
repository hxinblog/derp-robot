# renameCH2Pinyin.py
# Rename filename from Chinese characters to capitalized pinyin using the
# mapping file and taking out the tone numbers

import os
import re

# File uni2pinyin is a mapping from hex to Pinyin with a tone number
f = open('uni2pinyin')
wf = f.read() # read the whole mapping file

os.chdir('voc') # to rename all files in sub folder 'voc'
myulist = os.listdir(u'.') # read all file names in unicode mode
for x in myulist: # each file name
    filenamePY = ''
    for y in x: # each character
        if 0x4e00 <= ord(y) <= 0x9fff: # Chinese Character Unicode range
            hexCH = (hex(ord(y))[2:]).upper() # strip leading '0x' and change
                                              # to uppercase
            p = re.compile(hexCH+'\t([a-z]+)[\d]*') # define the match pattern
            mp = p.search(wf)
            filenamePY+=mp.group(1).title() # get the pinyin without the tone
                                            # number and capitalize it
        else:
            filenamePY+=y
    print x
    filename = filenamePY[:9]+' '+filenamePY[9:]
    print filename
    os.rename(x,filename)
os.chdir('..') # go back to the parent folder
