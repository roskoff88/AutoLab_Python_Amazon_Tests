"""
Created on Mon May 25 21:21:02 2015

@author: Sebastian Rodriguez
@email: roskoff@hotmail.es
@linkedin: https://www.linkedin.com/in/sebastianr88

"""


from pages.Basepage import Basepage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Homepage(Basepage):
    # Page URL
    url = "https://www.amazon.com/"
    
    # Locators
    _Search_bar_locator = (By.XPATH, ".//*[@id='twotabsearchtextbox']")
    _Result_count_locator = (By.ID, "s-result-count")
    _No_Result_title_locator = (By.ID, "noResultsTitle")

    
    # Actions
    def checkHomepageTitle(self):
        assert 'Amazon' in self.driver.title
        
    def search_product_bar(self, product):
        elem = self.driver.find_element(*self._Search_bar_locator)
        elem.send_keys(product)
        elem.send_keys(Keys.ENTER)
    
    def checkSearchInPage(self, product):
        assert product in self.driver.page_source 
    
    def checkCountProductSearch(self):
        elem = self.driver.find_element(*self._Result_count_locator)
        assert elem is not None
        
    def checkNoProductMessageDisplayed(self):
        assert "Your search did not match any products." not in self.driver.page_source  
    
    def checkProductMessageDisplayed(self,product):
        elem = self.driver.find_element(*self._No_Result_title_locator)
        msg = "Your search \"" + product + "\" did not match any products."
        assert msg in elem.text 
    
        
        
        
    
    
    