import os
def rename_files() :
	# get file names from a directory
	file_list = os.listdir(r"/home/ujjwal/Desktop/photo/prank")
	print (file_list)

	saved_path = os.getcwd()
	os.chdir (r"/home/ujjwal/Desktop/photo/prank")

	# for each file, rename filename
	for file_name in file_list :
		os.rename(file_name,file_name.translate(None, "0123456789"))
	os.chdir (saved_path) 

rename_files()