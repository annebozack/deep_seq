import xml.etree.ElementTree as ET
import csv
import sys

path = sys.argv[1]

path1 = ''+path+'crass1.crispr'
filename1 = 'spacer_count1.csv'
path2 = ''+path+'crass2.crispr'
filename2 = 'spacer_count2.csv'
path3 = ''+path+'crass7.crispr'
filename3 = 'spacer_count7.csv'
path4 = ''+path+'crass60.crispr'
filename4 = 'spacer_count60.csv'


def spcount(path, filename):
	tree = ET.parse(path)
	root = tree.getroot()
	with open(filename, 'wb') as file:
		wr = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
		i=0
		while i < len(root):
			group = [root[i].attrib, "", "", "", ""]
			wr.writerow(group)
			j = 0
			while j < len(root[i][0][2]):
				spacenum = ["", root[i][0][2][j].attrib, len(root[i][0][2][j]), root[i][0][2][j].get('cov'), root[i][0][2][j].get('seq')]
				wr.writerow(spacenum)
				j+=1
			i+=1
		file.close()

spcount(path1, filename1)
spcount(path2, filename2)
spcount(path3, filename3)
spcount(path4, filename4)


