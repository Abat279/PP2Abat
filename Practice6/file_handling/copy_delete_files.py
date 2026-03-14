import shutil
import os



shutil.copy("file1.txt", "backup1.txt")



shutil.copy("file2.txt", "copy_file2.txt")



shutil.copy2("file3.txt", "backup_file3.txt")



if os.path.exists("backup1.txt"):
    print("File exists")



if os.path.exists("backup1.txt"):
    os.remove("backup1.txt")