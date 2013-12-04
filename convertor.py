#!/usr/bin/python
#
# quick dbf 2 csv converter
#
# based on dbfypy (http://dbfpy.sourceforge.net)
#
# ABSOLUTELY NO WARRENTY

from dbfpy import dbf

#define the seperator for the csv file
sep=';'

def main():
	#filename (and path) to the original dbf file
	filein = raw_input('Filepath to dbf: ')
	db=dbf.Dbf(filein)
	fileout=open(filein[0:-3]+'csv','w') #the csv is saved in the same directory as the original dbf
	outstring=''

	#first row in the csv is for the fieldnames
	for fldnm in db.fieldNames:
		outstring+=fldnm + sep
	outstring=outstring[0:-1]+'\n'

	fileout.write(outstring) #write to file
	outstring=''

	for rec in db:
	#loop over all records
		for col in rec:
		#loop over all columnes
			outstring+='%s' %(col)+sep
		outstring=outstring[0:-1]+'\n'
		fileout.write(outstring)
		outstring=''

	fileout.close()

if __name__ == '__main__':
	main()
