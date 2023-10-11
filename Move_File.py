import os
import shutil
from_dir = r'C:\Users\arung\Downloads\C102_assets-main\C102_assets-main'
to_dir = r'C:\Users\arung\Desktop\ByjuS\Class102\DownloadedImages'
list_of_files = os.listdir(from_dir)
print(list_of_files)
for filename in list_of_files:
    root,extension = os.path.splitext(filename)
    if extension == '':
        continue
    if extension in ['.gif','.png','.jpg','.jepg','.jfif']:
        path1 = from_dir + '/' + filename
        path2 = to_dir + '/' + 'image_files'
        path3 = to_dir + '/' + 'image_files' + '/' + filename
        if os.path.exists(path2): 
            print('moving' + filename + '...')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('moving' + filename + '...')
            shutil.move(path1,path3)