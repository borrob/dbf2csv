#!/usr/bin/python

from dbfpy import dbf
sep=';'

def main():
	filein = raw_input('Filepath to dbf: ')

	db=dbf.Dbf(filein)
	fileout=open(filein[0:-3]+'csv','w')
	outstring=''

	colnums=len(db.fieldNames)
	for fldnm in db.fieldNames:
		outstring+=fldnm + sep
	outstring=outstring[0:-1]+'\n'

	fileout.write(outstring)
	outstring=''

	for rec in db:
		for col in rec:
			outstring+='%s' %(col)+sep
		outstring=outstring[0:-1]+'\n'
		fileout.write(outstring)

	fileout.close()

if __name__ == '__main__':
	main()
