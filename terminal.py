import getopt
import sys
import Help
import window


def main(argv):
    d = {'-s': 's', '-d': 'd', '-p': 'p', '-t': 't', '-m': 'm'}
    cmp = ""
    text = list()
    try:
        opts, args = getopt.getopt(argv, "hsdptm::",)
    except getopt.GetoptError:
        #print("1\n")
        Help.main()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            Help.main()
            sys.exit()
        elif opt in d:
            cmp = d[opt]
        text = sys.argv[3:]
    try:
        if sys.argv[2] == "":
            raise Exception('No dialog name')
            sys.exit(2)
    except:
        print("No dialog name")
        sys.exit(2)
    window.main(cmp, sys.argv[2], text)


if __name__ == '__main__':
    main(sys.argv[1:])
