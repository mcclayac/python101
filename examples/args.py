

def add_many(*args):
    total = 0
    for arg in args:
        total += arg
 #   print args, " = " , total


def main():
    add_many(5,6,3,2)
    add_many(2)
    add_many()

if __name__ == "__main__":
    main()





    
