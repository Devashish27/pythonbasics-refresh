import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt")
# print(f.read())
# print(f.read(4))  # For reading first 4 characters...

# print(f.readline())

# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
    print("Found the file")
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# Append - creates the file if it doesn't exist.
f = open("names.txt", "a")
f.write("Ishana\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing,
# creates the file if it doesn't exist

f = open("name_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists..
if not os.path.exists("aron.txt"):
    f = open("aron.txt", "x")
    f.close()

# Delete a file

# Avoid an error if it doesn't exist.
if os.path.exists("aron.txt"):
    os.remove("aron.txt")
else:
    print("The file you wish to delete does not exist")

# Other way to create...
with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
