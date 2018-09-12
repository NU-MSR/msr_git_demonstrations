import sys

def main():
    print "hello world"
    for i,p in enumerate(sys.path):
        print "Path # {0:d} = {1:s}".format(i,p)

if __name__ == '__main__':
    main()

