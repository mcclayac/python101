
import sys

if (len(sys.argv) < 3):
    print "you neet to sepcify two directries"
    print sys.argv[0], "<directory 1> <directory 2>"
    sys.exit()

directory1 = sys.argv[1]
directory2 = sys.argv[2]

print ("Comaring:")
print (directory1)
print (directory2)
print


for directory in [director1, directory2]:
    if nt os.access)directory, os.F_OK):
        print directory, "isn't a valida directory!"
        sys.exit()

    print ("Directory", directory)
    for item in os.walk(directory):
        print item
    print

    
