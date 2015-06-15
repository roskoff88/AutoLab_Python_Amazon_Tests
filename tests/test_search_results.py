'''
Created on Jun 1, 2015

@author: Sebastian Rodriguez
@email: roskoff@hotmail.es
@linkedin: https://www.linkedin.com/in/sebastianr88
'''
import os
import multiprocessing
import unittest
from pages.Homepage import Homepage
from container.data_product import DataProduct
from container.data_browser import DataBrowser

class TestSearchResult(object):
    
    def __init__(self, drivers):
        # """ Initialize class with list of drivers """
        self.drivers = drivers
        
        # """ Initialize products """
        self.dataproduct = DataProduct()
        self.dataproduct.getData()
        print "Product import ... ok"
        print ""
        print "Running the search result page test for all browsers selected:"
        print ""
        
    def run(self):
        # """ The threads are created and assigned to the different browsers """
        threads = []
        
        for driver in self.drivers:
            t = multiprocessing.Process(target=self.test_search, args=(driver,))
            t.start()
            threads.append(t)
            #print (t.pid)
        
        for t in threads:
            t.join()
            #print (t.exitcode)
            
    def test_search(self,driver): 
        # Import a valid product from the data_product file
        self.product = self.dataproduct.getProduct(self.dataproduct.n)
        driverToString = str(driver)
        dn = driverToString[20:29]
        driver_name = dn.split(".")[0]
        driver_name = driver_name.upper()
        
        # ''' Access to Amazon page '''
        homepage = Homepage(driver)
        homepage.navigate()
        print str(os.getpid()) + " - " + "[" + driver_name + "] - " + "Access to Amazon page ... ok"
        
        # ''' Verify that the home page title is displayed '''
        homepage.checkHomepageTitle()
        print str(os.getpid()) + " - " + "[" + driver_name + "] - " + "The home page title is displayed ... ok"
        
        # ''' Search for a product '''
        homepage.search_product_bar(self.product)
        print str(os.getpid()) + " - " + "[" + driver_name + "] - " + "Search for a product from the data product ... ok"
        
        # ''' Verify that the search product is displayed in the page '''
        homepage.checkSearchInPage(self.product)      
        print str(os.getpid()) + " - " + "[" + driver_name + "] - " + "The search product is displayed in the page ... ok"
        
        # ''' Verify that the page displays a product's counter '''
        homepage.checkCountProductSearch()
        print str(os.getpid()) + " - " + "[" + driver_name + "] - " + "The page displays a product's counter... ok"
        
        # ''' Verify that the "Your search did not match any products." message is not displayed in the page'''
        homepage.checkNoProductMessageDisplayed()
        print str(os.getpid()) + " - " + "[" + driver_name + "] - " +  "The \"Your search did not match any products.\" message is not displayed in the page ... ok"
        
        # ''' The browser is closed. '''
        driver.close()
        #driver.quit()
        print str(os.getpid()) + " - " + "[" + driver_name + "] - " + "The browser is closed... ok"
        
class SearchResultTestCase(unittest.TestCase):
    
    def runTest(self):
        print "Starting the import data."
        # IMPORT BROWSERS
        dataBrowser = DataBrowser()
        dataBrowser.getDataBrowser()
        drivers = dataBrowser.getBrowser() #Lista con los distintos agentes a probar
        print "Drivers import ... ok"
        test = TestSearchResult(drivers)
        test.run()
        print ""
        print "Test result: PASS"
        print ""

if __name__ == "__main__":
    unittest.main()