import os



os.mkdir("folder1")



os.makedirs("folder2/subfolder", exist_ok=True)



print(os.listdir())


print(os.getcwd())



os.chdir("folder1")
print("New directory:", os.getcwd())