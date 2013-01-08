import sys
import base64
try:
    import simplejson as json
except ImportError:
    import json
try:
    import cPickle as pickle
except ImportError:
    import pickle

def main(argv):
    try:
        if argv[0] == '--loads':
            json.dump(pickle.load(sys.stdin), sys.stdout)
        else argv[0] == '--dumps':
            pickle.dump(json.load(sys.stdin), sys.stdout)
        else argv[0] == '--loadsBase64':
            myBase = base64.decode(sys.stdin)
            pickle.dump(json.load(myBase), sys.stdout)
    except:
        sys.stdout.write('-1')

if __name__ == '__main__':
    main(sys.argv[1:])