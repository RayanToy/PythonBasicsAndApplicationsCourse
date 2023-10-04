import os

for cur_dir, subdirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py"):
            print(cur_dir)
            break