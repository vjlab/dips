import os,sys

#Filter vcf file. Discard all the entries where ALT number of reads in DP4 is lower than the REF.
#python filterVCF.py vcf.file > filteredVCF.file


def minor(s):
	if int(s.split(",")[2])+int(s.split(",")[3])<int(s.split(",")[0])+int(s.split(",")[1]):
		return True
	else:
		return False

res=""
with open (sys.argv[1],'r') as fi:
	for line in fi:
		if line[0]!="#":
			dp4=line.split("DP4=")[1].split(";")[0]
			if not minor(dp4):
				res+=line
		else:
			if line!="\n" and line!="":
				res+=line.replace('\n\n','\n')

print(res)