import sys

def main():
    print "This is me putting a print line on the third branch"
    for p in sys.path:
        print p

    print "Also adding code where it hasn't been before"
    return

if __name__ == '__main__':
    main()

