'''
Created on Jun 9, 2015

@author: Sebastian Rodriguez
@email: roskoff@hotmail.es
@linkedin: https://www.linkedin.com/in/sebastianr88
'''
from selenium import webdriver

import sys, os

PATH = lambda f: os.path.join(os.path.dirname(os.path.abspath(__file__)), f)         
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(path)

class DataBrowser(object):
    
    browser = []
    try:
        dataBrowser = open(os.path.join(PATH("DataBrowser.txt")),'r')
    except IOError:
        print "Error: can\'t find DataBrowser file or read data"
    
    def getDataBrowser(self): 
        self.dataBrowser.readline()
        try:
            for line in self.dataBrowser.readlines():
                try:
                    segmentedLine = line.split(";")
                except IOError:
                    print "Error: The DataProduct file does not have the (;) character"
                if (segmentedLine[1] == 'Yes' or segmentedLine[1] == 'yes'):
                    if (segmentedLine[0] == "Firefox"):
                        self.browser.append(webdriver.Firefox())
                    elif (segmentedLine[0] == "Chrome"):
                        self.browser.append(webdriver.Chrome())
                    elif (segmentedLine[0] == "PhantomJS"):
                        self.browser.append(webdriver.PhantomJS())
                    elif (segmentedLine[0] == "Safari"):
                        self.browser.append(webdriver.Safari())
                    elif (segmentedLine[0] == "Ie"):
                        self.browser.append(webdriver.Ie())
                    else:
                        """ Por defecto asumo Firefox """
                        print "EL NAVEGADOR INGRESADO NO ES CORRECTO"
                        print "Por defecto se ejecuta en firefox"
                        self.browser.append(webdriver.Firefox())
        except IOError:
            print "Error: The DataBrowser file is empty."
        
    def getBrowser(self):
        return self.browser