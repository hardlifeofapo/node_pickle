#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import base64
from cStringIO import StringIO

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
        elif argv[0] == '--dumps':
            pickle.dump(json.load(sys.stdin), sys.stdout)
        elif argv[0] == '--loadsBase64':
            raw_data = sys.stdin.readline()
            encoded_data = base64.b64decode(raw_data)
            hash, pickled = encoded_data.split(b':', 1)
            json.dump(pickle.loads(pickled), sys.stdout)

    except Exception as inst:
        print inst
        sys.stdout.write('-1')

if __name__ == '__main__':
    main(sys.argv[1:])