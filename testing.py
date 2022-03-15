# import webdriver 
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.support.ui import Select
from time import sleep
import HtmlTestRunner
class prediction(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.driver.implicitly_wait(25)
		self.driver.maximize_window() 
  
	def test_web(self):
		self.driver.get("http://127.0.0.1:5000/")
		element = self.driver.find_element_by_id("Dep_Time")
		element.send_keys("01022021")
		element.send_keys(Keys.TAB)
		element.send_keys('0245PM')
		element1 = self.driver.find_element_by_id("Arrival_Time")
		element1.send_keys("01032021")
		element1.send_keys(Keys.TAB)
		element1.send_keys('0100PM')
		element2 = self.driver.find_element_by_id("Source")
		drp = Select(element2)
		drp.select_by_index(2)
		element3 = self.driver.find_element_by_id("Destination")
		drp1 = Select(element3)
		drp1.select_by_index(3)
		element4 = self.driver.find_element_by_name("stops")
		drp2 = Select(element4)
		drp2.select_by_index(1)
		element5 = self.driver.find_element_by_id("airline")
		drp3 = Select(element5)
		drp3.select_by_index(5)
		sleep(4)
		self.driver.find_element_by_id("a").click()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))		