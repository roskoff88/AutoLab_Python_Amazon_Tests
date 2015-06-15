"""
Created on Mon May 25 21:21:02 2015

@author: Sebastian Rodriguez
@email: roskoff@hotmail.es
@linkedin: https://www.linkedin.com/in/sebastianr88

"""

class Basepage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver
        
    def navigate(self):
        self.driver.get(self.url)