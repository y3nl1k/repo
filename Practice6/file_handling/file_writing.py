with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("First line\n")
    f.writelines(["Second line\n", "Third line\n"])
with open("sample.txt", "a") as f:
    f.write("Appended line\n")