import sys

# primary partner edit

def main():
    print "hello moon"
    for i,p in enumerate(sys.path):
        print "Path # {0:d} = {1:s}".format(i,p)

    print "Also adding code where it hasn't been before"
    return

if __name__ == '__main__':
    main()

