import shutil
import os
shutil.copy("sample.txt", "example.txt")
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted safely")