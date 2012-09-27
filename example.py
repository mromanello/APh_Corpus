import csv
newdict = {}

# read the csv catalog as a dictionary
with open ('catalog.csv','rb') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        newdict[row['id']]=row
print newdict

# abstract ids grouped by language
bylang = {}
for id in newdict.keys():
    if(bylang.has_key(newdict[id]['lang'])):
        bylang[newdict[id]['lang']]+=[id]
    else:
        bylang[newdict[id]['lang']]=[]
        bylang[newdict[id]['lang']]+=[id]
print bylang

# prints language and number of abstracts for each language
total = 0
for lang in bylang.keys():
	print lang,len(bylang[lang])
	for id in bylang[lang]:
		print id
	total += len(bylang[lang])
print total