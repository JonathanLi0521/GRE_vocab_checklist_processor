INFILEPATH = "./GREin.txt"
OUTFILEPATH = "./GREout.txt"
STARTINGINDEX = 0

infile = open(INFILEPATH, "r")
outfile = open(OUTFILEPATH, "w+")

index = STARTINGINDEX
for line in infile:
    if("- [x]" in line):
        outfile.write(str(index) + ". " + line)
        index += 1
