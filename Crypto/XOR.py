#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: DEADF1SH_CAT
@Filename: XOR.py
@Time: 2019/10/2  18:07
@About: XOR
'''


import sys
import base64

class XOR:
    def __init__( self, str, key):
        self.str = str
        self.key = key
        self.en_str = ''
        self.de_str = ''

    def encrypto( self):
        str_len = len(self.str)
        key_len = len(self.key)
        NUM = 0
        for i in self.str:
            if NUM >= key_len:
                NUM = NUM % key_len
            self.en_str = self.en_str + chr(ord(i) ^ ord(self.key[NUM]))
            NUM = NUM + 1
        print("The encryption is", base64.b64encode(self.en_str.encode('utf-8')).decode(),"(base64-encoding)")
        return self.en_str

    def decrypto( self):
        str_len = len(self.str)
        key_len = len(self.key)
        NUM = 0
        for i in self.str:
            if NUM >= key_len:
                NUM = NUM % key_len
            self.de_str = self.de_str + chr(ord(i) ^ ord(self.key[NUM]))
            NUM = NUM + 1
        print("The decryption is", base64.b64encode(self.de_str.encode('utf-8')).decode(),"(base64-encoding)")
        return self.de_str

if __name__ == '__main__':
    if len(sys.argv) > 3:
        print("Argv ERROR!")
    xor = XOR( sys.argv[1], sys.argv[2])
    xor.encrypto()
    xor.str = xor.en_str
    xor.decrypto()