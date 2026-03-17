import os
os.makedirs("parent/child/grandchild", exist_ok=True)
print("Files and dirs:", os.listdir("."))
print("Current location:", os.getcwd())