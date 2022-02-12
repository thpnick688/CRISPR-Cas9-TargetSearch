# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:26:11 2022

@author: meng
"""
from CRISPRtarget import TargetSearch
from CRISPRtarget import SiteOptimize
from pathlib import Path
import sys

def Path_setup(WD):
    os.chdir(WD)
    RootDIR=Path.cwd()
    SeqFolder=RootDIR / 'fasta'
    return SeaFolder
def main():
    SeqFoldr=Path_setup(sys.argv[1])
    
if __name__ == '__main__':
    main()