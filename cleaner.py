#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys

def main():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')
if __name__ == '__main__':
    main()
