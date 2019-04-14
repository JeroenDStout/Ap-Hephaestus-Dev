import os
import shutil

dir_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../../");

fresh_folders = []
for (root, dirs, files) in os.walk(dir_path):
    for name in dirs:
        if name != "Fresh":
            continue
        fresh_folders.append(os.path.abspath(os.path.join(root, name)))
    
fresh_files = []
for folder in fresh_folders:
    for (root, dirs, files) in os.walk(folder):
        for name in files:
            if not name.endswith(".ftemplate"):
                continue
            fresh_files.append([os.path.abspath(os.path.join(root, name)), os.path.abspath(os.path.join(root + "/../", name.rstrip(".ftemplate")))])
    
print("Copying .ftemplate files...")
 
def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    except shutil.Error as e:
        print('Error: %s' % e)
    except IOError as e:
        print('Error: %s' % e.strerror)

for [input, output] in fresh_files:
    print("* " + os.path.relpath(output, dir_path))
    copyFile(input, output)
    
print("Done.")