###########################################################
# Python Transcode
# Author: Dave Comstock
#############################################################

import os
import string

orig_dir = "./test_structure/orig"
dest_dir = "./test_structure/dest"

orig_dir_list = {}
orig_file_list ={}

dest_dir_list = {}
dest_file_list = {}

dir_ops_list = {}
file_ops_list = {}


os.chdir(orig_dir)

for root, dirs, files in os.walk("."):
    for dir in dirs:
        #Build the full pathname of directory
        full_path = root+"/"+dir
        orig_dir_list[full_path] = {"root":root, "name":dir}
        
    for file in files:
        #split the file path        
        (base,ext) = os.path.splitext(root+"/"+file)
        #Get the modify time of the file
        full_path = root+"/"+file
        mtime = os.path.getmtime(full_path)
        orig_file_list[full_path] = {"root":root,"base":base, "ext":ext, "mtime":mtime}
        
for root, dirs, files in os.walk("."):
    for dir in dirs:
        #Build the full pathname of directory
        full_path = root+"/"+dir        
        dest_dir_list[full_path] = {"root":root, "name":dir}
        
    for file in files:
        #split the file path
        (base,ext) = os.path.splitext(root+"/"+file)
        #Get the modify time of the file
        full_path = root+"/"+file
        mtime = os.path.getmtime(full_path)      
        dest_file_list[full_path] = {"root":root, "base":base, "ext":ext, "mtime":mtime}
                  



for full_path in orig_dir_list:
    
    cur_orig_data = orig_dir_list[full_path]
    
    dir_ops_list[full_path]={"root":cur_orig_data["root"], "name":cur_orig_data["name"], "op_type":"add"}
    
for full_path in dest_dir_list:
    
    cur_dest_data = dest_dir_list[full_path]
    
    if (dir_ops_list.has_key(full_path)):
        dir_ops_list[full_path]["op_type"]="keep"
    else:
        dir_ops_list[full_path]={"root":cur_orig_data["root"], "name":cur_orig_data["name"], "op_type":"add"}


        
    
    
    
        
        
        
