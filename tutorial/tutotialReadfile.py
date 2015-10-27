


# Define a filename.
filename = "tonyfile.txt"

# Open the file as f.
# The function readlines() reads the file.
with open(filename) as f:
    content = f.readlines()

# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.
for line in content:
    print(line)


import os.path

# Define a filename.
filename = "tonyfile2.txt"

if not os.path.isfile(filename):
    print('File does not exist.')
else:
    # Open the file as f.
    # The function readlines() reads the file.
    with open(filename) as f:
        content = f.read().splitlines()

    # Show the file contents line by line.
    # We added the comma to print single newlines and not double newlines.
    # This is because the lines contain the newline character '\n'.
for line in content:
    print(line)

# Filename to write
filename = "tonyfile3.txt"

# Open the file with writing permission
myfile = open(filename, 'w')

# Write a line to the file
myfile.write('Written with Python\n')

# Close the file
myfile.close()



# Filename to append
filename = "tonyfile3.txt"

# The 'a' flag tells Python to keep the file contents
# and append (add line) at the end of the file.
myfile = open(filename, 'a')

# Add the line
myfile.write('Written with Python 3 again\n')

# Close the file
myfile.close()


# Flag	Action
# r	 open file for reading
# w	open file for writing (will truncate file)
# b	binary mode
# r+	open file reading and writing
# a+	open file for reading and writing (appends to end)
# w+	open file for reading and writing (truncates file)




import csv

with open('persons.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Name", "Profession"])
    filewriter.writerow(['Derek', 'Software Developer'])
    filewriter.writerow(['Steve', 'Software Developer'])
    filewriter.writerow(['Paul', 'Manager'])