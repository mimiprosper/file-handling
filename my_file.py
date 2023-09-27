# give the file a name
filename = 'emma.txt'

# open the file
with open(filename) as file_obj:
    for line in file_obj:
        
        # print out the file contents line by line
        print(line.rstrip())

        # print(file_obj.read())

