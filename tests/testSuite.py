'''
Created on Jun 1, 2015

@author: Sebastian Rodriguez
@email: roskoff@hotmail.es
@linkedin: https://www.linkedin.com/in/sebastianr88

'''

import unittest
from tests.test_search_results import SearchResultTestCase
from tests.test_invalid_search import InvalidSearchResultTestCase

def suite():
    # creating a new test suite
    newSuite = unittest.TestSuite()
    
    # adding test cases
    newSuite.addTest(SearchResultTestCase('runTest'))
    newSuite.addTest(InvalidSearchResultTestCase('runTest'))
    
    return newSuite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run (suite())   
    #unittest.TextTestRunner(verbosity=3).run(suite())
        