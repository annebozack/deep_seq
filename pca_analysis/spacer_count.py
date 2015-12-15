import xml.etree.ElementTree as ET
import csv
import sys

path = sys.argv[1]

tree = ET.parse(path)
root = tree.getroot()


def spcount(root):
	with open('spacer_count.csv', 'wb') as file:
		wr = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
		i=0
		while i < len(root):
			group = [root[i].attrib]
			wr.writerow(group)
			j = 0
			while j < len(root[i][0][2]):
				spacenum = ["", root[i][0][2][j].attrib, len(root[i][0][2][j])]
				wr.writerow(spacenum)
				j+=1
			i+=1
		file.close()

spcount(root)


