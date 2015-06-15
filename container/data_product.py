'''
Created on May 31, 2015

@author: Sebastian Rodriguez
@email: roskoff@hotmail.es
@linkedin: https://www.linkedin.com/in/sebastianr88

'''
import sys, os

PATH = lambda f: os.path.join(os.path.dirname(os.path.abspath(__file__)), f)         
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(path)

class DataProduct(object):
    i=0
    n=-1
    product = []
    invalidProduct = []
    try:
        file = open(os.path.join(PATH("DataProduct.txt")),'r')
    except IOError:
        print "Error: can\'t find DataProduct file or read data"
       
    
    def getData(self): 
        self.file.readline()
        try:
            for line in self.file.readlines():
                try:
                    segmentedLine = line.split(";")
                except IOError:
                    print "Error: The DataProduct file does not have the (;) character"
                self.product.append(segmentedLine[0])
                self.invalidProduct.append(segmentedLine[1])
                self.i += 1
        except IOError:
            print "Error: The DataProduct file is empty."
        if (self.n+1 == self.i):
            self.n=0
        else:
            self.n += 1
        
            
    def getProduct(self,n):
        return self.product[n]
    
    def getInvalidProduct(self,n):
        return self.invalidProduct[n]