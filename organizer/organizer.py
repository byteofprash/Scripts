#!/usr/bin/env python

import sys,argparse,os,glob

# categorize

def categorize():
	args = getargs()
	path = args.path
	files = glob.glob(path +"/*")
	print files
	documents = [];pictures = [];videos = [];audio = [];compressed = [];ppts = []
	for filename in files:
		extension = os.path.splitext(filename)[1]
		if (extension in ['.ppt','.pptx','.odp','.pps']):
			move_file(filename,path,'ppt')
		elif (extension in ['.odt','.doc','.docx','.rtf','.txt','.pdf']):
			move_file(filename,path,'Documents')
		elif (extension in ['.zip','.rar','.gz','.bz2']):
			move_file(filename,path,'Compressed')
		elif (extension in ['.jpg','.gif','.png','.jpeg','.tiff','tif','.bmp']):
			move_file(filename,path,'Pictures')
		elif (extension in ['.avi','.mov','.mkv','.mp4','.mp3','.wav']):
			move_file(filename,path,'Media')



def move_file(filename,path,dirname):
	if not os.path.isdir(dirname):
		os.makedirs(dirname)
		os.rename(filename,path+"/"+dirname+"/"+filename)
		print filename + "\t => \t" + path + "/" + dirname
	else:
		os.rename(filename,path+"/"+dirname+"/"+filename)
		print filename + "\t => \t" + path + "/" + dirname


# Obtaining the path of the directory as an argument
def getargs():
	parser = argparse.ArgumentParser()
	parser.add_argument("path",help = "Enter the path of the directory which you want to categorize")
	args = parser.parse_args()
	return args


if __name__ == '__main__':
	categorize()
