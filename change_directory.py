import os
dir = input("Name a folder to be created. It will be deleted immediately afterwards.\n")
os.mkdir(dir)
os.chdir(dir)
print(os.getcwd())
os.chdir("..")

os.rmdir(dir)