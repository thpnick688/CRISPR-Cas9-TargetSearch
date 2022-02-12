# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:21:12 2022
This is a re-write of my previous CRISPR/Cas9 target search tool. with OOP programing
The code below are the collection of the in-built defined function. Please use the Main.py to run the code
@author: R.L
"""
import re
from pathlib import Path
class TargetSearch():
    def __init__(self, WD):
        self.WD=Path(WD)
    def RawSeq_Process(self):
        fasta_Path=self.WD/'fata'
        seq=open(fasta_Path,'r')
        seq_head=str()
        seq_body=str()
        for line in seq:
            if re.search('>',line):
                seq_head=line
            else:
                line.strip('\n')
                line.strip('\t')
                seq_body=seq_body+line
        return seq_head,seq_body
    def Seq_Sotre(self,fileList):
        Seq_Dict={}
        for file in fileList:
            file_path=WD/file
            seq_head,seq_body=RawSeq_Process(file_Path)[0],RawSeq_Process(file_Path)[1]
            Seq_Dict={seq_head:seq_body}
        return Seq_Dict
#     def SiteSearch(self):
#         Seq_Dict=self.Seq_Dict
#         OutFile=self.OutFile
#         WD=self.WD
#         OutFile=open(WD/OutFile,'a')
#         CutSite_List=['ATT','TTT','CTT','GTT']
#         Target_Length=range(20,25,1)
#         for key in Seq_Dict.keys:
#             seq_body=Seq_Dict[key]
#             for CutSite in CutSite_List:
#                 CutSite_Pos=re.findall(CutSite,seq_body)
#                 for length in Target_Lenght:
#                     Begin_Pos=CutSite_Pos-length
#                     End_Pos=CutSite_Pos-1
#                     if Begin_Pos<0:
#                         Skip
#                     else:
#                         print(seq_body[Begin_Pos])
#                         Begin_Pos=Begin_Pos+1
#                     else
                
            
# class SiteOptimize():
#     def __init__(self):
#         self.WD=WD
#     def GC_content(self):
        
            
        

