import os

img_dir = "img_origin/ "
dir_renamed = "img_renamed/ "
f = open("images.txt", "r")
file_text = f.readlines()
#print(file_text)

for file_name in file_text:  
    #full_name = img_dir + file_name
    print(img_dir[:-1] + file_name)
    print(dir_renamed[:-1] + file_name[:5] + file_name[-5:])
    #print(img_dir[:-1] + file_name[:5] + file_name[-4:])
    os.rename(img_dir[:-1] + file_name.rstrip("\n"), dir_renamed[:-1] + file_name[:5] + file_name[-5:].rstrip("\n"))