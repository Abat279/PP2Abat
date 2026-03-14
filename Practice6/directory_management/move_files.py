import shutil
import os



shutil.move("file1.txt", "folder1/file1.txt")



shutil.move("file2.txt", "folder1/file2.txt")



os.rename("file3.txt", "new_file3.txt")


os.rename("new_file3.txt", "folder1/new_file3.txt")


print("Files moved successfully")