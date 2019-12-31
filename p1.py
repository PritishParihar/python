#!/usr/bin/python3

import sys,os
def trav(dir):
	for root,dirs,files in os.walk(dir):
		if files != "":
			#dirs="Nil"
			#files="Nil"
			print("Current location:",root)
			if dirs==[]:
				print("Folders inside current location(",root,"): Nil")
			else:
				print("Folders inside current location(",root,"):",dirs)
			if files==[]:
				print('Files inside current location)',root,'): Nil')
			else:
				print('Files inside current location)',root,'):',files)
			print("+++++++++++++++++++++++++++++++++++++++++++++++++")
		elif files==[]:
			files="Nil"
			print('Files inside current location)',root,'):',files)

def main():
	trav(sys.argv[1])

if __name__=='__main__':
	main()
