#Provides a way of using operating system-dependent functionality like reading or writing to the file system
import os
#Provides a higher-level interface for file operations, such as copying and moving files
import shutil 

#Stores the path to the downloads folder to be organized
path = '/Users/zubinsidhu/Downloads'

#Gets a list of all the files and directories in the path
list_ = os.listdir(path)

#Repeats the sorting process for every file in the given list
for file_ in list_: 
    #Splits the file name into the name and the extension (with the dot)
	name, ext = os.path.splitext(file_)
    #Removes the dot from the extension
	ext = ext[1:]
    #Prevents crash if extension doesn't have dot
	if ext == '': 
		continue
    #Determines if a directory is already named after the file
	if os.path.exists(path+'/'+ext): 
        #Moves to existing directory
		shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
	#Makes a new directory and moves file there
	else: 
		os.makedirs(path+'/'+ext) 
		shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)