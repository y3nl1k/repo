import shutil
import os

os.mkdir("target_dir") if not os.path.exists("target_dir") else None

if os.path.exists("example2.txt"):
    shutil.move("example2.txt", "target_dir/example_moved.txt")