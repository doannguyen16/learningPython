import sys
import os

# https://www.w3schools.com/python/python_file_remove.asp

# python script.py "/abc/config a.yaml" ""
print("Script " + sys.argv[1] + " " + sys.argv[2])

# line by line
# "r" throw exception when not found
f = open("text.txt", "r")
print(f.read())

# write-append append without breakline.
# create if not found
f = open("text.txt", "a")
f.write("\nNow the file has more content!")
f.close()

# write-override
# create if not found
f = open("text.txt", "w")
f.write("Override")
f.close()

# create file
# "x" -> throw error when file existed.
# f = open("text.txt", "x")

# delete file.
os.remove("text.txt")