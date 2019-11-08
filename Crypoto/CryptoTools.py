#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: DEADF1SH_CAT
@Filename: CryptoTools.py
@Time: 2019/10/2  23:09
@About: CryptoTools
'''

import sys
import argparse
from XOR import XOR
from file import File

def init():
    print(
"""
Cryptographic Tools
-h or --help : 显示帮助信息
-s or --str  : 需要加密的字符串
-k or --key  : 密钥
-x or --xor  : 进行异或加解密
-b64 or --base64 : 进行base64编码或解码(未完成)
-b58 or --base58 : 进行base58编码或解码(未完成)
-i or --infile  : 需要加密的文件路径
-o or --outfile : 解密后的文件路径
-e or --encrypto : 选择加密
-d or --decrypto : 选择解密
"""
    )

def index():
    ter_opt={}
    parser = argparse.ArgumentParser(description='Cryptographic Tools',add_help=True)
    parser.add_argument('-s','--str',default=None,help='需要加密的字符串', type=str)
    parser.add_argument('-k','--key',default=None,help='密钥', type=str)
    parser.add_argument('-x','--xor',default=None,help='进行异或加解密',action="store_true")
    parser.add_argument('-b64','--base64',default=None,help='进行base64编码或解码(未完成)',action="store_true")
    parser.add_argument('-b58','--base58',default=None,help='进行base58编码或解码(未完成)',action="store_true")
    parser.add_argument('-i','--infile',default=None,help='需要加密的文件路径', type=str)
    parser.add_argument('-o','--outfile',default=None,help='解密后的文件路径', type=str)
    parser.add_argument('-e','--encrypto',default=None,help='选择加密',action="store_true")
    parser.add_argument('-d','--decrypto',default=None,help='选择解密',action="store_true")
    args = parser.parse_args()

    if args.str and args.infile:
        print("Args Error!")
        exit()

    if args.xor and args.key and (args.encrypto or args.decrypto):
        if args.str:
            xor = XOR(args.str, args.key)
            result = xor.encrypto()
            if args.outfile:
                if(File(args.outfile).write(result)):
                    print("Write file success!")
                else:
                    print("ERROR!")

        if args.infile:
            if(File(args.infile).read()):
                xor = XOR(File(args.infile).read(), args.key)
                result = xor.encrypto()
                if args.outfile:
                    if (File(args.outfile).write(result)):
                        print("Write file success!")
                    else:
                        print("ERROR!")
            else:
                print("File not exist!")

if len(sys.argv) == 1:
    sys.argv.append('-h')

if __name__ == '__main__':
    index()