# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

def main():
    csv_file = File()
    filename = "C:/Users/Beheerder/Documents/GitHub/classifier/input.csv"
    obj_valuelist = csv_file.get_values(filename)
    
        
class File:
    
    def get_values(self, filename):
        start = False
        with open(filename, "r") as csv_file:
            obj_valuelist = []
            for line in csv_file:
                if re.match(r'^\d', line):
                    start = True
                if start == True:
                     line = line.replace("\n", "")
                     line = line.split(",")
                     obj = Aminoacid(line[0], line[1], line[2])
                     obj_valuelist.append(obj)
        return(obj_valuelist)
                     
        
class Aminoacid:
    def __init__(self, polarity, hydrofobicity, given):
        self.pol = polarity
        self.hyd = hydrofobicity
        self.giv = given
        
    def get_polarity(self):
        return(self.pol)
    
    def get_hydrofobicity(self):
        return(self.hyd)
    
    def get_given(self):
        return(self.giv)
    
    def predicted(self):
        return(self.pred)
    
    def error(self):
        return(self.error)
        

    
main()