#!/usr/bin/python
# -*- coding: utf8 -*-
#Genarate Weekly Report
__author__ = 'Tan Ying<ying.tan@tcl.com>'

import re

DATA_PATH = './data/'
BIN_PATH = './bin/'
OG_FILE = DATA_PATH + 'og.txt' #ongoing defects
IN_FILE = DATA_PATH + 'in.txt' #weekly in defects
OUT_FILE = DTAT_PATH + 'out.txt' #weekly out defects

OGList = []
INList = []
OUTList = []

class Defect:
    def __init__(self):
        self.id = '' #A
        self.project = '' #B
        self.assigner = '' #C
        self.summary = '' #D
        self.state = '' #E

def main():
    #login to ALM (Manually gen the 3 excel)

    #count the source to dict
    f = open(OG_FILE, 'r')

    while True:
        line = f.readline()
        if not line:
            break
        else:
            parse_line(line)

def parse_line(s):
    defect = Defect()
    defect.id = s[:6]
    if s.find('')
    defect.project = s[7:]

def get_defect_project(s):
    m1 = re.match(r'\/TCT\/GApp\/CameraL', s)
    m2 = re.match(r'\/TCT\/QCT MSM8952\/Idol4', s)
    m3 = re.match(r'\/TCT\/QCT MSM8976\/Idol4 S', s)
    m4 = re.match(r'\/TCT\/QCT MSM8976\/Idol4 S VF', s)
    if m4:
        return idol4svf
    else:
        if m3:
            return idol4s
        else:
            if m2:
            




if __name__ == '__main__':
    main()