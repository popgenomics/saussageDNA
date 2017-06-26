#!/usr/bin/pypy

import sys
infileName = sys.argv[1]
size = int(sys.argv[2])

def parseDNA(infileName):
	res = {}
	res['names'] = []
	res['seq'] = []
	
	cnt = -1
	
	infile = open(infileName, "r")
	seqID = ""	
	for i in infile:
		i = i.strip()
		if i[0] == ">":
			seqID = i[1::]
			cnt += 1
			res['names'].append(seqID)
			res['seq'].append("")
		else:
			res['seq'][cnt] += i
	
	infile.close()
	return(res)

def cutDNA(alignement, size, infileName):
	cnt = -1
	start = range(0, len(alignement['seq'][0]), size)
	for i in start:
		cnt += 1
		outputName = "sub_" + infileName.split(".")[0] + "_" + str(cnt) + ".fas"
		outputName2 = "sub_" + infileName.split(".")[0] + "_" + str(cnt) + ".txt"
		
		
#		print(outputName)
		outFile = open(outputName, "w")
		outFile2 = open(outputName2, "w")
		if (i+size) < len(alignement['seq'][0]):
			outFile2.write("{0}\t{1}\t{2}\n".format(outputName, i, i+size))
			for j in range(len(alignement['seq'])):
				outFile.write(">{0}\n{1}\n".format(alignement['names'][j], alignement['seq'][j][i:(i+size)]))
				#print(">{0}\n{1}\n".format(alignement['names'][j], alignement['seq'][j][i:(i+size)]))
		else:
			outFile2.write("{0}\t{1}\t{2}\n".format(outputName, i, len(alignement['seq'][0])))
			for j in range(len(alignement['seq'])):
				outFile.write(">{0}\n{1}\n".format(alignement['names'][j], alignement['seq'][j][i:]))
				#print(">{0}\n{1}\n".format(alignement['names'][j], alignement['seq'][j][i:]))
		outFile.close()
		outFile2.close()

alignement = parseDNA(infileName)
cutDNA(alignement, size, infileName)


