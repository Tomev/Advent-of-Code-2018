file_read = open("test.txt", "r")
# file_read = open("input.txt", "r")

line = file_read.readline()

while line:
    print(line)
    line = file_read.readline()
