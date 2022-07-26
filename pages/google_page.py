from re import I
import time
import datetime

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib.app import get_final_time, kill_slack


class GooglePage(BasePage):
    SEARCH_INPUT = (By.NAME, 'q')
    FEELING_LUCKY = (By.NAME, 'btnI')
    SEARCH_BUTTON = (By.NAME, 'btnK')
    RESULTS_LIST = (By.XPATH, '//h3[contains(@class, "LC20lb")]')
    AGREE_POPUP = (By.XPATH, '//*[@id="introAgreeButton"]/span/span')
    IFRAME = (By.XPATH, '//iframe')

    def accept_agreement(self):
        try:
            iframe = self.driver.find_element(*self.IFRAME)
            self.driver.switch_to.frame(iframe)
            agree_popup = self.driver.find_element(*self.AGREE_POPUP)
            agree_popup.click()
            self.driver.switch_to.default_content()
        except:
            pass

    def normal_search(self, phrase):
      cont = 1
      is_valid_time= self.is_valid_time()
      while (is_valid_time==True):
        self.accept_agreement()
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)        
        time.sleep(60*5)
        search_input.clear()
        print("INFO: Execution Round", cont)
        cont = cont + 1
        
      if(is_valid_time==False):
        print("INFO: Killing Slack at -->",time.localtime().tm_hour,":",time.localtime().tm_min )
        kill_slack()
      
      

    def is_valid_time(self):
      finalTime =  time.strptime(get_final_time(), '%H:%M:%S')
      value = time.localtime()
      return ((value.tm_hour==finalTime.tm_hour and value.tm_min>finalTime.tm_min)== False)