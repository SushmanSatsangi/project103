import os
import shutil

from_dir = "E:\Entertainment"
to_dir = "E:\Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == "":
        continue

    if extension in ['.mp4','.txt', '.doc', '.docx', '.mp3', '.pdf']:
        path1 = from_dir + '/' + file_name # path1 : Entertainment/VideoName.mp4
        path2 = to_dir + '/' + "Video Files" # path2 : E:/My Videos/Video Files
        path3 = to_dir + '/' + "Video Files" + "/" + file_name # E:/My Videos/Video File/VideoName.mp4

    if os.path.exists(path2):
        print("Moving" + file_name + '....')
        shutil.move(path1, path3)

    else: 
        os.makedirs(path2)
        print("Moving" + file_name + '....')
        shutil.move(path1, path3)