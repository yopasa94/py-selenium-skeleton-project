import time
import datetime

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

      value = time.localtime()
      finalTime =  time.strptime('18:30:00', '%H:%M:%S')
      cont = 1
      while ((value.tm_hour==finalTime.tm_hour and value.tm_min>finalTime.tm_min)== False):
        self.accept_agreement()
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)        
        time.sleep(10)
        search_input.clear()
        print("execution round", cont)
        cont = cont + 1
        value = time.localtime()
