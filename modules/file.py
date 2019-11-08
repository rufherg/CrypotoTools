#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: DEADF1SH_CAT
@Filename: file.py
@Time: 2019/10/7  22:38
@About: 
'''

import os
import sys

class File:
    def __init__(self, str):
        self.str = str
        self.indata = ''
        self.outdata = ''

    def read(self):
        if(os.path.isfile(self.str)):
            try:
                with open(self.str) as file:
                    self.indata = str(file.read())
                return self.indata
            except IOError:
                return False
        else:
            return False

    def write(self, str):
        self.outdata = str
        try:
            self.f = open(self.str,"w+")
            self.f.write(self.outdata)
            self.f.close()
            return True
        except IOError:
            return False

if __name__ == '__main__':
    if len(sys.argv) > 3:
        print("Argv ERROR!")
    file = File(sys.argv[1])
    print(file.read())
    file.write(sys.argv[2])
    print(file.read())