#!/bin/python3
#coding: utf-8

# read config
watchlist = [ ] # files path .... to watch integrity

algo_hash = "sha512"

import hashlib
from base64 import b64encode as benc
from base64 import b64decode as bdec




class Dog(object):
    def __init__(self):
        self.logfilepath="grrr.log"

    def watch(self,filepath):
        with open(filepath, "rb") as f:
            data = f.read()
            f.close()
        h = hashlib.sha3_512(data)
        return h.hexdigest().decode()

    def whooaf(self,title,message):
        pass

    def grrr(self):
        with open(self.logfilepath, "a") as f:
            f.write("{}\n".format(self.changes))
            f.close()

    def storeCurrentBones(self):
        pass

    def undoVersion(self):
        pass

    def extract(self,file)
