# Python File Open
f = open("demofile.txt", "a")
f.write("\nMy Training in Python")

# Open a File on the Server
f = open("demofile.txt", "r")
print(f.read())
print()

# Read Only Parts of the File
f = open("demofile.txt", "r")
print(f.read(13))
