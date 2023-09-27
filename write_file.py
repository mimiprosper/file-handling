# give the file a name
filename = 'programming.pdf'

# create the file programming.pdf
with open(filename, 'w') as f:
    # write to the file --> i love python programming
    f.write('i love python programming \n')

    # add more text in new line
    f.write('i want to be a good programmer \n')

    # add more text in new line
    f.write('with 5 star rating \n')


# using a path --> make sure the document is already created
# path = 'document/programming.pdf'
# with open(path, 'w') as f:
#     f.write('i love programming')
