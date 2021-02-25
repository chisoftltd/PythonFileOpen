# Python File Open
f = open("demofile.txt", "a")
f.write("\nMy Training in Python")
f.close()

# Open a File on the Server
f = open("demofile.txt", "r")
print(f.read())
f.close()
print()

# Read Only Parts of the File
f = open("demofile.txt", "r")
print(f.read(13))
f.close()
print()

# Write to an Existing File
f = open("demofile2.txt", "a")
f.write("\nNow the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

# Write to an Existing File
f = open("demofile2.txt", "a")
f.write("\nNow the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

# Write to an Existing File
f = open("myfile.txt", "x")
f.write("\nNow the file has content!")
f.close()

#open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read())

# Write to an Existing File
f = open("myfile2.txt", "w")
f.write("\nWoops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("myfile2.txt", "r")
print(f.read())