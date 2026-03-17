with open("sample.txt", "r") as f:
    f.seek(0) 
    print("List of lines:", f.readlines())