#!/usr/bin/python
import os
import re
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv[1])

line_regex = re.compile(r"^\d")

logFile = sys.argv[1]
tempList = []

filelist = []
    for root, dirs, files in os.walk(dirname,  topdown=True):
         files = [i for i in files if re.match(filepat, i)]
        for i, name in enumerate(files):
                 filelist.insert(i, os.path.join(root, name))

    for filename in filelist:
        if os.path.splitext(filename)[1] == '.gz':
            with gzip.open(filename, 'r') as f:
                for line in f:
                    yield line
        if os.path.splitext(filename)[1] == '.bz2':
            with bz2.BZ2File(filename, 'r') as f:
                for line in f:
                    yield line
        else:
            with open(filename, 'r') as f:
                for line in f:
                    yield line

with open("parsed_logs.txt", "a") as out_file:
        with open(logFile, "r") as in_file:
                for line in in_file:
                        if (line_regex.search(line)):
                                #print "{}+{}i".format(int(float(re.split("\t",line)[1].lstrip())),int(float(re.split("\t",line)[2].lstrip()))).replace("+-", "-")

                                tempList.append("{}+{}i".format(int(float(re.split("\t",line)[1].lstrip())),int(float(re.split("\t",line)[2].lstrip()))).replace("+-", "-"))

                #out_file.write(line)

#tempList = tempList[0:600]
ListOfSubframes = [tempList[x:x+8400] for x in range(0, len(tempList), 8400)]
ListOfSymbols = [tempList[x:x+600] for x in range(0, len(tempList), 600)]
print SecondList[1]

tempList.insert(0,"{{")
print tempList

for p in tempList: print p